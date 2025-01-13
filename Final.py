import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from tkinter.messagebox import askyesno

def easy():

    tk.messagebox.showinfo("IMP!!", "THERE IS ONLY 1 LEVEL IN THIS MODE WITH ONE RIDDLE AND YOU WILL BE GIVEN 3mins TO SOLVE THE RIDDLE.")
    roote=tk.Tk()
    roote.geometry("900x500")
    roote.title('Main Page')
    message = "WELCOME TO THE EASY LEVEL, "+name.get().upper()
    label_1  = tk.Label(roote, text =message, width = 50, font = ("bold", 25)).pack()
    
    def left_ans():
        if ans.get() == "384":
            tk.messagebox.showinfo("Congrats!","You have unlocked key1!!")
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                roote.destroy()
            else:
                roote.destroy()
                easy()
        elif ans.get() == "BACK":
            left_submit
        elif ans.get() != "384":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(roote, text="Would you like to try again or continue with the game:").pack()
            Button(roote, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(roote, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def back_ans():
        if ans.get() == "53":
            tk.messagebox.showinfo("Congrats!","You have unlocked key2!!")
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                roote.destroy()
            else:
                roote.destroy()
                easy()
        elif ans.get() == "BACK":
            left_submit
        elif ans.get() != "53":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(roote, text="Would you like to try again or continue with the game:").pack()
            Button(roote, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(roote, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def right_ans():
        if ans.get() == "eircn":
            tk.messagebox.showinfo("Congrats!","You have unlocked key3!!")
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                roote.destroy()
            else:
                roote.destroy()
                easy()
        elif ans.get() == "BACK":
            left_submit
        elif ans.get() != "eircn":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(roote, text="Would you like to try again or continue with the game").pack()
            Button(roote, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(roote, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def left_submit():
        game_line_7 = Label(roote, text="Choose a direction to go (LEFT/RIGHT/BACKWARDS):").pack()
        descision2 = Entry(roote)
        descision2.pack()
        Button(roote, text="Submit",command=Choice).pack()

    def Choice():
        global ans
        if user_decision_1.get() == "LEFT":
            game_line_5 =Label(roote, text="You observe the clocks on the wall. there are three of different colors, stuck at different times. The first one is red and stuck at 1 o'clock. The second one is a yellow one stuck at 4 o'clock. The last one was green and stuck at 2 o'clock").pack()
            game_line_6=Label(roote,text="The safe has a three digit password. On the safe you find a post-it note with the following written: red X 3, green X 4, yellow X 1").pack()
            game_line_7=Label(roote,text="Enter the password! or type back to check something else:").pack()
            ans=Entry(roote)
            ans.pack()
            Button(roote, text="Submit", command=left_ans).pack()
        elif user_decision_1.get() == "BACKWARDS":
            game_line_5 = Label(roote, text="You observe the bouquets on the table. There are three types of flowers, peonies, sunflowers and roses,in different quantities\nthere are 5 roses, 8 sunflowers and 3 peonies.").pack()
            game_line_6=Label(roote,text="The safe has a two digit password. Above the keypad you find a drawing of a rose and then a peon").pack()
            game_line_7=Label(roote,text="Enter the password! or type back to check something else:").pack()
            ans = Entry(roote)
            ans.pack()
            Button(roote, text="Submit", command=back_ans).pack()
        elif user_decision_1.get() == "RIGHT":
            game_line_5 = Label(roote, text="There is an old map of the world on the wall. On taking a closer look, you find that some places are marked.\ngreenland marked 1, madagascar marked 3, jamaica marked 4, india marked 2, argentina marked 5").pack()
            game_line_6=Label(roote,text="There is a burner phone on the dresser. Its password locked, but there is a post-it note on it, which reads 1[3] 2[0] 3[9] 4[5] 5[4]").pack()
            game_line_7=Label(roote,text="Enter the password! or type back to check something else:").pack()
            ans = Entry(roote)
            ans.pack()
            Button(roote, text="Submit", command=right_ans).pack()
            
    def direction():
        game_line_1 = Label(roote, text="You enter a room and can see a lot of different things. Which direction do you want to move in --> LEFT/RIGHT/FORWARDS/BACKWARDS").pack()
        global user_decision_1
        user_decision_1 = Entry(roote)
        user_decision_1.pack()
        Button(roote, text="Submit", command=Choice).pack()
        ##TIMER
        tk.messagebox.showinfo("WARNING!!", "THE TIMER HAS STARTED!!")
        second=StringVar()
        second.set("00")
        temp=180
        while temp >-1:
            secs=60
            second.set("{0:2d}".format(secs))

            roote.update()
            time.sleep(1)

            if (temp == 30):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 30s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 10):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 10s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 0):
                tk.messagebox.showinfo("TIME'S UP!!", "YOU LOST THE GAME :(")
                roote.destroy()
            temp -= 1
    direction()
    roote.mainloop()

def medium():
    tk.messagebox.showinfo("IMP!!", "THERE ARE 2 LEVELS IN THIS MODE WITH ONE RIDDLE IN EACH LEVEL AND YOU WILL BE GIVEN 3mins TO SOLVE EACH RIDDLE.")
    rootm=tk.Tk()
    rootm.geometry("900x500")
    rootm.title('Main Page')
    message = "WELCOME TO THE MEDIUM LEVEL, "+name.get().upper()
    label_1  = tk.Label(rootm, text = message, width = 50, font = ("bold", 25)).pack() 

    def left_ans():
        if ans1.get() == "138":
            game_line_10=Label(rootm,text="The answer is correct!").pack()
            game_line_8=Label(rootm,text="The safe has a three-digit password. It has a post-it note on it, which reads:\n(10X(A+B+2XC))-((A+B)/10)").pack()
            game_line_9=Label(rootm,text="Enter the password:").pack()
            ans2=Entry(rootm)
            ans2.pack()
            def answer():
                if ans2.get()=="437":
                    tk.messagebox.showinfo("Congrats!","You have unlocked key1!!")
                    tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
                    answer = askyesno(title='confirmation',message='Do you want to play again?')
                    if answer==False:
                        rootm.destroy()
                    else:
                        rootm.destroy()
                        medium()
            Button(rootm, text="Submit",command=answer).pack()        
        elif ans1.get() == "BACK":
            left_submit
        elif ans1.get() != "138":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(rootm, text="Would you like to try again or continue with the game:").pack()
            Button(rootm, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(rootm, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def right_ans():
        if ans1.get() == "739157":
            game_line_10=Label(rootm,text="The answer is correct!").pack()
            game_line_9=Label(rootm,text="The safe has a eight-digit password. It has a post-it note on it, which reads:\nthe answer you find, only when there are no vowels in the alphabet..").pack()
            game_line_7=Label(rootm,text="Enter the password:").pack()
            ans2 = Entry(rootm)
            ans2.pack()
            def answer():
                if ans2.get()=="23441225":
                    tk.messagebox.showinfo("Congrats!","You have unlocked key2!!")
                    tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
                    answer = askyesno(title='confirmation',message='Do you want to play again?')
                    if answer==False:
                        rootm.destroy()
                    else:
                        rootm.destroy()
                        medium()

            Button(rootm, text="Submit", command=answer).pack()           
        elif ans1.get() == "BACK":
            left_submit
        elif ans1.get() != "739157":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(rootm, text="Would you like to try again or continue with the game").pack()
            Button(rootm, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(rootm, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def left_submit():
        game_line_7 = Label(rootm, text="Choose a direction to go (LEFT/RIGHT):").pack()
        descision2 = Entry(rootm)
        descision2.pack()
        Button(rootm, text="Submit",command=Choice).pack()

    def Choice():
        global ans1
        if user_decision_1.get() == "LEFT":
            game_line_5 =Label(rootm, text="On the wall,you find an unusual poster.\nIt looks like the solar system, but some planets are torn off.\nOnly Mercury, Earth and Neptune remain.").pack()
            game_line_6=Label(rootm,text="Its a chart of the periodic table, but there were some markings on it\nCa₂₀ was marked A, Ne₁₀ marked B, N₇ marked C").pack()
            game_line_6=Label(rootm,text="The safe has three dials on it, each having the numbers 1-9").pack()
            game_line_7=Label(rootm,text="Enter the password! or type back to check something else:").pack()
            ans1=Entry(rootm)
            ans1.pack()
            Button(rootm, text="Submit", command=left_ans).pack()
        elif user_decision_1.get() == "RIGHT":
            game_line_5 = Label(rootm, text="You open the smaller pouch of marbles.\nOn counting them, you find there are 7 pink, 5 blue, 9 yellow, 1 white, 3 black ones").pack()
            game_line_6=Label(rootm,text="The clue card reads: the bird really wanted to ride the bicycle\nIt didnt make any sense to you..").pack()
            game_line_8=Label(rootm,text="The locked box has a six-digit password. It also has a beautiful flower pattern painted onto it\npink, black, yellow, white, blue and pink flowers (in order)").pack()
            game_line_8=Label(rootm,text="Enter the password! or type back to check something else:").pack()
            ans1 = Entry(rootm)
            ans1.pack()
            Button(rootm, text="Submit", command=right_ans).pack()
            
    def direction():
        game_line_1 = Label(rootm, text="You enter a room and can see a lot of different things. Which direction do you want to move in --> LEFT/RIGHT").pack()
        global user_decision_1
        user_decision_1 = Entry(rootm)
        user_decision_1.pack()
        Button(rootm, text="Submit", command=Choice).pack()

    ##TIMER
        tk.messagebox.showinfo("WARNING!!", "THE TIMER HAS STARTED!!")
        second=StringVar()
        second.set("00")
        temp=180
        while temp >-1:
            secs=60
            second.set("{0:2d}".format(secs))

            rootm.update()
            time.sleep(1)

            if (temp == 30):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 30s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 10):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 10s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 0):
                tk.messagebox.showinfo("TIME'S UP!!", "YOU LOST THE GAME :(")
                rootm.destroy()
            temp -= 1
    direction()
    rootm.mainloop()

def hard():
    tk.messagebox.showinfo("IMP!!", "THERE ARE 3 LEVELS IN THIS MODE WITH ONE RIDDLE IN EACH LEVEL AND YOU WILL BE GIVEN 30s TO SOLVE EACH RIDDLE.")
    rooth=tk.Tk()
    rooth.geometry("900x500")
    rooth.title('Main Page')
    message = "WELCOME TO THE HARD LEVEL, "+name.get().upper()
    label_1  = tk.Label(rooth, text = message, width = 50, font = ("bold", 25)).pack() 
    def left_ans():
        if ans1.get() == "ITGGP":
            game_line_5 =Label(rooth, text="Its a card which reads: Peter is in the East of Tom and Tom is in the North of John. Mike is in the South of John then in which direction of Peter is Mike?").pack()
            game_line_6=Label(rooth,text="The safe has a two letter password. It has a post-it note on it, which reads:\nEnter the answer in this form: NE for North-East, TS for True South").pack()
            game_line_7=Label(rooth,text="Enter the password: ").pack()
            ans2=Entry(rooth)
            ans2.pack()
            def answer():
                if ans2.get()=="SW":
                    tk.messagebox.showinfo("Congrats!","You have unlocked key1!!")
            Button(rooth, text="Submit",command=answer).pack()        
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                rooth.destroy()
            else:
                rooth.destroy()
                hard()
        elif ans1.get() != "ITGGP":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(rooth, text="Would you like to try again or continue with the game:").pack()
            Button(rooth, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(rooth, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def right_ans():
        if ans1.get() == "DANGER":
            game_line_5 =Label(rooth, text="There is an incomplete number series on the card. It says,\n36, 34, 30, 28, 24, _ , 18...").pack()
            game_line_6=Label(rooth,text="The safe has a two-digit password").pack()
            game_line_7=Label(rooth,text="Enter the password: ")
            ans2=Entry(rooth)
            ans2.pack()
            def answer():
                if ans2.get()=="22":
                    tk.messagebox.showinfo("Congrats!","You have unlocked key1!!")
            Button(rooth, text="Submit",command=answer).pack()   
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                rooth.destroy()
            else:
                rooth.destroy()
                hard()     
        elif ans1.get() != "DANGER":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(rooth, text="Would you like to try again or continue with the game:").pack()
            Button(rooth, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(rooth, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 


    def back_ans():
        if ans1.get() == "56":
            tk.messagebox.showinfo("Congrats!","You have unlocked key1!!")
            tk.messagebox.showinfo("End of game!","Thank you for playing with us!!")
            answer = askyesno(title='confirmation',message='Do you want to play again?')
            if answer==False:
                rooth.destroy()
            else:
                rooth.destroy()
                hard()
        elif ans1.get() != "56":
            tk.messagebox.showinfo("OOPS!","Wrong answer!Try again!")
            game_line_7 = Label(rooth, text="Would you like to try again or continue with the game:").pack()
            Button(rooth, text = 'TRY AGAIN', width = 20, bg = "blue", fg = 'black', font = ("bold",12), command = left_submit).pack() 
            Button(rooth, text = 'CONTINUE', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = direction).pack() 

    def left_submit():
        game_line_7 = Label(rooth, text="Choose a direction to go (LEFT/RIGHT/BACKWARDS):").pack()
        descision2 = Entry(rooth)
        descision2.pack()
        Button(rooth, text="Submit",command=Choice).pack()

    def Choice():
        global ans1
        if user_decision_1.get() == "LEFT":
            game_line_5 =Label(rooth, text="There is a poster .The poster says: MADRAS:OCFTCU::GREEN:?").pack()
            game_line_6=Label(rooth,text="The safe has a 5 letters password").pack()
            game_line_7=Label(rooth,text="Enter the password:").pack()
            ans1=Entry(rooth)
            ans1.pack()
            Button(rooth, text="Submit", command=left_ans).pack()
        elif user_decision_1.get() == "RIGHT":
            game_line_5 =Label(rooth, text="On the wall, you find a poster. It reads,Does anyone know Anything about Non earth beings? Green bodied and Eerie eyed, Rambling in unknown speak.").pack()
            game_line_6=Label(rooth,text="the alphabetical safe has a 6 letter answer").pack()
            game_line_7=Label(rooth,text="Enter the password!(AS CAPITAL LETTERS):").pack()
            ans1 = Entry(rooth)
            ans1.pack()
            Button(rooth, text="Submit", command=right_ans).pack()    
        elif user_decision_1.get() == "BACKWARDS":
                game_line_5 =Label(rooth, text="Its a chart which reads:A=no. of days in a week B=no. of hours in a day").pack()
                game_line_6=Label(rooth,text="the safe has a two digit password. It has a post-it note on it, which reads:\n(10AXB)/(B+A-1)").pack()
                game_line_7=Label(rooth,text="Enter the password:").pack()
                ans2=Entry(rooth)
                ans2.pack()
                Button(rooth, text="Submit", command=back_ans).pack()

    def direction():
        game_line_1 = Label(rooth, text="You enter a room and can see a lot of different things. Which direction do you want to move in --> LEFT/RIGHT/BACKWARDS").pack()
        global user_decision_1
        user_decision_1 = Entry(rooth)
        user_decision_1.pack()
        Button(rooth, text="Submit", command=Choice).pack()

    ##TIMER
        tk.messagebox.showinfo("WARNING!!", "THE TIMER HAS STARTED!!")
        second=StringVar()
        second.set("00")
        temp=180
        while temp >-1:
            secs=60
            second.set("{0:2d}".format(secs))

            rooth.update()
            time.sleep(1)

            if (temp == 30):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 30s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 10):
                tk.messagebox.showinfo("WARNING!!", "THERE ARE ONLY 10s REMAINING FOR YOU TO SOLVE THE RIDDLE!!")
            if (temp == 0):
                tk.messagebox.showinfo("TIME'S UP!!", "YOU LOST THE GAME :(")
                rooth.destroy()
            temp -= 1
    direction()  
    rooth.mainloop()

rootL = tk.Tk()
rootL.geometry("900x800")
rootL.title('Start Page')
label_1  = tk.Label(rootL, text = "WELCOME TO THE HAUNTED HOUSE", width = 50, font = ("bold", 25)).place(x = 30,y = 60)
label_2 = tk.Label(rootL, text = "ENTER YOUR NAME: ", width = 30, font = ("bold",12)).place(x = 125, y = 200)
name = tk.Entry(rootL)
name.place(x = 350, y = 200)
label_3  = tk.Label(rootL, text = "CHOOSE A MODE: ", width = 20, font = ("bold", 12)).place(x = 160,y = 250)

var = IntVar()
Radiobutton(rootL, text = "EASY", width = 15, font = ("bold", 11), variable = var, value = 1,command=easy).place(x = 230,y = 300)
Radiobutton(rootL, text = "MEDIUM", width = 15, font = ("bold", 11), variable = var, value = 2,command=medium).place(x = 450, y = 300)
Radiobutton(rootL, text = "HARD", width = 15, font = ("bold", 11), variable = var, value = 3,command=hard).place(x = 670, y = 300)
Button(rootL, text = 'START GAME', width = 30, bg = "blue", fg = 'black', font = ("bold",12), command = rootL.destroy).place(x = 300, y = 350) 
rootL.mainloop()

