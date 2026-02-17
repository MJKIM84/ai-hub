const SLACK_WEBHOOK_URL = process.env.SLACK_WEBHOOK_URL;

interface SlackMessage {
  text: string;
  blocks?: Record<string, unknown>[];
}

export async function sendSlackMessage(message: SlackMessage): Promise<boolean> {
  if (!SLACK_WEBHOOK_URL) {
    console.warn("[Slack] SLACK_WEBHOOK_URL not configured");
    return false;
  }

  try {
    const res = await fetch(SLACK_WEBHOOK_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(message),
      signal: AbortSignal.timeout(10000),
    });
    return res.ok;
  } catch (err) {
    console.error("[Slack] Failed to send message:", err);
    return false;
  }
}

interface CrawlReport {
  crawlRunId: string;
  sourcesChecked: number;
  urlsDiscovered: number;
  urlsNew: number;
  urlsDuplicate: number;
  servicesCreated: number;
  errors: string[];
}

interface ValidationReportInput {
  totalChecked: number;
  passed: number;
  warnings: {
    serviceName: string;
    serviceUrl: string;
    type: string;
    message: string;
    severity: "error" | "warning";
  }[];
}

export async function sendValidationReport(report: ValidationReportInput): Promise<boolean> {
  if (report.totalChecked === 0) return true;

  const now = new Date().toLocaleString("ko-KR", { timeZone: "Asia/Seoul" });
  const hasIssues = report.warnings.length > 0;
  const emoji = hasIssues ? "⚠️" : "✅";
  const errorCount = report.warnings.filter(w => w.severity === "error").length;
  const warningCount = report.warnings.filter(w => w.severity === "warning").length;

  let issueText = "";
  if (hasIssues) {
    const grouped = new Map<string, string[]>();
    for (const w of report.warnings.slice(0, 10)) {
      const key = w.serviceName;
      if (!grouped.has(key)) grouped.set(key, []);
      grouped.get(key)!.push(`${w.severity === "error" ? "🔴" : "🟡"} ${w.message}`);
    }

    const lines: string[] = [];
    for (const [name, issues] of grouped) {
      lines.push(`*${name}*`);
      issues.forEach(i => lines.push(`  ${i}`));
    }
    issueText = lines.join("\n");
    if (report.warnings.length > 10) {
      issueText += `\n...외 ${report.warnings.length - 10}건`;
    }
  }

  return sendSlackMessage({
    text: `${emoji} 크롤링 데이터 검증 완료`,
    blocks: [
      {
        type: "header",
        text: {
          type: "plain_text",
          text: `${emoji} 크롤링 데이터 검증 리포트`,
        },
      },
      {
        type: "section",
        fields: [
          { type: "mrkdwn", text: `*검증 시각:*\n${now}` },
          { type: "mrkdwn", text: `*검증 서비스:*\n${report.totalChecked}개` },
          { type: "mrkdwn", text: `*통과:*\n${report.passed}개` },
          { type: "mrkdwn", text: `*이슈:*\n🔴 ${errorCount} / 🟡 ${warningCount}` },
        ],
      },
      ...(hasIssues
        ? [
            {
              type: "section",
              text: {
                type: "mrkdwn",
                text: issueText,
              },
            },
          ]
        : []),
    ],
  });
}

export async function sendCrawlReport(result: CrawlReport): Promise<boolean> {
  const hasErrors = result.errors.length > 0;
  const emoji = hasErrors ? "⚠️" : result.servicesCreated > 0 ? "🎉" : "✅";
  const status = hasErrors ? "일부 오류 발생" : "정상 완료";

  const now = new Date().toLocaleString("ko-KR", { timeZone: "Asia/Seoul" });

  const errorSection = hasErrors
    ? `\n\n❌ *오류 (${result.errors.length}건)*\n${result.errors.slice(0, 5).map((e) => `• ${e.substring(0, 100)}`).join("\n")}${result.errors.length > 5 ? `\n...외 ${result.errors.length - 5}건` : ""}`
    : "";

  return sendSlackMessage({
    text: `${emoji} 일일 AI 서비스 크롤링 ${status}`,
    blocks: [
      {
        type: "header",
        text: {
          type: "plain_text",
          text: `${emoji} 일일 AI 서비스 크롤링 리포트`,
        },
      },
      {
        type: "section",
        fields: [
          { type: "mrkdwn", text: `*상태:*\n${status}` },
          { type: "mrkdwn", text: `*실행 시각:*\n${now}` },
          { type: "mrkdwn", text: `*검사한 소스:*\n${result.sourcesChecked}개` },
          { type: "mrkdwn", text: `*발견된 URL:*\n${result.urlsDiscovered}개` },
          { type: "mrkdwn", text: `*신규 URL:*\n${result.urlsNew}개` },
          { type: "mrkdwn", text: `*중복:*\n${result.urlsDuplicate}개` },
        ],
      },
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `🆕 *새로 등록된 서비스: ${result.servicesCreated}개*${errorSection}`,
        },
      },
      {
        type: "context",
        elements: [
          {
            type: "mrkdwn",
            text: `Crawl Run ID: \`${result.crawlRunId}\``,
          },
        ],
      },
    ],
  });
}
