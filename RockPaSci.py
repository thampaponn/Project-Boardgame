"""Rock Paper Scissors"""

from tkinter import *
import random

def game_inter():
    """game interface"""

    p1_all_re = {'wins':0, 'losses':0, 'ties':0} #แถบแสดงผลทั้งหมด

    def game_rule(p1_shoot, p2_shoot): #กติกา
        """rule of RPS"""
        if p1_shoot == p2_shoot:
            p1_all_re['ties'] += 1
            return "tied"
        elif (p1_shoot == "rock" and p2_shoot == "scissors") or (p1_shoot == "paper" and p2_shoot == "rock") or \
            (p1_shoot == "scissors" and p2_shoot == "paper"):
            p1_all_re['wins'] += 1
            return "P1 won"
        else:
            p1_all_re['losses'] += 1
            return "P1 lost"

    def on_click(e): #แสดงแถบผลการเล่นในรอบนั้นๆ
        p1_shoot = e.widget["text"]
        p2_shoot = random.choice(shoot)
        result = game_rule(p1_shoot, p2_shoot)
        tv_result.set(f'p1:{p1_shoot} - p2:{p2_shoot} >>> {result}')
        result_all.set(f'{p1_all_re["wins"]} wins, {p1_all_re["ties"]} ties, {p1_all_re["losses"]} losses')

    root = Tk()
    root.option_add("*Font", "consolas 20")
    shoot = ['rock', 'paper', 'scissors']
    p1_shoot = [PhotoImage(file=f'{img}.png') for img in shoot]
    f1 = Frame(root)
    f1.grid(row=0, column=0)
    f2 = Frame(root)
    f2.grid(row=1, column=0)

    tv_result = StringVar()
    result_all = StringVar()

    for i in range(len(p1_shoot)):
        w = Button(f1, image=p1_shoot[i], text=shoot[i], borderwidth=0)
        w.pack(side=LEFT, padx=10)
        w.bind('<Button-1>', on_click)
    Label(f2, textvariable=tv_result, width=40).pack()
    Label(f2, textvariable=result_all, width=40, bg="pink").pack()
    root.mainloop()

game_inter()
