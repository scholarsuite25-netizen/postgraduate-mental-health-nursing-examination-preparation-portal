/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React from 'react';
import { Phone, MessageCircle, ShieldCheck, BookOpen, Award, Heart, HelpCircle } from 'lucide-react';

interface FooterProps {
  onNavigate: (tab: string) => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigate }) => {
  return (
    <footer className="bg-slate-900 text-slate-300 pt-12 pb-8 border-t border-slate-800 mt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Col 1: About & Encouragement */}
          <div className="space-y-3">
            <h4 className="font-bold text-white text-base flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-emerald-400" />
              <span>WAPCNM Specialty Prep Portal</span>
            </h4>
            <p className="text-xs text-slate-400 leading-relaxed">
              Empowering postgraduate mental health nursing candidates across West Africa to excel in specialty board examinations through rigorous 1,000+ MCQ practice, immediate rationales, and timed mock simulations.
            </p>
            <div className="text-xs text-emerald-400 font-medium">
              ✨ Your success in the examination starts with disciplined daily practice!
            </div>
            <div className="pt-2 text-[11px] text-slate-400 border-t border-slate-800 leading-relaxed">
              <strong className="text-blue-400 font-semibold block mb-0.5">Statutory Council Scope Note:</strong>
              NMCN statutory examinations govern the 5 core post-basic specialisations (Medical-Surgical, Midwifery, Paediatric, Public Health, A&E/Critical Care). Mental Health Specialty Fellowship examinations are administered under WAPCNM.
            </div>
          </div>

          {/* Col 2: Quick Navigation */}
          <div className="space-y-3">
            <h4 className="font-bold text-white text-sm">Quick Portal Navigation</h4>
            <ul className="space-y-2 text-xs">
              <li className="pb-1">
                <button 
                  onClick={() => { onNavigate('specialties'); window.scrollTo(0,0); }} 
                  className="w-full text-left inline-flex items-center gap-2 px-3 py-2 rounded-xl bg-gradient-to-r from-blue-700 to-indigo-700 hover:from-blue-600 hover:to-indigo-600 text-white font-black text-xs shadow-md border border-blue-400/50 transition-all cursor-pointer"
                >
                  <ShieldCheck className="w-4 h-4 text-cyan-300 shrink-0" />
                  <span>NMCN Statutory Specialisations & Licensure Suite</span>
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('dashboard'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  WAPCNM Tutorial
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('clinical-exams'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  Clinical Examination Center (CAOSCE & NGN)
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('modules'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  Browse 14 Specialty Modules
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('reports'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  My Persistent Examination Reports
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('bookmarks'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  Bookmarks & Incorrect Review Queue
                </button>
              </li>
              <li>
                <button onClick={() => { onNavigate('help'); window.scrollTo(0,0); }} className="hover:text-emerald-400 transition-colors cursor-pointer">
                  Help & Privacy Documentation
                </button>
              </li>
            </ul>
          </div>

          {/* Col 3: Designer Contact */}
          <div className="space-y-3">
            <h4 className="font-bold text-white text-sm">Design & Engineering Support</h4>
            <p className="text-xs text-slate-400">
              Need custom academic portal solutions or technical support? Connect directly with our lead developer:
            </p>
            <div className="space-y-2 pt-1">
              <div className="text-xs font-semibold text-white">
                Designed by S. B. Omotoso
              </div>
              <div className="flex items-center gap-2 flex-wrap">
                <a
                  href="tel:+2348034710699"
                  className="inline-flex items-center gap-1.5 bg-emerald-600 hover:bg-emerald-500 text-white px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors shadow-xs"
                >
                  <Phone className="w-3.5 h-3.5" />
                  <span>Call: +234 803 471 0699</span>
                </a>
                <a
                  href="https://wa.me/2348034710699"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 bg-teal-600 hover:bg-teal-500 text-white px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors shadow-xs"
                >
                  <MessageCircle className="w-3.5 h-3.5" />
                  <span>WhatsApp Chat</span>
                </a>
              </div>
            </div>
          </div>
        </div>

        <div className="pt-8 border-t border-slate-800 text-center text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p>© {new Date().getFullYear()} WAPCNM Postgraduate Mental Health Nursing Preparation Portal. Independent Educational Resource.</p>
          <p className="text-slate-400">
            Designed with <Heart className="w-3 h-3 inline text-rose-500 fill-rose-500 mx-0.5" /> by <strong className="text-white">S. B. Omotoso</strong>
          </p>
        </div>
      </div>
    </footer>
  );
};
