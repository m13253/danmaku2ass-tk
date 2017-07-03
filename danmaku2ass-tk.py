#!/usr/bin/env python3

import sys

if sys.version_info < (3,):
    raise RuntimeError('at least Python 3.0 is required')

import gettext
import os
import tkinter
import tkinter.ttk
import danmaku2ass.danmaku2ass

gettext.install('danmaku2ass-qt', os.path.join(os.path.dirname(os.path.abspath(os.path.realpath(sys.argv[0] or 'locale'))), 'locale'))


class MainFrame(tkinter.ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack(anchor='center', expand=True, fill='both')
        self.onCreate()
        self.master.update()
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())

    def onCreate(self):
        self.left_panel = tkinter.ttk.Frame(self, style='White.TFrame', borderwidth=1, relief='solid')
        self.left_panel.grid(column=2, row=4)
        self.left_panel.tabs = []
        for i, text in enumerate([_('1. Configure'), _('2. Import Comments'), _('3. Export Subtitles'), _('4. Post-processing')]):
            new_label = tkinter.ttk.Label(self.left_panel, style='White.TLabel', text='\u3000', justify='left', pad=4)
            new_label.grid(column=1, row=i + 1, sticky=(tkinter.N, tkinter.W, tkinter.S, tkinter.E))
            new_label = tkinter.ttk.Label(self.left_panel, style='White.TLabel', text=text, justify='left', pad=4)
            self.left_panel.tabs.append(new_label)
            new_label.grid(column=2, row=i + 1, sticky=(tkinter.N, tkinter.W, tkinter.S, tkinter.E))
        self.left_panel.pack(side='left', padx=8, pady=8)
        self.right_panel = tkinter.ttk.Frame(self, style='White.TFrame', borderwidth=1, relief='solid')
        self.right_panel.pack(side='right', expand=True, fill='both', padx=8, pady=8)


if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.title('Danmaku2ASS')
    tkstyle = tkinter.ttk.Style()
    tkstyle.configure('White.TFrame', background='white')
    tkstyle.configure('White.TLabel', background='white')
    mainframe = MainFrame(master=tk)
    mainframe.mainloop()
