from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timeit import default_timer as timer
import random
#main window
root = Tk()
root.geometry("500x500")
root.configure(bg="black")


#child window
window = Tk()
window.geometry("550x500")
window.withdraw()

hs_file = open('highscore.txt', 'r+')
x = 0


def game():
    global x
    if x == 0:
        root.withdraw()
        x =x+1
    window.deiconify()
    
def check_result():
    j = error = 0
    answer = entry.get("1.0", 'end-1c')
    end = timer()
    time_taken = end - Start

    if len(words[word]) >= len(answer):
        for i in answer:
            if i == words[word][j]:
                pass
            else:
                error += 1
            j += 1
    elif len(words[word]) <= len(answer):
        error = len(answer) - len(words[word])
        for i in words[word]:
            if i == answer[j]:
                pass
            else:
                error += 1
            j += 1
    
    #WPM=[(no of chars type/5)-errors]/time taken (in mins)
    wpm = len(answer) / 5
    wpm = wpm - error
    wpm = int(wpm / (time_taken / 60))

    hs_file.seek(0)
    line = int(hs_file.readline())

    if wpm > line:
        hs_file.seek(0)
        hs_file.write(str(wpm))
        result = "Amazing! Your new high score is: " + str(wpm) + "WPM"
        messagebox.showinfo("Score", result)
    else:
        result = "Your score is: " + str(wpm) + " WPM\n Better luck next time!"
        messagebox.showinfo("Score", result)

def finish():
    hs_file.close()
    window.destroy()
    root.destroy()
   
   
#randomly display list of sentence
words= ["Radha is going to wthe store.","Ram like to play with ball.","I would like to be there","Veena had two cup of coffee","I will give it to you","Life is a box of chocolates.","Joe wins every time.","Larry is kind of kind may be","I lost my little brothers ball.", "Tom is coming here", "Kids are not playing."]
word = random.randint(0, (len(words) - 1))

x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500)
x2.place(x=15, y=10)

x3 = Button(window, text="submit!", font="times 20", bg="#fc2828", command=check_result)
x3.place(x=220, y=350)

entry = Text(window)
entry.place(x=100, y=180, height=150, width=350)

b2 = Button(window, text="done", font="times 13", bg='#ffc003', width=12, command=finish)
b2.place(x=155, y=420)

b3 = Button(window, text="Another one!", font="times 13", bg='#ffc003', width=12, command=game)
b3.place(x=265, y=420)

Start = timer()
#window.mainloop()

x1 = Label(root, text="let's test your typing speed!", bg="black", fg="White", font="times 20")
x1.place(x=100, y=50)

#main window button
b1 = Button(root, text="Go!", width=12, bg='#fcba03', font="times 20", command=game)
b1.place(x=150, y=120)

hs_text = Label(root, text="High score!", width=12, bg='#03fcf8', font="times 35")
hs_text.place(x=90,y=40)

hs = int(hs_file.readline())
#pop up  window
hs_val = Label(root,text=str(hs)+"WPM",width=12,fg='#03fcf8',bg='Black',font="times 35")
hs_val.place(x=110,y=320)
root.mainloop()
