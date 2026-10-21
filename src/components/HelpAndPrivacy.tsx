/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { HelpCircle, ShieldCheck, Database, FileText, Lock, Sparkles } from 'lucide-react';

export const HelpAndPrivacy: React.FC = () => {
  return (
    <div className="max-w-4xl mx-auto space-y-6 pb-12">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs">
        <div className="inline-flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-semibold text-xs mb-1">
          <HelpCircle className="w-4 h-4" />
          <span>Candidate Guidance & Documentation</span>
        </div>
        <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
          Application Help & Privacy Notice
        </h2>
        <p className="text-slate-500 dark:text-slate-400 text-xs sm:text-sm mt-1">
          Everything you need to know about using the WAPCNM Postgraduate Mental Health Nursing Examination Preparation Portal.
        </p>
      </div>

      {/* Sections */}
      <div className="grid grid-cols-1 gap-6">
        {/* Pass Mark & Scoring */}
        <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-3">
          <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-emerald-600" />
            <span>Scoring & Pass Mark Threshold (70%)</span>
          </h3>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            The application enforces a strict educational pass mark threshold of <strong>70.0%</strong>. Percentages are calculated as <code className="bg-slate-100 dark:bg-slate-800 px-1.5 py-0.5 rounded text-emerald-600 font-mono">(Correct Answers / Total Scored Questions) × 100</code> using unrounded floating-point evaluation. Unanswered questions are automatically counted as incorrect.
          </p>
        </div>

        {/* Persistent Storage & Privacy */}
        <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-3">
          <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <Database className="w-5 h-5 text-emerald-600" />
            <span>Privacy & IndexedDB Browser Storage</span>
          </h3>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            Version 1.0 operates entirely client-side using browser IndexedDB storage. No candidate personal data, assessment scores, or reports are transmitted to external servers or cloud databases. Candidates are strongly advised to download and save completed HTML reports to their local Documents folder or personal cloud storage.
          </p>
        </div>

        {/* Syllabus Modules */}
        <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-3">
          <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-emerald-600" />
            <span>Provisional Module Structure</span>
          </h3>
          <p className="text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
            The question bank covers 14 provisional specialty modules spanning Foundations of Mental Health Nursing, Psychiatric Assessment & MSE, Psychopathology, Psychopharmacology, Therapeutic Communication, Psychiatric Emergencies, Community Mental Health, Ethics, Law, and Advanced Clinical Scenarios.
          </p>
        </div>
      </div>
    </div>
  );
};
