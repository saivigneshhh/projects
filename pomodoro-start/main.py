from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    mylabel.config(text="TIMER")
    tick_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN
    short_break=SHORT_BREAK_MIN
    long_break=LONG_BREAK_MIN


    if reps%8==0:
        count_down(long_break)
        mylabel.config(fg=RED,text="LONG BREAK")
    elif reps%2==0:
        count_down(short_break)
        mylabel.config(fg="black", text="BREAK")
    else:
        count_down(work_sec)
        mylabel.config(fg="blue", text="TIMER")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec< 10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔"
        tick_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



mylabel=Label(text="TIMER",font=(FONT_NAME,45,"bold"),bg=YELLOW)
mylabel.grid(row=1,column=2)


canvas= Canvas(width=200, height=223)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(103,111,image=tomato)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.config(bg=YELLOW)
canvas.grid(row=2,column=2)

button1=Button(text="start",font=("ariel",10),command=start_timer)
button1.grid(row=3,column=1)

button2=Button(text="reset",font=("ariel",10),command=reset_timer)
button2.grid(row=3,column=3)

tick_mark=Label(bg=YELLOW,fg=GREEN)
tick_mark.grid(column=2,row=4)

window.mainloop()