/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
@@ -1,1 +1,35 @@
 */

import React from 'react';
import { Sparkles, Quote } from 'lucide-react';

const EXAM_QUOTES = [
  {
    quote: "Excellence in mental health nursing is not an act, but a habit of compassionate clinical rigor and continuous evidence-based preparation.",
    author: "WAPCNM Specialty Candidate Motivation"
  },
  {
    quote: "Your postgraduate specialty examination is the gateway to elevating psychiatric nursing standards across West Africa. Prepare with absolute diligence.",
    author: "Clinical Leadership Council"
  },
  {
    quote: "Every MCQ mastered today translates directly into life-saving therapeutic interventions and empathetic patient advocacy tomorrow.",
    author: "Mental Health Nursing Excellence"
  }
];

export const QuoteOfTheDay: React.FC = () => {
  // Select quote based on day of year
  const dayOfYear = Math.floor((Date.now() - new Date(new Date().getFullYear(), 0, 0).getTime()) / (1000 * 60 * 60 * 24));
  const currentQuote = EXAM_QUOTES[dayOfYear % EXAM_QUOTES.length];

  return (
    <div className="bg-gradient-to-r from-emerald-600 via-teal-600 to-emerald-700 text-white px-4 py-3 shadow-sm">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2 text-xs sm:text-sm">
        <div className="flex items-center gap-2.5 text-center sm:text-left">
          <Quote className="w-4 h-4 shrink-0 text-emerald-200 fill-emerald-200 opacity-80" />
          <span>
            <strong>Daily Examination Inspiration:</strong> &ldquo;{currentQuote.quote}&rdquo; — <span className="italic opacity-90">{currentQuote.author}</span>
          </span>
        </div>
        <div className="flex items-center gap-1.5 shrink-0 bg-white/10 px-2.5 py-1 rounded-full text-[11px] font-medium backdrop-blur-xs">
          <Sparkles className="w-3.5 h-3.5 text-amber-300" />
          <span>Pass Mark: 70% Threshold</span>
        </div>
      </div>
    </div>
  );
};
