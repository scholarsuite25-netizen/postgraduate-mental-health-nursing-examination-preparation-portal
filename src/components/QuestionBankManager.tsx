/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { Settings, Download, Upload, CheckCircle2, XCircle, AlertTriangle, FileJson } from 'lucide-react';
import { Question } from '../types';
import { StorageService } from '../services/storageService';
import { PROVISIONAL_MODULES } from '../data/questionBank';

interface QuestionBankManagerProps {
  questions: Question[];
  onQuestionsUpdated: () => void;
}

export const QuestionBankManager: React.FC<QuestionBankManagerProps> = ({
  questions,
  onQuestionsUpdated
}) => {
  const [jsonInput, setJsonInput] = useState('');
  const [importSummary, setImportSummary] = useState<{
    imported: number;
    rejected: number;
    errors: string[];
  } | null>(null);

  const handleExportJSON = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(questions, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `WAPCNM_QuestionBank_${Date.now()}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
  };

  const handleValidateAndImport = async () => {
    setImportSummary(null);
    let parsed: any[];
    try {
      parsed = JSON.parse(jsonInput);
      if (!Array.isArray(parsed)) {
        throw new Error('Imported JSON must be an array of question objects.');
      }
    } catch (err: any) {
      setImportSummary({
        imported: 0,
        rejected: 0,
        errors: [`Invalid JSON format: ${err.message}`]
      });
      return;
    }

    let importedCount = 0;
    let rejectedCount = 0;
    const errors: string[] = [];
    const existingIds = new Set(questions.map(q => q.id));
    const validQuestionsToSave: Question[] = [];

    parsed.forEach((item, index) => {
      const itemNum = index + 1;
      // Validation checks
      if (!item.id || typeof item.id !== 'string') {
        errors.push(`Item #${itemNum}: Missing or invalid 'id'.`);
        rejectedCount++;
        return;
      }
      if (existingIds.has(item.id)) {
        errors.push(`Item #${itemNum} (${item.id}): Duplicate question ID.`);
        rejectedCount++;
        return;
      }
      if (!item.questionText || typeof item.questionText !== 'string' || item.questionText.trim() === '') {
        errors.push(`Item #${itemNum} (${item.id}): Missing or empty questionText.`);
        rejectedCount++;
        return;
      }
      if (!Array.isArray(item.options) || item.options.length !== 4) {
        errors.push(`Item #${itemNum} (${item.id}): Must have exactly four options.`);
        rejectedCount++;
        return;
      }
      const optIds = item.options.map((o: any) => o.id);
      const expectedOptIds = ['A', 'B', 'C', 'D'];
      const hasValidOpts = expectedOptIds.every(id => optIds.includes(id));
      if (!hasValidOpts) {
        errors.push(`Item #${itemNum} (${item.id}): Options must be precisely labelled A, B, C, and D.`);
        rejectedCount++;
        return;
      }
      if (!['A', 'B', 'C', 'D'].includes(item.correctAnswer)) {
        errors.push(`Item #${itemNum} (${item.id}): correctAnswer must be 'A', 'B', 'C', or 'D'.`);
        rejectedCount++;
        return;
      }
      if (!item.module || typeof item.module !== 'string') {
        errors.push(`Item #${itemNum} (${item.id}): Missing or invalid module assignment.`);
        rejectedCount++;
        return;
      }

      validQuestionsToSave.push({
        id: item.id,
        module: item.module,
        topic: item.topic || 'General Specialty Practice',
        difficulty: item.difficulty || 'Intermediate',
        questionText: item.questionText,
        options: item.options,
        correctAnswer: item.correctAnswer,
        explanation: item.explanation || 'Detailed clinical rationale provided.',
        learningObjective: item.learningObjective || 'Master core postgraduate nursing competencies.',
        reference: item.reference,
        contentReviewStatus: 'Pending Review'
      });
      existingIds.add(item.id);
      importedCount++;
    });

    if (validQuestionsToSave.length > 0) {
      for (const q of validQuestionsToSave) {
        await StorageService.addCustomQuestion(q);
      }
      onQuestionsUpdated();
    }

    setImportSummary({
      imported: importedCount,
      rejected: rejectedCount,
      errors
    });
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center gap-2 text-emerald-600 dark:text-emerald-400 font-semibold text-xs mb-1">
            <Settings className="w-4 h-4" />
            <span>Admin & Bank Management</span>
          </div>
          <h2 className="text-xl sm:text-2xl font-bold text-slate-900 dark:text-white">
            Question Bank Management ({questions.length} Questions)
          </h2>
          <p className="text-slate-500 dark:text-slate-400 text-xs sm:text-sm mt-1">
            Export question bank JSON backups or import new validated batches of MCQs.
          </p>
        </div>

        <button
          onClick={handleExportJSON}
          className="bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold flex items-center gap-2 shadow-md cursor-pointer shrink-0"
        >
          <Download className="w-4 h-4" />
          <span>Export Question Bank JSON</span>
        </button>
      </div>

      {/* Import Card */}
      <div className="bg-white dark:bg-slate-900 p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-4">
        <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
          <Upload className="w-5 h-5 text-emerald-600" />
          <span>Import Question Batch (JSON)</span>
        </h3>
        <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed">
          Paste a JSON array of validated questions. Each question requires a unique ID, non-empty questionText, exactly 4 options (A, B, C, D), correct answer identifier, and module assignment.
        </p>

        <textarea
          rows={8}
          value={jsonInput}
          onChange={(e) => setJsonInput(e.target.value)}
          placeholder={`[\n  {\n    "id": "MHN-Q101",\n    "module": "1. Foundations of Mental Health Nursing",\n    "topic": "Therapeutic Alliance",\n    "difficulty": "Intermediate",\n    "questionText": "...",\n    "options": [\n      { "id": "A", "text": "..." },\n      { "id": "B", "text": "..." },\n      { "id": "C", "text": "..." },\n      { "id": "D", "text": "..." }\n    ],\n    "correctAnswer": "A",\n    "explanation": "..."\n  }\n]`}
          className="w-full font-mono text-xs p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:outline-hidden focus:ring-2 focus:ring-emerald-500"
        />

        <div className="flex justify-end">
          <button
            onClick={handleValidateAndImport}
            className="bg-slate-900 dark:bg-slate-800 hover:bg-emerald-600 text-white font-semibold px-6 py-2.5 rounded-xl text-xs transition-colors cursor-pointer"
          >
            Validate & Import Batch
          </button>
        </div>

        {/* Import Summary Result */}
        {importSummary && (
          <div className="mt-6 p-5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3">
            <h4 className="font-bold text-slate-900 dark:text-white text-sm">Import Summary Results</h4>
            <div className="grid grid-cols-2 gap-4">
              <div className="p-3 rounded-lg bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 text-emerald-800 dark:text-emerald-300 text-xs font-semibold">
                Successfully Imported: {importSummary.imported}
              </div>
              <div className="p-3 rounded-lg bg-rose-50 dark:bg-rose-950/40 border border-rose-200 text-rose-800 dark:text-rose-300 text-xs font-semibold">
                Rejected / Errors: {importSummary.rejected}
              </div>
            </div>

            {importSummary.errors.length > 0 && (
              <div className="space-y-1 pt-2">
                <p className="text-xs font-bold text-rose-600">Validation Errors:</p>
                <ul className="list-disc pl-4 text-xs text-rose-600 dark:text-rose-400 space-y-1">
                  {importSummary.errors.map((err, i) => (
                    <li key={i}>{err}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};
