# Author : Himanshu Gullaiya
# https://www.linkedin.com/in/himanshugullaiya/
# https://github.com/himanshugullaiya

from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.root = master
        self.frame = Frame(master, bg = 'black', height = 500, width = 800)
        self.frame.pack()
        self.texts = [StringVar(), StringVar(), StringVar()]
        [x.set('00') for x in self.texts]
        self.labels = [Label(self.frame), Label(self.frame),Label(self.frame)]
        [self.labels[x].config(font = ("Jersey M54", 80 ,"bold"), bg = '#232021',fg = 'white', padx= 15, pady = 15 ,textvariable = self.texts[x]) for x in range(len(self.texts))]
        [self.labels[x].grid(row = 0, column = x, padx = 20, pady = 20, sticky = N+S+E+W) for x in range(len(self.texts))]

        self.frame.columnconfigure([0, 1, 2], minsize=200)

        self.bt1 = Button(self.frame ,text="   Start   ",command=self.start,font=("Courier 12 bold"))
        self.bt2 = Button(self.frame, text="   Stop   ", command=self.stop, font=("Courier 12 bold"))
        self.bt3 = Button(self.frame, text="   Reset   ", command=self.reset, font=("Courier 12 bold"))
        self.bt4 = Button(self.frame, text="    Exit    ", command=self.exit, font=("Courier 12 bold"))

        self.bt1.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.bt2.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.bt3.grid(row = 1, column = 2, padx = 10, pady = 10)
        self.bt4.grid(row=2, columnspan = 3, column = 0, sticky = W + E)
        # self.bt1.focus_set()
        self.switch = 0
        self.total_time_prev = 0
        self.total_time_curr = 0
        self.pomodoro_count = 1

        master.bind('<Escape>',self.exit)
        # master.bind('<Return>', self.start)
        master.bind('<space>', self.start)
        master.bind('<Delete>', self.reset)

    def start(self, event = 0):
        self.bt1.config(bg = '#4BFFBD')
        self.bt2.config(bg = 'white')
        self.root.bind('<space>', self.stop)
        self.switch = 1
        self.timer()

    def timer(self, event = 0):
        if (self.switch == 1):
            h = int(self.texts[0].get())
            m = int(self.texts[1].get())
            s = int(self.texts[2].get())
            self.total_time_curr = h*60 + m
            diff = self.total_time_curr - self.total_time_prev

            if diff == 25:
                if self.pomodoro_count < 4:
                    messagebox.showwarning("Break Time","Boss 25 Minutes are Up! Relax for 5 Minutes")
                elif self.pomodoro_count == 4:
                    messagebox.showwarning("Break Time", "Boss 4 Pomodoros are Over! Relax for 15 Minutes")
                elif self.pomodoro_count == 5:
                    messagebox.showwarning("Break Time", "Great Going! Relax for 30 Minutes Now!")
                elif self.pomodoro_count == 6:
                    messagebox.showwarning("Break Time", "Fantastic Work! But relax for an hour or Two Now & we will Start from the Top.")
                    self.pomodoro_count = 1
                self.root.bind('<space>', self.stop)
                self.pomodoro_count += 1
                self.switch = 0
                self.total_time_prev = self.total_time_curr

            else:
                if (s < 59):
                    s += 1
                else:
                    s = 0
                    if (m < 59):
                        m += 1
                    else:
                        m = 0
                        h += 1

                if s < 10:
                    s = '0'+str(s)
                else:
                    s = str(s)
                if m < 10:
                    m = '0'+str(m)
                else:
                    m = str(m)
                if h < 10:
                    h = '0'+str(h)
                else:
                    h = str(h)

                self.texts[0].set(h)
                self.texts[1].set(m)
                self.texts[2].set(s)

            if self.switch == 1:
                self.frame.after(1000,self.timer)

    def stop(self, event = 0):
        self.switch = 0
        self.bt1.config(bg= 'white')
        self.bt2.config(bg= '#4BFFBD')
        self.root.bind('<space>', self.start)

    def reset(self, event = 0):
        self.switch = 0
        [x.set('00') for x in self.texts]
        self.bt1.config(bg = 'white')
        self.bt2.config(bg='white')
        self.root.bind('<space>', self.start)

    def exit(self, event = 0):
        self.frame.quit()


root = Tk()
App(root)
root.title("STOPWATCH")
root.mainloop()
root.deiconify()
root.destroy()