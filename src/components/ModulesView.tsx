/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { BookOpen, Sparkles, Play, ShieldAlert, Layers } from 'lucide-react';
import { Question } from '../types';
import { PROVISIONAL_MODULES } from '../data/questionBank';

interface ModulesViewProps {
  questions: Question[];
  onStartPractice: (module: string) => void;
  onStartLearning: (module: string) => void;
  onStartMock: () => void;
}

export const ModulesView: React.FC<ModulesViewProps> = ({
  questions,
  onStartPractice,
  onStartLearning,
  onStartMock,
}) => {
  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-semibold text-xs mb-1">
            <Layers className="w-4 h-4" />
            <span>Curriculum & Specialty Modules</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
            Mental Health Nursing Modules ({PROVISIONAL_MODULES.length})
          </h2>
          <p className="text-slate-500 dark:text-slate-400 text-xs sm:text-sm mt-1">
            Select a module to begin targeted MCQ practice or interactive learning mode with immediate explanations.
          </p>
        </div>
        <button
          onClick={onStartMock}
          className="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-2.5 rounded-xl text-xs sm:text-sm flex items-center gap-2 shadow-md shadow-emerald-600/20 shrink-0 cursor-pointer"
        >
          <Sparkles className="w-4 h-4" />
          <span>Launch Mock Examination</span>
        </button>
      </div>

      {/* Modules Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {PROVISIONAL_MODULES.map((moduleName) => {
          const modQuestions = questions.filter(q => q.module === moduleName);
          const count = modQuestions.length;

          return (
            <div
              key={moduleName}
              className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 shadow-xs flex flex-col justify-between hover:border-emerald-500/50 transition-all group"
            >
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                    {count} {count === 1 ? 'Question' : 'Questions'}
                  </span>
                  <BookOpen className="w-5 h-5 text-slate-400 group-hover:text-emerald-600 transition-colors" />
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white text-base mb-2">
                  {moduleName}
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400 line-clamp-2">
                  {count > 0 
                    ? `Covers core postgraduate clinical concepts, nursing interventions, and evidence-based rationales.`
                    : `Additional sample questions in preparation for upcoming syllabus expansion.`}
                </p>
              </div>

              <div className="mt-6 pt-4 border-t border-slate-100 dark:border-slate-800 flex items-center gap-2">
                <button
                  disabled={count === 0}
                  onClick={() => onStartPractice(moduleName)}
                  className={`flex-1 flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl text-xs font-semibold transition-all ${
                    count > 0 
                      ? 'bg-slate-900 dark:bg-slate-800 text-white hover:bg-emerald-600 dark:hover:bg-emerald-600 cursor-pointer' 
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-400 cursor-not-allowed'
                  }`}
                >
                  <Play className="w-3.5 h-3.5 fill-current" />
                  <span>Practice</span>
                </button>
                <button
                  disabled={count === 0}
                  onClick={() => onStartLearning(moduleName)}
                  className={`flex-1 flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl text-xs font-semibold transition-all ${
                    count > 0 
                      ? 'bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 hover:bg-emerald-100 dark:hover:bg-emerald-900 border border-emerald-200 dark:border-emerald-800 cursor-pointer' 
                      : 'bg-slate-100 dark:bg-slate-800 text-slate-400 cursor-not-allowed border border-transparent'
                  }`}
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Learn Mode</span>
                </button>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
