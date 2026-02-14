"use client";

interface PipeConnectorProps {
  direction?: "horizontal" | "vertical";
}

export function PipeConnector({ direction = "horizontal" }: PipeConnectorProps) {
  if (direction === "vertical") {
    return (
      <div className="flex justify-center py-1">
        <div className="w-0.5 h-8 pipe-flow-line rounded-full" />
      </div>
    );
  }

  return (
    <div className="flex items-center shrink-0 mx-1">
      <div className="h-0.5 w-8 pipe-flow-line rounded-full" />
    </div>
  );
}
