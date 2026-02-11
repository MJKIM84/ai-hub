"use client";

import { useState } from "react";
import { ThumbsUp, ThumbsDown } from "lucide-react";
import { formatNumber } from "@/lib/utils";

interface ServiceVotePanelProps {
  serviceId: string;
  initialUpvotes: number;
  initialDownvotes: number;
}

type VoteState = "upvote" | "downvote" | null;

export function ServiceVotePanel({ serviceId, initialUpvotes, initialDownvotes }: ServiceVotePanelProps) {
  const [upvotes, setUpvotes] = useState(initialUpvotes);
  const [downvotes, setDownvotes] = useState(initialDownvotes);
  const [currentVote, setCurrentVote] = useState<VoteState>(null);
  const [loading, setLoading] = useState(false);

  const handleVote = async (type: "upvote" | "downvote") => {
    if (loading) return;
    setLoading(true);

    try {
      const res = await fetch("/api/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ serviceId, type }),
      });
      const data = await res.json();

      if (res.ok) {
        setUpvotes(data.upvotes);
        setDownvotes(data.downvotes);

        if (data.action === "cancelled") {
          setCurrentVote(null);
        } else if (data.action === "switched" || data.action === "voted") {
          setCurrentVote(type);
        }
      }
    } catch {} finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center gap-3 my-6">
      <button
        onClick={() => handleVote("upvote")}
        disabled={loading}
        className={`flex items-center gap-2 px-5 py-3 rounded-xl text-sm font-medium transition-all duration-200
          ${currentVote === "upvote"
            ? "dark:bg-neon-blue/20 bg-neon-blue/10 dark:text-neon-blue text-neon-blue ring-1 dark:ring-neon-blue/30 ring-neon-blue/20"
            : "dark:bg-white/5 bg-black/5 dark:hover:bg-neon-blue/20 hover:bg-neon-blue/10 dark:text-zinc-300 text-zinc-600 dark:hover:text-neon-blue hover:text-neon-blue"
          } disabled:opacity-50`}
      >
        <ThumbsUp className={`w-4 h-4 ${currentVote === "upvote" ? "fill-current" : ""}`} />
        추천 {formatNumber(upvotes)}
      </button>

      <button
        onClick={() => handleVote("downvote")}
        disabled={loading}
        className={`flex items-center gap-2 px-5 py-3 rounded-xl text-sm font-medium transition-all duration-200
          ${currentVote === "downvote"
            ? "dark:bg-pink-500/20 bg-pink-500/10 dark:text-pink-400 text-pink-600 ring-1 dark:ring-pink-500/30 ring-pink-500/20"
            : "dark:bg-white/5 bg-black/5 dark:hover:bg-pink-500/20 hover:bg-pink-500/10 dark:text-zinc-300 text-zinc-600 dark:hover:text-pink-400 hover:text-pink-600"
          } disabled:opacity-50`}
      >
        <ThumbsDown className={`w-4 h-4 ${currentVote === "downvote" ? "fill-current" : ""}`} />
        비추천 {formatNumber(downvotes)}
      </button>

      {currentVote && (
        <span className="text-xs dark:text-zinc-500 text-zinc-400 ml-1">
          다시 클릭하면 취소됩니다
        </span>
      )}
    </div>
  );
}
