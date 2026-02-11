"use client";

import { useState } from "react";
import { ThumbsUp, ThumbsDown, Check } from "lucide-react";
import { formatNumber } from "@/lib/utils";

interface ServiceVotePanelProps {
  serviceId: string;
  initialUpvotes: number;
  initialDownvotes: number;
}

export function ServiceVotePanel({ serviceId, initialUpvotes, initialDownvotes }: ServiceVotePanelProps) {
  const [upvotes, setUpvotes] = useState(initialUpvotes);
  const [downvotes, setDownvotes] = useState(initialDownvotes);
  const [upvoted, setUpvoted] = useState(false);
  const [downvoted, setDownvoted] = useState(false);

  const handleVote = async (type: "upvote" | "downvote") => {
    if (type === "upvote" && upvoted) return;
    if (type === "downvote" && downvoted) return;

    try {
      const res = await fetch("/api/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ serviceId, type }),
      });
      const data = await res.json();

      if (type === "upvote") {
        if (data.alreadyVoted || res.ok) setUpvoted(true);
        if (res.ok && !data.alreadyVoted) setUpvotes(data.upvotes);
      } else {
        if (data.alreadyVoted || res.ok) setDownvoted(true);
        if (res.ok && !data.alreadyVoted) setDownvotes(data.downvotes);
      }
    } catch {}
  };

  return (
    <div className="flex items-center gap-3 my-6">
      <button
        onClick={() => handleVote("upvote")}
        disabled={upvoted}
        className={`flex items-center gap-2 px-5 py-3 rounded-xl text-sm font-medium transition-all duration-200
          ${upvoted
            ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-neon-blue cursor-default"
            : "dark:bg-white/5 bg-black/5 dark:hover:bg-neon-blue/20 hover:bg-neon-blue/10 dark:text-zinc-300 text-zinc-600 dark:hover:text-neon-blue hover:text-neon-blue"
          }`}
      >
        {upvoted ? <Check className="w-4 h-4" /> : <ThumbsUp className="w-4 h-4" />}
        추천 {formatNumber(upvotes)}
      </button>

      <button
        onClick={() => handleVote("downvote")}
        disabled={downvoted}
        className={`flex items-center gap-2 px-5 py-3 rounded-xl text-sm font-medium transition-all duration-200
          ${downvoted
            ? "dark:bg-pink-500/20 bg-pink-500/10 dark:text-pink-400 text-pink-600 cursor-default"
            : "dark:bg-white/5 bg-black/5 dark:hover:bg-pink-500/20 hover:bg-pink-500/10 dark:text-zinc-300 text-zinc-600 dark:hover:text-pink-400 hover:text-pink-600"
          }`}
      >
        {downvoted ? <Check className="w-4 h-4" /> : <ThumbsDown className="w-4 h-4" />}
        비추천 {formatNumber(downvotes)}
      </button>
    </div>
  );
}
