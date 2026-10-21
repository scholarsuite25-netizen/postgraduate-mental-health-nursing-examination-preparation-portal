/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { 
  CheckCircle2, 
  XCircle, 
  AlertCircle, 
  Download, 
  Printer, 
  FileText, 
  ArrowLeft, 
  Award, 
  Clock, 
  ShieldAlert,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import { AssessmentReport } from '../types';

interface AssessmentResultProps {
  report: AssessmentReport;
  onBackToDashboard: () => void;
  onViewReports: () => void;
}

export const AssessmentResult: React.FC<AssessmentResultProps> = ({
  report,
  onBackToDashboard,
  onViewReports
}) => {
  const [expandedQuestions, setExpandedQuestions] = useState<Record<string, boolean>>({});

  const toggleExpand = (qId: string) => {
    setExpandedQuestions(prev => ({
      ...prev,
      [qId]: !prev[qId]
    }));
  };

  const handleDownloadHTMLReport = () => {
    const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>WAPCNM Assessment Report - ${report.id}</title>
  <style>
    body { font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; color: #1e293b; max-width: 900px; margin: 0 auto; padding: 32px; background: #f8fafc; }
    .card { background: #ffffff; border-radius: 12px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border: 1px solid #e2e8f0; }
    .header { text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 24px; }
    .badge { display: inline-block; padding: 6px 16px; border-radius: 9999px; font-weight: bold; font-size: 14px; }
    .pass { background: #dcfce7; color: #166534; }
    .fail { background: #ffe4e6; color: #9f1239; }
    .warning { background: #fef3c7; border: 1px solid #f59e0b; color: #92400e; padding: 16px; border-radius: 8px; margin-bottom: 24px; font-size: 14px; }
    .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
    .stat-box { background: #f1f5f9; padding: 12px; border-radius: 8px; text-align: center; }
    .stat-val { font-size: 20px; font-weight: bold; color: #0f172a; }
    .stat-label { font-size: 12px; color: #64748b; }
    .question-item { border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px; margin-bottom: 16px; background: #fff; }
    .option { padding: 8px 12px; margin: 4px 0; border-radius: 6px; font-size: 14px; }
    .correct-opt { background: #dcfce7; border: 1px solid #86efac; color: #166534; font-weight: 500; }
    .incorrect-opt { background: #ffe4e6; border: 1px solid #fca5a5; color: #9f1239; }
    .normal-opt { background: #f8fafc; border: 1px solid #e2e8f0; }
    .explanation { margin-top: 12px; padding: 12px; background: #f0fdf4; border-left: 4px solid #10b981; font-size: 13px; color: #065f46; }
    .disclaimer { font-size: 11px; color: #64748b; text-align: center; margin-top: 40px; border-top: 1px solid #e2e8f0; padding-top: 20px; }
    @media print { body { background: #fff; padding: 0; } .card { box-shadow: none; border: 1px solid #cbd5e1; } }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h2>Postgraduate Mental Health Nursing Examination Preparation Portal</h2>
      <p style="margin: 4px 0; color: #64748b; font-size: 14px;">Official Assessment Result Slip & Detailed Learning Report</p>
      <p style="font-size: 12px; color: #94a3b8;">Report ID: <strong>${report.id}</strong> | Generated: ${new Date(report.dateTimestamp).toLocaleString()}</p>
    </div>

    <div class="warning">
      <strong>IMPORTANT: REPORT PRESERVATION NOTICE</strong><br/>
      Your result and answer explanations are valuable learning records. Keep this file saved securely in your Documents folder or cloud storage. Local browser storage may be cleared or reset.
    </div>

    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <div>
        <h3 style="margin: 0; font-size: 18px;">Candidate: ${report.candidateName}</h3>
        <p style="margin: 4px 0 0 0; color: #64748b; font-size: 14px;">Assessment: ${report.assessmentTitle}</p>
      </div>
      <div>
        <span class="badge ${report.status === 'PASS' ? 'pass' : 'fail'}">
          ${report.percentage.toFixed(1)}% — ${report.status}
        </span>
      </div>
    </div>

    <div class="grid">
      <div class="stat-box">
        <div class="stat-val">${report.totalQuestions}</div>
        <div class="stat-label">Total Questions</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" style="color: #16a34a;">${report.correctCount}</div>
        <div class="stat-label">Correct Answers</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" style="color: #dc2626;">${report.incorrectCount + report.unansweredCount}</div>
        <div class="stat-label">Incorrect / Unanswered</div>
      </div>
      <div class="stat-box">
        <div class="stat-val">70.0%</div>
        <div class="stat-label">Required Pass Mark</div>
      </div>
    </div>

    <h3 style="border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; margin-top: 32px;">Detailed Question-by-Question Review</h3>
    
    ${report.questionsSnapshot.map((q, idx) => {
      const candidateAns = report.candidateAnswers[q.id];
      const isCorrect = candidateAns === q.correctAnswer;
      const isUnanswered = !candidateAns;

      return `
        <div class="question-item">
          <p style="margin: 0 0 8px 0; font-size: 12px; font-weight: bold; color: #64748b;">
            Question ${idx + 1} • Module: ${q.module} • Topic: ${q.topic}
          </p>
          <p style="margin: 0 0 12px 0; font-weight: bold; font-size: 15px;">${q.questionText}</p>
          
          <div style="margin-bottom: 12px;">
            ${q.options.map(opt => {
              const isOptCorrect = opt.id === q.correctAnswer;
              const isOptCandidate = opt.id === candidateAns;
              let optClass = "normal-opt";
              if (isOptCorrect) optClass = "correct-opt";
              else if (isOptCandidate && !isOptCorrect) optClass = "incorrect-opt";

              return `
                <div class="option ${optClass}">
                  <strong>${opt.id}.</strong> ${opt.text}
                  ${isOptCorrect ? ' <strong>(Correct Answer)</strong>' : ''}
                  ${isOptCandidate && !isOptCorrect ? ' <strong>(Your Answer)</strong>' : ''}
                </div>
              `;
            }).join('')}
          </div>

          <p style="margin: 4px 0; font-size: 13px;">
            <strong>Candidate Status:</strong> 
            <span style="color: ${isCorrect ? '#16a34a' : '#dc2626'}; font-weight: bold;">
              ${isUnanswered ? 'Unanswered (Counted as Incorrect)' : isCorrect ? 'Correct' : 'Incorrect'}
            </span>
          </p>

          <div class="explanation">
            <strong>Correct Answer (${q.correctAnswer}):</strong> ${q.options.find(o => o.id === q.correctAnswer)?.text}<br/><br/>
            <strong>Detailed Explanation:</strong> ${q.explanation}
            ${q.learningObjective ? `<br/><br/><strong>Learning Objective:</strong> ${q.learningObjective}` : ''}
            ${q.reference ? `<br/><strong>Reference:</strong> ${q.reference}` : ''}
          </div>
        </div>
      `;
    }).join('')}

    <div class="disclaimer">
      <p>Independent Educational Preparation Resource — Associated with WAPCNM Specialty Examination Preparation.</p>
      <p>This report is generated locally in the candidate browser and is not an official West African Postgraduate College of Nurses and Midwives result slip.</p>
    </div>
  </div>
</body>
</html>`;

    const blob = new Blob([htmlContent], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `WAPCNM_Report_${report.id}.html`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-12">
      {/* Top Action Header */}
      <div className="flex items-center justify-between bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs print:hidden">
        <button
          onClick={onBackToDashboard}
          className="flex items-center gap-2 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-emerald-600 cursor-pointer"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Dashboard</span>
        </button>
        <div className="flex items-center gap-2">
          <button
            onClick={handleDownloadHTMLReport}
            className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-md shadow-emerald-600/20 cursor-pointer"
          >
            <Download className="w-4 h-4" />
            <span>Download Complete Report</span>
          </button>
          <button
            onClick={handlePrint}
            className="bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 px-4 py-2 rounded-xl text-xs font-semibold flex items-center gap-1.5 cursor-pointer"
          >
            <Printer className="w-4 h-4" />
            <span>Print / Save as PDF</span>
          </button>
        </div>
      </div>

      {/* REPORT PRESERVATION WARNING BANNER */}
      <div className="bg-amber-50 dark:bg-amber-950/50 border-2 border-amber-300 dark:border-amber-700 p-5 rounded-2xl shadow-sm text-amber-900 dark:text-amber-200 space-y-2 print:border">
        <div className="flex items-center gap-2 font-bold text-sm">
          <ShieldAlert className="w-5 h-5 text-amber-600 dark:text-amber-400 shrink-0" />
          <span>IMPORTANT: DOWNLOAD AND SAVE YOUR REPORT NOW</span>
        </div>
        <p className="text-xs sm:text-sm leading-relaxed">
          Your result and answer explanations are valuable learning records. Download this report and save it in a safe location, such as your device's Documents folder or a personal cloud-storage account. Reports saved only in this browser may be lost if you clear browser data, reset your device, change browsers, or experience device failure.
        </p>
      </div>

      {/* Main Result Card */}
      <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-6 sm:p-8 shadow-xs space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-6">
          <div>
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
              Assessment Report ID: {report.id}
            </span>
            <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white mt-1">
              {report.assessmentTitle}
            </h2>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
              Candidate: <strong className="text-slate-700 dark:text-slate-300">{report.candidateName}</strong> • Completed on {new Date(report.dateTimestamp).toLocaleString()}
            </p>
          </div>

          <div className="text-left sm:text-right">
            <div className={`inline-flex items-center gap-2 px-4 py-2 rounded-xl text-base font-bold ${
              report.status === 'PASS' 
                ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-200 border border-emerald-300' 
                : 'bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-200 border border-rose-300'
            }`}>
              {report.status === 'PASS' ? <CheckCircle2 className="w-5 h-5 text-emerald-600" /> : <XCircle className="w-5 h-5 text-rose-600" />}
              <span>{report.percentage.toFixed(1)}% — {report.status}</span>
            </div>
            <p className="text-[11px] text-slate-500 mt-1">Required Pass Mark: 70.0% (Fixed)</p>
          </div>
        </div>

        {/* Statistics Summary Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          <div className="bg-slate-50 dark:bg-slate-800/60 p-4 rounded-xl border border-slate-100 dark:border-slate-700/60 text-center">
            <div className="text-2xl font-bold text-slate-900 dark:text-white">{report.totalQuestions}</div>
            <div className="text-xs text-slate-500 mt-0.5">Total Questions</div>
          </div>
          <div className="bg-emerald-50/60 dark:bg-emerald-950/40 p-4 rounded-xl border border-emerald-100 dark:border-emerald-900/50 text-center">
            <div className="text-2xl font-bold text-emerald-600 dark:text-emerald-400">{report.correctCount}</div>
            <div className="text-xs text-emerald-700 dark:text-emerald-300 mt-0.5">Correct Answers</div>
          </div>
          <div className="bg-rose-50/60 dark:bg-rose-950/40 p-4 rounded-xl border border-rose-100 dark:border-rose-900/50 text-center">
            <div className="text-2xl font-bold text-rose-600 dark:text-rose-400">
              {report.incorrectCount + report.unansweredCount}
            </div>
            <div className="text-xs text-rose-700 dark:text-rose-300 mt-0.5">Incorrect / Unanswered</div>
          </div>
          <div className="bg-indigo-50/60 dark:bg-indigo-950/40 p-4 rounded-xl border border-indigo-100 dark:border-indigo-900/50 text-center">
            <div className="text-2xl font-bold text-indigo-600 dark:text-indigo-400">
              {Math.floor(report.timeTakenSeconds / 60)}m {report.timeTakenSeconds % 60}s
            </div>
            <div className="text-xs text-indigo-700 dark:text-indigo-300 mt-0.5">Time Taken</div>
          </div>
        </div>
      </div>

      {/* Detailed Question Review List */}
      <div className="space-y-4">
        <h3 className="text-lg font-bold text-slate-900 dark:text-white px-1">
          Detailed Question-by-Question Review & Explanations
        </h3>

        {report.questionsSnapshot.map((q, idx) => {
          const candidateAns = report.candidateAnswers[q.id];
          const isCorrect = candidateAns === q.correctAnswer;
          const isUnanswered = !candidateAns;
          const isExpanded = expandedQuestions[q.id] !== false; // expanded by default

          return (
            <div 
              key={q.id}
              className={`bg-white dark:bg-slate-900 rounded-2xl border p-6 shadow-xs space-y-4 ${
                isCorrect 
                  ? 'border-emerald-200 dark:border-emerald-900/60' 
                  : 'border-rose-200 dark:border-rose-900/60'
              }`}
            >
              <div className="flex items-start justify-between gap-4">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-xs font-bold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                      Q{idx + 1}
                    </span>
                    <span className="text-xs font-semibold text-slate-400">
                      {q.module} • {q.topic}
                    </span>
                  </div>
                  <h4 className="font-bold text-slate-900 dark:text-white text-base sm:text-lg">
                    {q.questionText}
                  </h4>
                </div>

                <div className="flex items-center gap-2 shrink-0">
                  <span className={`px-2.5 py-1 rounded-full text-xs font-bold flex items-center gap-1 ${
                    isCorrect 
                      ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/60 dark:text-emerald-300' 
                      : 'bg-rose-100 text-rose-800 dark:bg-rose-900/60 dark:text-rose-300'
                  }`}>
                    {isCorrect ? <CheckCircle2 className="w-3.5 h-3.5" /> : <XCircle className="w-3.5 h-3.5" />}
                    <span>{isUnanswered ? 'Unanswered' : isCorrect ? 'Correct' : 'Incorrect'}</span>
                  </span>
                  <button
                    onClick={() => toggleExpand(q.id)}
                    className="p-1.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                  >
                    {isExpanded ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                  </button>
                </div>
              </div>

              {/* Options list */}
              {isExpanded && (
                <div className="space-y-2 pt-2">
                  {q.options.map((opt) => {
                    const isCorrectOpt = opt.id === q.correctAnswer;
                    const isCandidateOpt = opt.id === candidateAns;

                    let optStyle = "border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-slate-700 dark:text-slate-300";
                    if (isCorrectOpt) {
                      optStyle = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/50 text-emerald-900 dark:text-emerald-200 font-semibold ring-1 ring-emerald-500";
                    } else if (isCandidateOpt && !isCorrectOpt) {
                      optStyle = "border-rose-500 bg-rose-50 dark:bg-rose-950/50 text-rose-900 dark:text-rose-200 font-semibold ring-1 ring-rose-500";
                    }

                    return (
                      <div
                        key={opt.id}
                        className={`p-3.5 rounded-xl border text-xs sm:text-sm flex items-center justify-between ${optStyle}`}
                      >
                        <div className="flex items-center gap-3">
                          <span className="w-6 h-6 rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-center font-bold text-xs">
                            {opt.id}
                          </span>
                          <span>{opt.text}</span>
                        </div>
                        <div className="flex items-center gap-2 shrink-0 text-xs">
                          {isCorrectOpt && (
                            <span className="text-emerald-600 dark:text-emerald-400 font-bold bg-emerald-100/80 dark:bg-emerald-900/60 px-2 py-0.5 rounded">
                              Correct Answer
                            </span>
                          )}
                          {isCandidateOpt && !isCorrectOpt && (
                            <span className="text-rose-600 dark:text-rose-400 font-bold bg-rose-100/80 dark:bg-rose-900/60 px-2 py-0.5 rounded">
                              Your Answer
                            </span>
                          )}
                        </div>
                      </div>
                    );
                  })}

                  {/* Explanation box */}
                  <div className="mt-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2 text-xs sm:text-sm text-slate-700 dark:text-slate-300">
                    <div className="font-bold text-slate-900 dark:text-white flex items-center gap-1.5">
                      <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                      <span>Detailed Explanation</span>
                    </div>
                    <p className="leading-relaxed">{q.explanation}</p>
                    {q.learningObjective && (
                      <p className="text-slate-500 dark:text-slate-400 pt-1">
                        <strong>Learning Objective:</strong> {q.learningObjective}
                      </p>
                    )}
                    {q.reference && (
                      <p className="text-[11px] text-slate-400">
                        <strong>Reference:</strong> {q.reference}
                      </p>
                    )}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
