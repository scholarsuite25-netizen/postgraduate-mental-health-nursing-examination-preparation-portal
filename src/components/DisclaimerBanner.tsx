/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { AlertCircle, ShieldCheck } from 'lucide-react';

export const DisclaimerBanner: React.FC = () => {
  return (
    <div className="bg-amber-50 dark:bg-amber-950/40 border-b border-amber-200 dark:border-amber-800/60 px-4 py-2.5 text-xs text-amber-900 dark:text-amber-200">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-center sm:text-left">
          <AlertCircle className="w-4 h-4 shrink-0 text-amber-600 dark:text-amber-400" />
          <span>
            <strong>Independent Educational Resource:</strong> This portal is an independent specialty examination preparation tool for postgraduate Mental Health Nursing candidates and is not an official portal of the West African Postgraduate College of Nurses and Midwives (WAPCNM).
          </span>
        </div>
        <div className="flex items-center gap-1.5 shrink-0 text-[11px] font-medium bg-amber-100/80 dark:bg-amber-900/60 px-2.5 py-1 rounded-full text-amber-800 dark:text-amber-300">
          <ShieldCheck className="w-3.5 h-3.5" />
          <span>Pass Mark Threshold: Fixed at 70%</span>
        </div>
      </div>
    </div>
  );
};
