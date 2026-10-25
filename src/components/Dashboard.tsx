/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { 
  BookOpen, 
  Award, 
  CheckCircle2, 
  XCircle, 
  Bookmark, 
  Play, 
  Clock, 
  TrendingUp, 
  ShieldCheck, 
  FileText, 
  AlertTriangle,
  Sparkles,
  ArrowRight,
  Search,
  HelpCircle,
  X
} from 'lucide-react';
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer, 
  ReferenceLine 
} from 'recharts';
import { AssessmentReport, Question, IncorrectRecord } from '../types';
import { CAOSCEReport } from '../types/clinicalExams';

interface DashboardProps {
  candidateName: string;
  questions: Question[];
  reports: AssessmentReport[];
  bookmarks: string[];
  incorrectQueue: IncorrectRecord[];
  caosceReports?: CAOSCEReport[];
  onStartPractice: (module?: string) => void;
  onStartLearning: (module?: string) => void;
  onStartMock: () => void;
  onNavigate: (tab: string) => void;
  onOpenReport: (reportId: string) => void;
  onStartTargetedPractice: (subset: Question[], title: string) => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  candidateName,
  questions,
  reports,
  bookmarks,
  incorrectQueue,
  caosceReports = [],
  onStartPractice,
  onStartLearning,
  onStartMock,
  onNavigate,
  onOpenReport,
  onStartTargetedPractice
}) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedMatch, setSelectedMatch] = useState<Question | null>(null);
  const [previewSelectedOption, setPreviewSelectedOption] = useState<'A' | 'B' | 'C' | 'D' | null>(null);

  const totalQuestions = questions.length;
  const completedAssessments = reports.length;
  
  // Calculate best and latest score
  const latestReport = reports.length > 0 ? reports[0] : null;
  const bestScore = reports.length > 0 
    ? Math.max(...reports.map(r => r.percentage))
    : null;

  const totalAttemptedQuestions = reports.reduce((acc, r) => acc + r.answeredCount, 0);

  // Prepare chart data (chronological order)
  const chartData = reports
    .slice()
    .reverse()
    .map((r, index) => ({
      attempt: `Attempt ${index + 1}`,
      date: new Date(r.dateTimestamp).toLocaleDateString(),
      score: Number(r.percentage.toFixed(1)),
      status: r.status,
      title: r.assessmentTitle
    }));

  // Global search filtering
  const trimmedSearch = searchQuery.trim().toLowerCase();
  const searchResults = trimmedSearch.length >= 2
    ? questions.filter(q => 
        q.questionText.toLowerCase().includes(trimmedSearch) ||
        q.topic.toLowerCase().includes(trimmedSearch) ||
        q.module.toLowerCase().includes(trimmedSearch)
      ).slice(0, 15) // limit to 15 results for performance
    : [];

  return (
    <div className="space-y-6">
      {/* Hero Welcome Banner */}
      <div className="bg-gradient-to-r from-slate-900 via-slate-800 to-emerald-950 text-white rounded-2xl p-6 sm:p-8 shadow-xl relative overflow-hidden">
        <div className="absolute right-0 top-0 bottom-0 w-1/3 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-emerald-500/20 via-transparent to-transparent pointer-events-none" />
        <div className="relative z-10 max-w-3xl space-y-4">
          <div className="inline-flex items-center gap-2 bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 px-3 py-1 rounded-full text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5" />
            <span>WAPCNM Postgraduate Specialty Exam Prep v1.0</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
            Welcome back, {candidateName}!
          </h2>
          <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
            Master the clinical competencies, psychopathology, psychiatric emergencies, and advanced nursing management required for your West African Postgraduate College of Nurses and Midwives specialty examinations.
          </p>

          {/* Global Search Bar */}
          <div className="relative pt-2">
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search 1,000+ questions, topics, or keywords (e.g., lithium, schizophrenia, delirium)..."
                className="w-full bg-slate-900/90 dark:bg-slate-950 border border-slate-700 focus:border-emerald-500 rounded-2xl pl-12 pr-4 py-3.5 text-sm text-white placeholder-slate-400 shadow-lg focus:outline-hidden"
              />
            </div>

            {/* Search Results Dropdown */}
            {searchResults.length > 0 && (
              <div className="absolute left-0 right-0 mt-2 bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl shadow-2xl z-50 max-h-96 overflow-y-auto divide-y divide-slate-100 dark:divide-slate-800 text-slate-900 dark:text-white">
                <div className="p-3 bg-slate-50 dark:bg-slate-800/80 text-xs font-semibold text-slate-500 flex items-center justify-between">
                  <span>Found {searchResults.length} matching questions</span>
                  <button 
                    onClick={() => onStartTargetedPractice(searchResults, `Search Results: "${searchQuery}"`)}
                    className="text-emerald-600 dark:text-emerald-400 hover:underline font-bold"
                  >
                    Practice These Results ({searchResults.length})
                  </button>
                </div>
                {searchResults.map((q) => (
                  <div 
                    key={q.id}
                    onClick={() => {
                      setSelectedMatch(q);
                      setPreviewSelectedOption(null);
                    }}
                    className="p-4 hover:bg-slate-50 dark:hover:bg-slate-800/50 cursor-pointer transition-colors space-y-1"
                  >
                    <div className="flex items-center justify-between text-[11px] text-slate-400">
                      <span className="font-bold text-emerald-600 dark:text-emerald-400">{q.module}</span>
                      <span>Topic: {q.topic}</span>
                    </div>
                    <p className="text-xs sm:text-sm font-semibold text-slate-900 dark:text-white line-clamp-2">
                      {q.questionText}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </div>

          <div className="flex flex-wrap gap-3 pt-2">
            <button
              onClick={() => onStartPractice()}
              className="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-5 py-2.5 rounded-xl text-sm flex items-center gap-2 shadow-lg shadow-emerald-600/30 transition-all cursor-pointer"
            >
              <Play className="w-4 h-4 fill-white" />
              <span>Start MCQ Practice</span>
            </button>
            <button
              onClick={onStartMock}
              className="bg-white/10 hover:bg-white/20 text-white border border-white/20 font-semibold px-5 py-2.5 rounded-xl text-sm flex items-center gap-2 transition-all cursor-pointer"
            >
              <Clock className="w-4 h-4" />
              <span>Launch Mock Examination (70% Pass Mark)</span>
            </button>
          </div>
        </div>
      </div>

      {/* NEW: Postgraduate Clinical Examination Suites Showcase */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-indigo-900 via-slate-900 to-purple-950 p-6 sm:p-7 text-white shadow-lg border border-indigo-500/30 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div className="space-y-2 max-w-2xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-amber-400/20 text-amber-300 border border-amber-400/30">
            <span>⚡</span> NEW: Autonomous CAOSCE & NGN Clinical Suites
          </div>
          <h2 className="text-xl sm:text-2xl font-black text-white tracking-tight">
            Postgraduate Clinical Examination Center
          </h2>
          <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
            Test hands-on psychomotor de-escalation, suicide risk stratification, NMS vs Serotonin emergencies, and mental health jurisprudence across 6 clock-synchronized stations with non-negotiable <strong>Red Flag patient safety criteria</strong>.
          </p>
          {caosceReports.length > 0 && (
            <div className="text-xs text-indigo-300 pt-1 flex items-center gap-2">
              <span>Last CAOSCE Result:</span>
              <strong className="text-white bg-white/10 px-2 py-0.5 rounded font-mono">
                {caosceReports[0].overallCompositePercentage.toFixed(1)}% ({caosceReports[0].overallStatus})
              </strong>
            </div>
          )}
        </div>

        <div className="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
          <button
            onClick={() => onNavigate('clinical-exams')}
            className="px-6 py-3 rounded-xl font-bold text-xs sm:text-sm bg-gradient-to-r from-amber-500 to-indigo-600 hover:from-amber-400 hover:to-indigo-500 text-white shadow-lg shadow-indigo-950/50 transition-all flex items-center justify-center gap-2 cursor-pointer"
          >
            <span>🎯</span> Enter Clinical Exam Suites →
          </button>
        </div>
      </div>

      {/* Selected Match Modal */}
      {selectedMatch && (
        <div className="fixed inset-0 z-50 bg-slate-950/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 rounded-2xl max-w-2xl w-full p-6 sm:p-8 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-6 max-h-[90vh] overflow-y-auto">
            <div className="flex items-start justify-between">
              <div>
                <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">
                  {selectedMatch.module}
                </span>
                <h3 className="text-base sm:text-lg font-bold text-slate-900 dark:text-white mt-2 leading-relaxed">
                  {selectedMatch.questionText}
                </h3>
              </div>
              <button 
                onClick={() => setSelectedMatch(null)}
                className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 font-bold p-1 text-lg"
              >
                ✕
              </button>
            </div>

            <div className="space-y-2">
              {selectedMatch.options.map(opt => (
                <div 
                  key={opt.id}
                  className={`p-3 rounded-xl border text-xs sm:text-sm flex items-center gap-3 ${
                    opt.id === selectedMatch.correctAnswer 
                      ? 'bg-emerald-50 dark:bg-emerald-950/50 border-emerald-500 text-emerald-900 dark:text-emerald-200 font-semibold' 
                      : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                  }`}
                >
                  <span className="w-6 h-6 rounded-lg bg-white dark:bg-slate-800 border flex items-center justify-center font-bold text-xs">
                    {opt.id}
                  </span>
                  <span>{opt.text}</span>
                  {opt.id === selectedMatch.correctAnswer && (
                    <span className="ml-auto text-xs font-bold text-emerald-600 dark:text-emerald-400">Correct Answer</span>
                  )}
                </div>
              ))}
            </div>

            <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 space-y-2 text-xs sm:text-sm">
              <strong className="text-slate-900 dark:text-white">Explanation:</strong>
              <p className="text-slate-600 dark:text-slate-300 leading-relaxed">{selectedMatch.explanation}</p>
            </div>

            <div className="flex items-center justify-end gap-3 pt-2">
              <button
                onClick={() => setSelectedMatch(null)}
                className="px-5 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-50 cursor-pointer"
              >
                Close
              </button>
              <button
                onClick={() => {
                  const m = selectedMatch;
                  setSelectedMatch(null);
                  onStartTargetedPractice([m], `Practice Question: ${m.id}`);
                }}
                className="px-5 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow-md cursor-pointer flex items-center gap-1.5"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Practice This Question</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Statistics Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Available Questions */}
        <div className="bg-white dark:bg-slate-900 p-5 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-500 dark:text-slate-400">Question Bank</p>
            <h3 className="text-2xl font-bold text-slate-900 dark:text-white mt-1">{totalQuestions}</h3>
            <p className="text-[11px] text-emerald-600 dark:text-emerald-400 mt-1 flex items-center gap-1 font-medium">
              <span>14 Specialized Modules</span>
            </p>
          </div>
          <div className="w-12 h-12 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center">
            <BookOpen className="w-6 h-6" />
          </div>
        </div>

        {/* Assessments Completed */}
        <div className="bg-white dark:bg-slate-900 p-5 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-500 dark:text-slate-400">Assessments Completed</p>
            <h3 className="text-2xl font-bold text-slate-900 dark:text-white mt-1">{completedAssessments}</h3>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">
              {totalAttemptedQuestions} total answers recorded
            </p>
          </div>
          <div className="w-12 h-12 rounded-xl bg-blue-50 dark:bg-blue-950/60 text-blue-600 dark:text-blue-400 flex items-center justify-center">
            <Award className="w-6 h-6" />
          </div>
        </div>

        {/* Latest Score / Best Score */}
        <div className="bg-white dark:bg-slate-900 p-5 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-500 dark:text-slate-400">Best / Latest Score</p>
            <div className="flex items-baseline gap-2 mt-1">
              <h3 className="text-2xl font-bold text-slate-900 dark:text-white">
                {bestScore !== null ? `${bestScore.toFixed(1)}%` : '—'}
              </h3>
              {latestReport && (
                <span className={`text-xs font-bold px-1.5 py-0.5 rounded ${
                  latestReport.status === 'PASS' 
                    ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300' 
                    : 'bg-rose-100 text-rose-800 dark:bg-rose-900/40 dark:text-rose-300'
                }`}>
                  {latestReport.status}
                </span>
              )}
            </div>
            <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-1">
              Pass mark threshold: 70.0%
            </p>
          </div>
          <div className="w-12 h-12 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 flex items-center justify-center">
            <TrendingUp className="w-6 h-6" />
          </div>
        </div>

        {/* Incorrect Queue & Bookmarks */}
        <div className="bg-white dark:bg-slate-900 p-5 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs flex items-center justify-between">
          <div>
            <p className="text-xs font-medium text-slate-500 dark:text-slate-400">Revision & Bookmarks</p>
            <div className="flex items-center gap-3 mt-1">
              <div>
                <span className="text-xl font-bold text-rose-600 dark:text-rose-400">{incorrectQueue.length}</span>
                <span className="text-[11px] text-slate-500 block">Incorrect</span>
              </div>
              <div className="h-6 w-px bg-slate-200 dark:bg-slate-700" />
              <div>
                <span className="text-xl font-bold text-amber-600 dark:text-amber-400">{bookmarks.length}</span>
                <span className="text-[11px] text-slate-500 block">Bookmarked</span>
              </div>
            </div>
          </div>
          <div className="w-12 h-12 rounded-xl bg-amber-50 dark:bg-amber-950/60 text-amber-600 dark:text-amber-400 flex items-center justify-center">
            <Bookmark className="w-6 h-6" />
          </div>
        </div>
      </div>

      {/* Performance Trend Line Chart Visualization */}
      <div className="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-xs space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-emerald-600" />
              <span>Assessment Performance Trend Over Time</span>
            </h3>
            <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
              Tracking your percentage scores against the fixed 70% pass threshold.
            </p>
          </div>
          {reports.length > 0 && (
            <span className="text-xs font-semibold px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300">
              {reports.length} Attempt{reports.length === 1 ? '' : 's'} Logged
            </span>
          )}
        </div>

        {reports.length === 0 ? (
          <div className="text-center py-10 px-4 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-dashed border-slate-200 dark:border-slate-700">
            <p className="text-xs text-slate-500 dark:text-slate-400">
              Complete practice sessions or mock examinations to visualize your score progression trend line.
            </p>
          </div>
        ) : (
          <div className="w-full h-72 pt-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={chartData} margin={{ top: 10, right: 20, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" opacity={0.6} />
                <XAxis dataKey="attempt" stroke="#64748b" fontSize={12} />
                <YAxis domain={[0, 100]} stroke="#64748b" fontSize={12} unit="%" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '8px', color: '#fff', fontSize: '12px' }}
                  formatter={(value: any) => [`${value}%`, 'Score']}
                  labelStyle={{ fontWeight: 'bold', color: '#38bdf8' }}
                />
                <ReferenceLine y={70} stroke="#ef4444" strokeDasharray="4 4" label={{ value: 'Pass Mark (70%)', fill: '#ef4444', fontSize: 11, position: 'top' }} />
                <Line 
                  type="monotone" 
                  dataKey="score" 
                  stroke="#059669" 
                  strokeWidth={3} 
                  dot={{ r: 5, fill: '#059669', strokeWidth: 2, stroke: '#fff' }} 
                  activeDot={{ r: 8, fill: '#047857' }} 
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Quick Action Shortcuts */}
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-white dark:bg-slate-900 p-6 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs">
            <h3 className="text-base font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-emerald-600" />
              <span>Core Examination Preparation Modes</span>
            </h3>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div 
                onClick={() => onStartPractice()}
                className="p-4 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 hover:border-emerald-500/50 hover:bg-emerald-50/20 transition-all cursor-pointer group"
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="w-9 h-9 rounded-lg bg-emerald-100 dark:bg-emerald-900/60 text-emerald-600 dark:text-emerald-300 flex items-center justify-center group-hover:scale-110 transition-transform">
                    <BookOpen className="w-5 h-5" />
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-emerald-600 transition-colors" />
                </div>
                <h4 className="font-semibold text-slate-900 dark:text-white text-sm">MCQ Practice Mode</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Test your knowledge across individual modules or the entire bank without immediate answer interruption.
                </p>
              </div>

              <div 
                onClick={() => onStartLearning()}
                className="p-4 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 hover:border-teal-500/50 hover:bg-teal-50/20 transition-all cursor-pointer group"
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="w-9 h-9 rounded-lg bg-teal-100 dark:bg-teal-900/60 text-teal-600 dark:text-teal-300 flex items-center justify-center group-hover:scale-110 transition-transform">
                    <Sparkles className="w-5 h-5" />
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-teal-600 transition-colors" />
                </div>
                <h4 className="font-semibold text-slate-900 dark:text-white text-sm">Learning Mode (Instant Explanations)</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Receive immediate correct answers and detailed explanatory rationales after each question attempt.
                </p>
              </div>

              <div 
                onClick={onStartMock}
                className="p-4 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 hover:border-indigo-500/50 hover:bg-indigo-50/20 transition-all cursor-pointer group"
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="w-9 h-9 rounded-lg bg-indigo-100 dark:bg-indigo-900/60 text-indigo-600 dark:text-indigo-300 flex items-center justify-center group-hover:scale-110 transition-transform">
                    <Clock className="w-5 h-5" />
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-indigo-600 transition-colors" />
                </div>
                <h4 className="font-semibold text-slate-900 dark:text-white text-sm">Timed Mock Examination</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Simulate high-stakes examination conditions with a strict countdown timer, auto-submit, and fixed 70% pass threshold.
                </p>
              </div>

              <div 
                onClick={() => onNavigate('modules')}
                className="p-4 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50 hover:border-amber-500/50 hover:bg-amber-50/20 transition-all cursor-pointer group"
              >
                <div className="flex items-center justify-between mb-2">
                  <div className="w-9 h-9 rounded-lg bg-amber-100 dark:bg-amber-900/60 text-amber-600 dark:text-amber-300 flex items-center justify-center group-hover:scale-110 transition-transform">
                    <BookOpen className="w-5 h-5" />
                  </div>
                  <ArrowRight className="w-4 h-4 text-slate-400 group-hover:text-amber-600 transition-colors" />
                </div>
                <h4 className="font-semibold text-slate-900 dark:text-white text-sm">Browse 14 Modules</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                  Explore specialized mental health nursing subject modules and targeted question distributions.
                </p>
              </div>
            </div>
          </div>
        </div>

        {/* Recent Activity / Recent Reports */}
        <div className="space-y-6">
          <div className="bg-white dark:bg-slate-900 p-6 rounded-xl border border-slate-200 dark:border-slate-800 shadow-xs">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-base font-bold text-slate-900 dark:text-white flex items-center gap-2">
                <FileText className="w-5 h-5 text-emerald-600" />
                <span>Recent Assessment Reports</span>
              </h3>
              {reports.length > 0 && (
                <button
                  onClick={() => onNavigate('reports')}
                  className="text-xs font-semibold text-emerald-600 dark:text-emerald-400 hover:underline"
                >
                  View All ({reports.length})
                </button>
              )}
            </div>

            {reports.length === 0 ? (
              <div className="text-center py-8 px-4 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-dashed border-slate-200 dark:border-slate-700">
                <AlertTriangle className="w-8 h-8 text-amber-500 mx-auto mb-2 opacity-80" />
                <h4 className="text-sm font-semibold text-slate-800 dark:text-slate-200">No Assessments Completed Yet</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400 mt-1 mb-4">
                  Complete your first MCQ practice or mock examination to generate persistent browser reports.
                </p>
                <button
                  onClick={onStartMock}
                  className="bg-emerald-600 hover:bg-emerald-500 text-white font-medium px-4 py-2 rounded-lg text-xs transition-colors"
                >
                  Start First Exam
                </button>
              </div>
            ) : (
              <div className="space-y-3">
                {reports.slice(0, 3).map((report) => (
                  <div
                    key={report.id}
                    onClick={() => onOpenReport(report.id)}
                    className="p-3.5 rounded-xl border border-slate-100 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 hover:border-emerald-500/50 transition-all cursor-pointer flex items-center justify-between"
                  >
                    <div>
                      <h4 className="text-xs font-bold text-slate-900 dark:text-white">
                        {report.assessmentTitle}
                      </h4>
                      <p className="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
                        {new Date(report.dateTimestamp).toLocaleDateString()} • {report.correctCount}/{report.totalQuestions} correct
                      </p>
                    </div>
                    <div className="text-right">
                      <span className={`inline-block px-2 py-0.5 rounded text-xs font-bold ${
                        report.status === 'PASS' 
                          ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900/40 dark:text-emerald-300' 
                          : 'bg-rose-100 text-rose-800 dark:bg-rose-900/40 dark:text-rose-300'
                      }`}>
                        {report.percentage.toFixed(1)}% {report.status}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Interactive Question Tutorial Support Modal for Search Previews */}
      {selectedMatch && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 rounded-2xl max-w-2xl w-full p-6 shadow-2xl max-h-[90vh] overflow-y-auto space-y-5 animate-fadeIn">
            <div className="flex items-start justify-between gap-4 border-b border-slate-100 dark:border-slate-800 pb-3">
              <div>
                <div className="flex items-center gap-2 text-xs font-semibold text-emerald-600 dark:text-emerald-400 mb-0.5">
                  <span>{selectedMatch.module}</span>
                  <span>•</span>
                  <span>{selectedMatch.topic}</span>
                </div>
                <h3 className="font-bold text-base sm:text-lg text-slate-900 dark:text-white">
                  {selectedMatch.questionText}
                </h3>
              </div>
              <button
                onClick={() => setSelectedMatch(null)}
                className="p-1 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Test Yourself Options */}
            <div className="space-y-2.5">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-500 block">
                Select an answer to test validation & tutorial support:
              </span>
              {selectedMatch.options.map((opt) => {
                const isSelected = previewSelectedOption === opt.id;
                const isCorrect = opt.id === selectedMatch.correctAnswer;
                const hasAnswered = previewSelectedOption !== null;

                let optStyle = "border-slate-200 dark:border-slate-800 hover:border-emerald-400 bg-white dark:bg-slate-800/40 text-slate-800 dark:text-slate-200";

                if (hasAnswered) {
                  if (isCorrect) {
                    optStyle = "border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500 font-medium";
                  } else if (isSelected && !isCorrect) {
                    optStyle = "border-rose-500 bg-rose-50 dark:bg-rose-950/40 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500 font-medium";
                  } else {
                    optStyle = "border-slate-200 dark:border-slate-800/60 bg-slate-50/50 dark:bg-slate-900/40 text-slate-400 opacity-60";
                  }
                }

                return (
                  <button
                    key={opt.id}
                    onClick={() => setPreviewSelectedOption(opt.id)}
                    className={`w-full text-left p-3.5 rounded-xl border text-xs sm:text-sm transition-all flex items-start gap-3 cursor-pointer ${optStyle}`}
                  >
                    <span className={`w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0 ${
                      hasAnswered && isCorrect
                        ? 'bg-emerald-600 text-white'
                        : hasAnswered && isSelected && !isCorrect
                        ? 'bg-rose-600 text-white'
                        : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300'
                    }`}>
                      {opt.id}
                    </span>
                    <span className="flex-1 leading-snug">{opt.text}</span>
                    {hasAnswered && isCorrect && (
                      <span className="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 shrink-0">
                        ✓ Correct Answer
                      </span>
                    )}
                    {hasAnswered && isSelected && !isCorrect && (
                      <span className="text-[10px] font-bold text-rose-600 dark:text-rose-400 shrink-0">
                        ✕ Selected Incorrectly
                      </span>
                    )}
                  </button>
                );
              })}
            </div>

            {/* Immediate Tutorial Support Box */}
            {previewSelectedOption !== null && (() => {
              const isCorrect = previewSelectedOption === selectedMatch.correctAnswer;
              const correctOpt = selectedMatch.options.find(o => o.id === selectedMatch.correctAnswer);
              const chosenOpt = selectedMatch.options.find(o => o.id === previewSelectedOption);

              return (
                <div className={`p-4 rounded-xl border text-xs sm:text-sm space-y-3 animate-fadeIn ${
                  !isCorrect
                    ? 'bg-rose-50/70 dark:bg-rose-950/40 border-rose-200 dark:border-rose-900/60'
                    : 'bg-emerald-50/70 dark:bg-emerald-950/40 border-emerald-200 dark:border-emerald-900/60'
                }`}>
                  <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-200/60 dark:border-slate-800/60">
                    <div className="flex items-center gap-2 font-bold">
                      {!isCorrect ? (
                        <span className="text-rose-700 dark:text-rose-300 flex items-center gap-1.5 font-bold">
                          <XCircle className="w-4 h-4 text-rose-600" />
                          Incorrect Choice — Tutorial Support Active
                        </span>
                      ) : (
                        <span className="text-emerald-700 dark:text-emerald-300 flex items-center gap-1.5 font-bold">
                          <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                          Correct Answer Validated! Well done.
                        </span>
                      )}
                    </div>
                    {!isCorrect && (
                      <button
                        onClick={() => setPreviewSelectedOption(null)}
                        className="text-[11px] font-bold px-2 py-1 rounded bg-rose-200/80 hover:bg-rose-300 dark:bg-rose-900/80 dark:hover:bg-rose-800 text-rose-900 dark:text-rose-100 transition-colors cursor-pointer"
                      >
                        Try Again
                      </button>
                    )}
                  </div>

                  {/* Direct Comparison */}
                  <div className="space-y-1 text-xs">
                    <div className="flex items-start gap-1.5 font-semibold text-emerald-800 dark:text-emerald-300">
                      <span className="font-bold shrink-0">✓ Validated Correct Answer:</span>
                      <span>
                        Option {selectedMatch.correctAnswer} — {correctOpt?.text}
                      </span>
                    </div>
                    {!isCorrect && chosenOpt && (
                      <div className="flex items-start gap-1.5 text-rose-700 dark:text-rose-400">
                        <span className="font-bold shrink-0">✕ Your Choice:</span>
                        <span>
                          Option {chosenOpt.id} — {chosenOpt.text}
                        </span>
                      </div>
                    )}
                  </div>

                  {/* Rationale */}
                  <div className="p-3.5 rounded-lg bg-white/90 dark:bg-slate-900/90 border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300 space-y-1">
                    <strong className="text-slate-900 dark:text-white block font-bold text-xs uppercase tracking-wide">
                      Clinical Tutorial Explanation:
                    </strong>
                    <p className="leading-relaxed text-xs">
                      {selectedMatch.explanation}
                    </p>
                  </div>
                </div>
              );
            })()}

            {/* Actions */}
            <div className="pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between">
              <button
                onClick={() => setSelectedMatch(null)}
                className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
              >
                Close Preview
              </button>
              <button
                onClick={() => {
                  const targetModule = selectedMatch.module;
                  setSelectedMatch(null);
                  onStartPractice(targetModule);
                }}
                className="px-5 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white shadow-md transition-colors flex items-center gap-1.5 cursor-pointer"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Practice All Questions in this Module</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
