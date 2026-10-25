/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { 
  BookOpen, 
  LayoutDashboard, 
  FileText, 
  Bookmark, 
  Settings, 
  HelpCircle, 
  Brain, 
  User, 
  Check, 
  Edit2, 
  Menu, 
  X,
  Phone,
  MessageCircle,
  Activity,
  Volume2,
  VolumeX,
  ShieldCheck
} from 'lucide-react';
import { StorageService } from '../services/storageService';
import { AudioChimes } from '../utils/audioChimes';

interface NavbarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  candidateName: string;
  setCandidateName: (name: string) => void;
  questionCount: number;
  reportCount: number;
  caosceCount?: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  candidateName,
  setCandidateName,
  questionCount,
  reportCount,
  caosceCount = 0
}) => {
  const [isEditingName, setIsEditingName] = useState(false);
  const [tempName, setTempName] = useState(candidateName);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isMuted, setIsMuted] = useState(AudioChimes.getMuteState());

  const handleToggleMute = () => {
    const nextMuted = AudioChimes.toggleMute();
    setIsMuted(nextMuted);
  };

  const handleSaveName = async (e: React.FormEvent) => {
    e.preventDefault();
    if (tempName.trim()) {
      await StorageService.setCandidateName(tempName.trim());
      setCandidateName(tempName.trim());
      setIsEditingName(false);
    }
  };

  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
    { id: 'clinical-exams', label: 'Clinical Exams', icon: Activity, badge: 'CAOSCE & NGN' },
    { id: 'modules', label: 'Modules & Practice', icon: BookOpen },
    { id: 'reports', label: 'My Reports', icon: FileText, badge: reportCount > 0 ? reportCount : undefined },
    { id: 'bookmarks', label: 'Bookmarks & Review', icon: Bookmark },
    { id: 'specialties', label: 'NMCN Specialisations', icon: ShieldCheck, isNMCN: true, badge: 'STATUTORY' },
    { id: 'help', label: 'Help & Privacy', icon: HelpCircle },
  ];

  return (
    <header className="bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800 sticky top-0 z-30 shadow-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Title */}
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => { setActiveTab('dashboard'); setMobileMenuOpen(false); }}>
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white shadow-md shadow-emerald-500/20">
              <Brain className="w-6 h-6" />
            </div>
            <div>
              <h1 className="font-bold text-slate-900 dark:text-white text-sm sm:text-lg leading-tight tracking-tight">
                WAPCNM Mental Health Nursing
              </h1>
              <p className="text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                Postgraduate Specialty Examination Portal v1.0
              </p>
            </div>
          </div>

          {/* Right Actions & Candidate Profile */}
          <div className="flex items-center gap-3">
            <div className="hidden md:flex items-center gap-3 bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 px-3 py-1.5 rounded-full">
              <div className="w-7 h-7 rounded-full bg-emerald-100 dark:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 flex items-center justify-center font-bold text-xs">
                <User className="w-3.5 h-3.5" />
              </div>
              {isEditingName ? (
                <form onSubmit={handleSaveName} className="flex items-center gap-1">
                  <input
                    type="text"
                    value={tempName}
                    onChange={(e) => setTempName(e.target.value)}
                    className="text-xs px-2 py-0.5 border border-emerald-500 rounded bg-white dark:bg-slate-900 text-slate-900 dark:text-white focus:outline-hidden"
                    autoFocus
                  />
                  <button type="submit" className="p-1 text-emerald-600 hover:text-emerald-700">
                    <Check className="w-3.5 h-3.5" />
                  </button>
                </form>
              ) : (
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold text-slate-700 dark:text-slate-200">
                    {candidateName}
                  </span>
                  <button 
                    onClick={() => { setTempName(candidateName); setIsEditingName(true); }}
                    className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors"
                    title="Edit candidate name"
                  >
                    <Edit2 className="w-3 h-3" />
                  </button>
                </div>
              )}
            </div>

            {/* Audio Chime Mute/Unmute Toggle */}
            <button
              onClick={handleToggleMute}
              className={`p-2 rounded-xl border transition-colors cursor-pointer ${
                isMuted
                  ? 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-400'
                  : 'bg-emerald-50 dark:bg-emerald-950/40 border-emerald-300 dark:border-emerald-800 text-emerald-600 dark:text-emerald-400'
              }`}
              title={isMuted ? 'CAOSCE Bells Muted - Click to Unmute' : 'CAOSCE Bells Active (750Hz/1000Hz) - Click to Mute'}
            >
              {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
            </button>

            {/* Hamburger Menu Toggle Button */}
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition-colors cursor-pointer"
              aria-label="Toggle Navigation Menu"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>
        </div>

        {/* Desktop Navigation Tabs */}
        <nav className="hidden lg:flex items-center space-x-1.5 pb-2 scrollbar-none">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            const isNMCN = item.id === 'specialties';

            let btnClasses = '';
            if (isNMCN) {
              btnClasses = isActive
                ? 'bg-blue-600 text-white shadow-md shadow-blue-500/30 ring-2 ring-blue-400 font-black uppercase tracking-wider border border-blue-400'
                : 'bg-blue-50 dark:bg-blue-950/80 text-blue-700 dark:text-blue-300 border-2 border-blue-500 dark:border-blue-400 hover:bg-blue-100 dark:hover:bg-blue-900 font-extrabold uppercase tracking-wider shadow-sm';
            } else {
              btnClasses = isActive
                ? 'bg-emerald-600 text-white shadow-xs shadow-emerald-600/20 font-semibold'
                : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white font-medium';
            }

            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs sm:text-sm whitespace-nowrap transition-all cursor-pointer ${btnClasses}`}
              >
                <Icon className={`w-4 h-4 ${
                  isNMCN 
                    ? isActive ? 'text-white' : 'text-blue-600 dark:text-blue-400'
                    : isActive ? 'text-white' : 'text-slate-500 dark:text-slate-400'
                }`} />
                <span>{item.label}</span>
                {item.badge !== undefined && (
                  <span className={`ml-1 px-1.5 py-0.5 rounded-full text-[10px] font-black tracking-wide ${
                    isNMCN
                      ? isActive ? 'bg-white text-blue-800' : 'bg-blue-600 text-white'
                      : isActive ? 'bg-emerald-700 text-white' : 'bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300'
                  }`}>
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Mobile / Hamburger Dropdown Menu Drawer */}
        {mobileMenuOpen && (
          <div className="lg:hidden py-4 border-t border-slate-200 dark:border-slate-800 space-y-3 animate-fadeIn">
            {/* Candidate Name Banner in Mobile Menu */}
            <div className="flex items-center justify-between p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
              <div className="flex items-center gap-2">
                <div className="w-7 h-7 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-xs">
                  <User className="w-3.5 h-3.5" />
                </div>
                <span className="text-xs font-semibold text-slate-700 dark:text-slate-200">
                  {candidateName}
                </span>
              </div>
              <button 
                onClick={() => { setTempName(candidateName); setIsEditingName(true); setMobileMenuOpen(false); }}
                className="text-xs font-medium text-emerald-600 hover:underline"
              >
                Edit Name
              </button>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = activeTab === item.id;
                const isNMCN = item.id === 'specialties';

                let mobileClasses = '';
                if (isNMCN) {
                  mobileClasses = isActive
                    ? 'bg-blue-600 text-white shadow-md font-extrabold border-2 border-blue-400 sm:col-span-2'
                    : 'bg-blue-50 dark:bg-blue-950/80 text-blue-800 dark:text-blue-200 border-2 border-blue-500 font-extrabold shadow-sm sm:col-span-2';
                } else {
                  mobileClasses = isActive
                    ? 'bg-emerald-600 text-white shadow-sm font-semibold'
                    : 'bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-700 font-medium';
                }

                return (
                  <button
                    key={item.id}
                    onClick={() => { setActiveTab(item.id); setMobileMenuOpen(false); }}
                    className={`flex items-center justify-between px-4 py-3 rounded-xl text-sm transition-all ${mobileClasses}`}
                  >
                    <div className="flex items-center gap-3">
                      <Icon className={`w-4 h-4 ${isNMCN && !isActive ? 'text-blue-600 dark:text-blue-400' : ''}`} />
                      <span className={isNMCN ? 'tracking-wide' : ''}>{item.label}</span>
                    </div>
                    {item.badge !== undefined && (
                      <span className={`px-2 py-0.5 rounded-full text-xs font-black ${
                        isNMCN 
                          ? isActive ? 'bg-white text-blue-800' : 'bg-blue-600 text-white'
                          : 'bg-emerald-700 text-white'
                      }`}>
                        {item.badge}
                      </span>
                    )}
                  </button>
                );
              })}
            </div>

            {/* Designer Info in Mobile Drawer */}
            <div className="pt-3 border-t border-slate-100 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-xs text-slate-500">
              <span>Designed by <strong className="text-slate-800 dark:text-slate-200">S. B. Omotoso</strong></span>
              <div className="flex items-center gap-2">
                <a
                  href="tel:+2348034710699"
                  className="inline-flex items-center gap-1 bg-emerald-50 text-emerald-700 px-2.5 py-1 rounded-lg border border-emerald-200 font-medium"
                >
                  <Phone className="w-3 h-3" />
                  <span>Call</span>
                </a>
                <a
                  href="https://wa.me/2348034710699"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 bg-teal-50 text-teal-700 px-2.5 py-1 rounded-lg border border-teal-200 font-medium"
                >
                  <MessageCircle className="w-3 h-3 text-teal-600" />
                  <span>WhatsApp</span>
                </a>
              </div>
            </div>
          </div>
        )}
      </div>
    </header>
  );
};
