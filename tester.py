from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timeit import default_timer as timer
import random
#main window
root = Tk()
root.geometry("500x500")
root.configure(bg="black")
#root.title("Testing root")


#child window
window = Tk()
window.geometry("550x500")
#window.title("Testing window")

window.withdraw()

hs_file = open('highscore.txt', 'r+')

x = 0

def game():
    global x
    if x == 0:
        root.withdraw()
        x += 1
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

    string = f"{entered.get()}"
    today2=datetime.now()
    end=today2.strftime("%H:%M:%S")
    
    ##end = timeit.default_timer()
    FMT = "%H:%M:%S"
    s_time = datetime.strptime(end,FMT) - datetime.strptime(start , FMT)
    
    s_time=str(s_time)
    dif=[]
    s_time=s_time.split(":")
    for s in s_time:
        dif.append(int(s))
    time=dif[0]*3600+dif[1]*60+dif[2]

    try:
        speed = round(len(string.split()) * 60 / time, 2)
    except:
        speed=0

    
if string == word:
     Msg1 = "Time= " + str(time) + ' seconds'
Msg2 = " Accuracy= 100% "
Msg3 = " Speed= " + str(speed) + 'wpm'


accuracy = difflib.SequenceMatcher(None, word, string).ratio()
accuracy = str(round(accuracy * 100, 2))
Msg1 = "Time= " + str(time) + ' seconds'
Msg2 = " Accuracy= " + accuracy + '%'
Msg3 = " Speed= " + str(speed) + ' wpm'  # words per minute



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
#words = ["Larry is kind of kind may be", "Tom is coming here", "Kids are not playing."]
words = ["An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state."," Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission.", "Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. ","The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets.", "Two common terms used to describe a salesperson are 'Farmer' and 'Hunter'."," The reality is that most professional salespeople have a little of both."," A hunter is often associated with aggressive personalities who use aggressive sales technique.", "A late 20th century trend in typing, primarily used with devices with small keyboards (such as PDAs and Smartphones), is thumbing or thumb typing."," This can be accomplished using one or both thumbs.", "One study examining 30 subjects, of varying different styles and expertise, has found minimal difference in typing speed between touch typists and self-taught hybrid typists. According to the study, 'The number of fingers does not determine typing speed..."," People using self-taught typing strategies were found to be as fast as trained typists... instead of the number of fingers, there are other factors that predict typing speed.", "Closed captions were created for deaf or hard of hearing individuals to assist in comprehension. ","They can also be used as a tool by those learning to read, learning to speak a non-native language, or in an environment where the audio is difficult to hear or is intentionally muted.", "A freelancer or freelance worker, is a term commonly used for a person who is self-employed and is not necessarily committed to a particular employer long-term."," Freelance workers are sometimes represented by a company or a temporary agency that resells freelance labor to clients"," others work independently or use professional associations or websites to get work."]
word = random.randint(0, (len(words) - 1))

x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500)
x2.place(x=15, y=10)

x3 = Button(window, text="submit!", font="times 20", bg="#fc2828", command=check_result)
x3.place(x=220, y=350)

entry = Text(window)
entry.place(x=100, y=180, height=150, width=350)

b2 = Button(window, text="done", font="times 13", bg='#ffc003', width=12, command=finish)
b2.place(x=155, y=420)

b3 = Button(window, text="Another one?", font="times 13", bg='#ffc003', width=12, command=game)
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