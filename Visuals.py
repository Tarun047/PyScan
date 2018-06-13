import tkinter
import sys
import json
from tkinter import messagebox
class Application(tkinter.Frame):
    def __init__(self,master = tkinter.Tk(),res = None):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.res = res
        self.initGUI()
        self.master.mainloop()

    def initGUI(self):
        self.QUIT = tkinter.Button(self,text = "Exit",command=self.quit)
        self.QUIT.pack({"side":"bottom"})
        self.Title = tkinter.Label(self,text="Detection Results")
        self.Title.pack()
        self.Labels = []
        texts = list(self.res.keys())
        values = list(self.res.values())
        self.scrollbar = tkinter.Scrollbar(self)
        self.scrollbar.pack(side="right", fill="both")
        self.ListBox= tkinter.Listbox(self,width = 800,height = 600,yscrollcommand = self.scrollbar.set)
        self.ListBox.insert("end","File Name:"+sys.argv[0])
        self.ListBox.insert("end","-"*600)
        for name,val in zip(texts,values):
            if not isinstance(val,dict):
                self.ListBox.insert("end",str(name)+":"+str(val))
            self.ListBox.insert("end","-"*600)
        engines = list(self.res['scans'].items())
        self.ListBox.insert("end","SCAN ENGINES AND RESULTS: ")
        self.ListBox.insert("end","-"*600)
        for scanner in engines:
            self.ListBox.insert("end", scanner[0] + ":")
            y = list(scanner[1].items())
            for param in y:
                self.ListBox.insert("end", param)
            self.ListBox.insert("end", "-" * 600)
        self.ListBox.pack(side="left",fill="both")

        if self.res is None:
            tkinter.messagebox.showwarning(self, "App Broken! Sending Diagnostic Data to SUPER_USER")


