/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { FileText, Award, Calendar, Download, ArrowRight, Trash2, ShieldCheck, AlertTriangle } from 'lucide-react';
import { AssessmentReport } from '../types';

interface MyReportsProps {
  reports: AssessmentReport[];
  onOpenReport: (reportId: string) => void;
  onClearHistory?: () => void;
}

export const MyReports: React.FC<MyReportsProps> = ({
  reports,
  onOpenReport
}) => {
  const handleExportJSON = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(reports, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `WAPCNM_Reports_Backup_${Date.now()}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  };

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-semibold text-xs mb-1">
            <FileText className="w-4 h-4" />
            <span>Persistent Browser Reports</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
            My Examination Reports ({reports.length})
          </h2>
          <p className="text-slate-500 dark:text-slate-400 text-xs sm:text-sm mt-1">
            Access, review, and download completed assessment reports saved securely in your browser's IndexedDB storage.
          </p>
        </div>

        {reports.length > 0 && (
          <button
            onClick={handleExportJSON}
            className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold flex items-center gap-2 cursor-pointer transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Export All as JSON Backup</span>
          </button>
        )}
      </div>

      {/* Reports List */}
      {reports.length === 0 ? (
        <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-12 text-center space-y-3">
          <AlertTriangle className="w-12 h-12 text-amber-500 mx-auto opacity-80" />
          <h3 className="text-lg font-bold text-slate-800 dark:text-slate-200">No Examination Reports Found</h3>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 max-w-md mx-auto">
            You have not completed any practice sessions or mock examinations yet. Complete an assessment to generate your permanent report.
          </p>
        </div>
      ) : (
        <div className="grid grid-cols-1 gap-4">
          {reports.map((report) => (
            <div
              key={report.id}
              onClick={() => onOpenReport(report.id)}
              className="bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs hover:border-emerald-500/50 transition-all cursor-pointer flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 group"
            >
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold px-2.5 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    {report.id}
                  </span>
                  <span className="text-xs text-slate-400 flex items-center gap-1">
                    <Calendar className="w-3.5 h-3.5" />
                    {new Date(report.dateTimestamp).toLocaleString()}
                  </span>
                </div>
                <h3 className="font-bold text-slate-900 dark:text-white text-base sm:text-lg group-hover:text-emerald-600 transition-colors">
                  {report.assessmentTitle}
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  Candidate: {report.candidateName} • {report.correctCount} correct out of {report.totalQuestions} questions
                </p>
              </div>

              <div className="flex items-center gap-4 w-full sm:w-auto justify-between sm:justify-end pt-3 sm:pt-0 border-t sm:border-t-0 border-slate-100 dark:border-slate-800">
                <div className="text-right">
                  <span className={`inline-block px-3 py-1 rounded-xl text-xs font-bold ${
                    report.status === 'PASS' 
                      ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-200' 
                      : 'bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-200'
                  }`}>
                    {report.percentage.toFixed(1)}% — {report.status}
                  </span>
                  <span className="block text-[10px] text-slate-400 mt-0.5">Pass mark: 70.0%</span>
                </div>

                <div className="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-600 dark:text-slate-300 group-hover:bg-emerald-600 group-hover:text-white transition-all">
                  <ArrowRight className="w-4 h-4" />
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
