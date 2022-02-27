from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import sqlite3
import time

def Database():
    global conn, cursor
    conn = sqlite3.connect("db_members.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

#========================MAIN GUI=============================#

def main_program_screen():
    time.sleep(0.5)
    global program1
    program1 = Tk()
    program1.title("Universal Fitness")
    program1.geometry("350x365")
               
    WelcomeMsg = Label(program1, text="Welcome to Universal Fitness!", bg="pink", width="36", height="2", font=('arial',12,'bold'), justify=LEFT)
    WelcomeMsg.grid(row=0, column=0)
    btn_calculateBMI = Button(program1, text="BMI Calculator", fg="Blue", height="3", width="19", font=('arial',10,'bold',), bd=2, command=BMI, justify=LEFT)
    btn_calculateBMI.grid(row=1, column=0, pady=20)

    btn_trainingplan = Button(program1, text="Generate Training Plan", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=TrainingQuestions, justify=LEFT)
    btn_trainingplan.grid(row=2, column=0, pady=20)

    btn_exit = Button(program1, text="Exit", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=Exit, justify=LEFT)
    btn_exit.grid(row=3, column=0, pady=20)

#======================REGISTRATION FORM========================#

def main_screen():
    global screen
    screen = Tk()
    screen.title("Universal Fitness")
    screen.geometry("400x200")
   
    LblMsg = Label(screen, text="Please Login or Register to access Universal Fitness!", bg="pink", width="50", height="2", font=('arial',10,'bold'))
    LblMsg.grid(row=0, column=0)
                           
    Log = Button(screen, text="Login", height="3", width="11", font=('arial',10,'bold'), command=Login, justify=LEFT)
    Log.grid(row=1, column=0, pady=10)

    Reg = Button(screen, text="Register", height="3", width="11", font=('arial',10,'bold'), command=Register, justify=LEFT)
    Reg.grid(row=2, column=0)

    screen.mainloop()

#=======================FUNCTIONS==================================#

def Exit():
    Exit = tkinter.messagebox.askyesno("Universal Fitness", "Are you sure you want to exit?")
    if Exit > 0:
        program1.destroy()
        return

   
#========================BMI CALCULATOR=============================#

def BMI():

    program1.destroy()
    class BMI:

        def __init__(self, root):
            self.root = root
            self.root.title("Body Mass Index")
            self.root.geometry("1375x625")
            self.root.configure(background="Pink")

            BMIMainFrame = Frame(self.root, bd=20, width= 1350, height=700, padx=10, pady=10, bg="Pink", relief=RIDGE)
            BMIMainFrame.grid()

            LeftFrame = Frame(BMIMainFrame, bd=10, width=600, height=600, padx=10, pady=13, bg="Pink", relief=RIDGE)
            LeftFrame.pack(side=LEFT)

            RightFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            RightFrame.pack(side=RIGHT)

            LeftFrame0 = Frame(LeftFrame, bd=5, width=712, height=143, padx=5, bg="Pink", relief=RIDGE)
            LeftFrame0.grid(row=0, column=0)
            LeftFrame0.grid_propagate(False)
            LeftFrame1 = Frame(LeftFrame, bd=5, width=712, height=170, padx=5, pady=5, relief=RIDGE)                
            LeftFrame1.grid(row=4, column=0)
            LeftFrame2 = Frame(LeftFrame, bd=5, width=712, height=168, padx=5, pady=6, relief=RIDGE)
            LeftFrame2.grid(row=2, column=0)
            LeftFrame2.grid_propagate(False)
            LeftFrame3 = Frame(LeftFrame, bd=5, width=712, height=95, padx=5, pady=5, relief=RIDGE)
            LeftFrame3.grid(row=3, column=0)
            LeftFrame3.grid_propagate(False)
           
           
            RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
            RightFrame0.grid(row=0, column=0)
            RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)                
            RightFrame1.grid(row=1, column=0)
            RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=5, pady=6, bg="Grey", relief=RIDGE)
            RightFrame2.grid(row=2, column=0)

            HEIGHT = StringVar()
            WEIGHT = StringVar()
            HEIGHTSCALE = DoubleVar()
            WEIGHTSCALE = DoubleVar()
               
       
            def ReturnToMenu():
                ReturnToMenu= tkinter.messagebox.askyesno("Body Mass Index", "Confirm if you want to return to menu")
                if ReturnToMenu > 0:
                    root.destroy()
                    time.sleep(0.5)
                    main_program_screen()
                    return
                   

            def Reset():
                HEIGHT.set("")
                WEIGHT.set("")
                HEIGHTSCALE.set(0)
                WEIGHTSCALE.set(0)
                self.txtBMIResult.delete("1.0",END)

            def BMI_Calculator():
                BHeight = (HEIGHT.get())
                BWeight = (WEIGHT.get())

                self.txtBMIResult.delete("1.0",END)
                if(BHeight.isdigit() and BWeight.isdigit()):
                    BHeight = float(BHeight)
                    BWeight = float(BWeight)
                    BMI = float(BWeight / (BHeight/100)**2)
                    self.txtBMIResult.insert(END,BMI)
                    HEIGHTSCALE.set(BHeight)
                    WEIGHTSCALE.set(BWeight)
                    return True

                else:  
                    tkinter.messagebox.showwarning("Body Mass Index", "Enter a valid number")
                    HEIGHT.set("")
                    WEIGHT.set("")
                    HEIGHTSCALE.set(0)
                    WEIGHTSCALE.set(0)
                    self.txtBMIResult.delete("1.0",END)

               
            self.lblTitle = Label(LeftFrame0, text="Body Mass Index", padx=17, pady=4, bd=1, fg="#000000", font=('arial', 40, 'bold'), bg='White', width=20)
            self.lblTitle.pack()
            self.lblTitle.pack_propagate(False)

            self.BodyHeight = Scale(RightFrame0, variable = HEIGHTSCALE, from_ = 0, to = 220, length=507, tickinterval=20,
                                    orient = HORIZONTAL, state=DISABLED, label="Height in CM", font=('arial', 10, 'bold'))
            self.BodyHeight.grid(row=1, column=0)

            self.BodyWeight = Scale(RightFrame2, variable = WEIGHTSCALE, from_ = 0, to = 200, length=507, tickinterval=25,
                                    orient = HORIZONTAL, state=DISABLED, label="Weight in Kilograms", font=('arial', 10, 'bold'))
            self.BodyWeight.grid(row=1, column=0)

            self.lblBMITable = Label(RightFrame1,font=('arial',20,'bold'),text="\tBMI Table").grid(row=0,column=0)
            self.txtBMITable = Text(RightFrame1, height=12, width= 53, bd=16, font=('arial', 12, 'bold'))
            self.txtBMITable.grid(row=1, column=0, columnspan=3)

            self.txtBMITable.insert(END, 'Meaning \t\t\t\t' + "BMI \n\n")
            self.txtBMITable.insert(END, 'Underweight \t\t\t\t' + "Below 18.5 \n\n")
            self.txtBMITable.insert(END, 'Healthy Weight \t\t\t\t' + "18.5 - 24.9 \n\n")
            self.txtBMITable.insert(END, 'Overweight \t\t\t\t' + "25.0 - 29.9 \n\n")
            self.txtBMITable.insert(END, 'Obese \t\t\t\t' + "30.0 and Above \n\n")


            self.lblheight = Label(LeftFrame2, text= "Enter height in CM:", font=('arial', 20, 'bold'), bd=2, justify=LEFT)
            self.lblheight.grid(row=0, column=0, padx=15)
            self.txtheight = Entry(LeftFrame2, textvariable = HEIGHT, font=('arial',20,'bold'), bd=5, width=15, justify=RIGHT)
            self.txtheight.grid(row=0, column=1, pady=10)


            self.lblWeight = Label(LeftFrame2, text= "Enter height in Kilograms:", font=('arial', 20, 'bold'), bd=2, justify=LEFT)
            self.lblWeight.grid(row=1, column=0)
            self.txtWeight = Entry(LeftFrame2, textvariable = WEIGHT, font=('arial',20,'bold'), bd=5, width=15, justify=RIGHT)
            self.txtWeight.grid(row=1, column=1, pady=10)

            self.lblBMIResult = Label(LeftFrame3, text="Your BMI Result is:", font=('arial',20,'bold'), bd=2, justify=LEFT)
            self.lblBMIResult.grid(row=0, column=0)
            self.txtBMIResult = Text(LeftFrame3, padx=65, pady=12, bd=5, font=('arial',20,'bold'), bg="White", relief='sunk',
                                     width=13, height= 1)
            self.txtBMIResult.grid(row=0, column=1)

            self.btnBMI = Button(LeftFrame1, text= "Calculate BMI", bd=3, width=12, pady=4, height=3, font=('arial',20,'bold'), command=BMI_Calculator)
            self.btnBMI.grid(row=3, column=0)

            self.btnReset = Button(LeftFrame1, text= "Reset", bd=3, width=12, pady=4, height=3, font=('arial',20,'bold'), command=Reset)
            self.btnReset.grid(row=3, column=1)

            self.btnExit = Button(LeftFrame1, text= "Exit", bd=3, width=12, pady=4, height=3, font=('arial',20,'bold'), command=ReturnToMenu)
            self.btnExit.grid(row=3, column=2)

           
    if __name__ == '__main__':
        root = Tk()
        application = BMI(root)
        root.mainloop()

#========================CALCULATE TRAINING PROGRAM===================#

def TrainingQuestions():
    program1.destroy()
    class TrainingQuestions():

       
        def __init__(self,root):
            global screen1
            self.root = root
            self.root.title("Generate Training Program")
            self.root.geometry("650x500")
   
            screen1 = self.root
            screen1.grid()

           
            def ReturnToMenu():
                ReturnToMenu= tkinter.messagebox.askyesno("Training Program", "Confirm if you want to return to menu")
                if ReturnToMenu > 0:
                    root.destroy()
                    time.sleep(0.5)
                    main_program_screen()
                    return

           
            def comboclick():
                if myCombo.get() == "Power":
                    TrainingProgram1()
                elif myCombo.get() == "Strength":
                    TrainingProgram2()
                else:
                    TrainingProgram3()
               

            StartMessage = Label(screen1, text="Please complete the following questions below.", bg="pink", font=('arial',10,'bold'), justify=LEFT)
            StartMessage.grid(row=1, column=0, pady=5)

            Question1 = Label(screen1, text="What is your intended focus?", font=('arial',10,'bold'), justify=LEFT)
            Question1.grid(row=2, column=0, pady=5)

            options = [
                "Power",
                "Strength",
                "Fat Burning"
                ]
                 
            myCombo = ttk.Combobox(root, value=options, width=40, justify=LEFT)
            myCombo.grid(row=2, column=1, padx=30, pady=8)
            myCombo.current(0)
            myCombo.bind("<<ComboBoxSelected>>")

            Question2 = Label(screen1, text="How experienced in the gym are you?", font=('arial',10,'bold'), justify=LEFT)
            Question2.grid(row=3, column=0, pady=5)

            options2 = [
                "Beginner",
                "Advanced",
                "Expert"
                ]

            myCombo2 = ttk.Combobox(root, value=options2, width=40, justify=LEFT)
            myCombo2.grid(row=3, column=1, padx=30, pady=8)
            myCombo2.current(0)
            myCombo2.bind("<<ComboBoxSelected>>")

            Generate = Button(screen1, text="Generate Training Program", command=comboclick)
            Generate.grid(row=4, column=0)
                         
           
    if __name__ == '__main__':
        root = Tk()
        application = TrainingQuestions(root)
        root.mainloop()

#========================TRAINING PROGRAM 1 [Power]=============================#

def TrainingProgram1():

    class TrainingProgram1:
        screen1.destroy()
        def __init__(self,root):
            self.root = root
            self.root.title("Power Training Program")
            self.root.geometry("1250x600")
                   
            BMIMainFrame = Frame(self.root, bd=20, width= 1350, height=700, padx=10, pady=10, bg="Pink", relief=RIDGE)
            BMIMainFrame.grid()

            LeftFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            LeftFrame.pack(side=LEFT)

            RightFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            RightFrame.pack(side=RIGHT)

            LeftFrame0 = Frame(LeftFrame, bd=5, width=522, height=220, padx=5, pady=2, relief=RIDGE)
            LeftFrame0.grid(row=0, column=0)
            LeftFrame0.grid_propagate(False)
            LeftFrame0.propagate(0)
            LeftFrame1 = Frame(LeftFrame, bd=5, width=522, height=220, padx=5, relief=RIDGE)                
            LeftFrame1.grid(row=1, column=0)
            LeftFrame1.grid_propagate(False)

           
            RightFrame0 = Frame(RightFrame, bd=5, width=522, height=220, padx=5, pady=2, relief=RIDGE)
            RightFrame0.grid(row=0, column=0)
            RightFrame0.grid_propagate(False)
            RightFrame1 = Frame(RightFrame, bd=5, width=522, height=220, padx=5, relief=RIDGE)                
            RightFrame1.grid(row=1, column=0)
            RightFrame1.grid_propagate(False)

            def LegPressHelp():
                tkinter.messagebox.showinfo("Leg Press Help", "The leg press is a good exercise for people who may struggle with squat positioning.")   

            def SquatJumpHelp():
                tkinter.messagebox.showinfo("Squat Jump", "Cardio")
       
            Exc1 = Label(LeftFrame0, text="Leg Press:", font=('arial',15,'bold'))
            Exc1.grid(row=0, column=0)
            Exc1Info = Label(LeftFrame0, text="3 sets of 8 reps, 75% of your 1RM", font=('arial',13))
            Exc1Info.grid(row=0, column=1)
            Exc1Help = Button(LeftFrame0, text="Help", font=('arial', 10, 'bold'), padx=20, width=2, height=2, command=LegPressHelp)
            Exc1Help.grid(row=0, column=2)

           
            Exc2 = Label(LeftFrame0, text="Squat Jump:", font=('arial', 15,'bold'))
            Exc2.grid(row=2, column=0)
            Exc2Info= Label(LeftFrame0, text="4 sets of 5 reps", font=('arial',13))
            Exc2Info.grid(row=2, column=1)
            Exc2Help = Button(LeftFrame0, text="Help", font=('arial', 10, 'bold'), padx=20, width=2, height=2, command=SquatJumpHelp)
            Exc2Help.grid(row=2, column=2)
           
                           
           
           

    if __name__ == '__main__':
        root = Tk()
        application = TrainingProgram1(root)
        root.mainloop()

#========================TRAINING PROGRAM 2 [Strength Training Program]=============================#

def TrainingProgram2():

    class TrainingProgram2:
        screen1.destroy()
        def __init__(self,root):
            self.root = root
            self.root.title("Strength Training Program")
            self.root.geometry("1375x625")

            BMIMainFrame = Frame(self.root, bd=20, width= 1350, height=700, padx=10, pady=10, bg="Pink", relief=RIDGE)
            BMIMainFrame.grid()

            LeftFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            LeftFrame.pack(side=LEFT)

            RightFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            RightFrame.pack(side=RIGHT)
   
            LeftFrame0 = Frame(LeftFrame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
            LeftFrame0.grid(row=0, column=0)
            LeftFrame1 = Frame(LeftFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)                
            LeftFrame1.grid(row=1, column=0)
            LeftFrame2 = Frame(LeftFrame, bd=5, width=522, height=95, padx=5, pady=6, bg="Pink", relief=RIDGE)
            LeftFrame2.grid(row=2, column=0)
           
            RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
            RightFrame0.grid(row=0, column=0)
            RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)                
            RightFrame1.grid(row=1, column=0)
            RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=5, pady=6, bg="Pink", relief=RIDGE)
            RightFrame2.grid(row=2, column=0)

    if __name__ == '__main__':
        root = Tk()
        application = TrainingProgram2(root)
        root.mainloop()


#========================TRAINING PROGRAM 3 [Fat Burning Training Program]=============================#

def TrainingProgram3():

    class TrainingProgram3:
        screen1.destroy()
        def __init__(self,root):
            self.root = root
            self.root.title("Strength - Beginner / Advanced")
            self.root.geometry("1375x625")

            BMIMainFrame = Frame(self.root, bd=20, width= 1350, height=700, padx=10, pady=10, bg="Pink", relief=RIDGE)
            BMIMainFrame.grid()

            LeftFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            LeftFrame.pack(side=LEFT)

            RightFrame = Frame(BMIMainFrame, bd=10, width= 560, height=600, padx=10,pady=10, relief=RIDGE)
            RightFrame.pack(side=RIGHT)
   
            LeftFrame0 = Frame(LeftFrame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
            LeftFrame0.grid(row=0, column=0)
            LeftFrame1 = Frame(LeftFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)                
            LeftFrame1.grid(row=1, column=0)
            LeftFrame2 = Frame(LeftFrame, bd=5, width=522, height=95, padx=5, pady=6, bg="Pink", relief=RIDGE)
            LeftFrame2.grid(row=2, column=0)
           
            RightFrame0 = Frame(RightFrame, bd=5, width=522, height=200, padx=5, pady=2, relief=RIDGE)
            RightFrame0.grid(row=0, column=0)
            RightFrame1 = Frame(RightFrame, bd=5, width=522, height=280, padx=5, relief=RIDGE)                
            RightFrame1.grid(row=1, column=0)
            RightFrame2 = Frame(RightFrame, bd=5, width=522, height=95, padx=5, pady=6, bg="Pink", relief=RIDGE)
            RightFrame2.grid(row=2, column=0)

    if __name__ == '__main__':
        root = Tk()
        application = TrainingProgram3(root)
        root.mainloop()
       
#========================REGISTER======================================#

   
def Delete1():
    screen.destroy()


def Register():
    Delete1()
    class Register:
       
        def __init__(self, root):
            global USERNAME, PASSWORD, VERIFYPASSWORD, FIRSTNAME, LASTNAME, screen1
            self.root = root
            self.root.title("Register")
            self.root.geometry("400x290")

            screen1 = self.root
            screen1.grid()

            USERNAME = StringVar()
            PASSWORD = StringVar()
            VERIFYPASSWORD = StringVar()
            FIRSTNAME = StringVar()
            LASTNAME = StringVar()
           
            def main_program_screen():
                time.sleep(0.25)
                screen1.destroy()
                global program1
                program1 = Tk()
                program1.title("Universal Fitness")
                program1.geometry("350x365")
               
                WelcomeMsg = Label(program1, text="Welcome to Universal Fitness!", bg="pink", width="36", height="2", font=('arial',12,'bold'
                                                                                                                            ), justify=LEFT)
                WelcomeMsg.grid(row=0, column=0)

                btn_calculateBMI = Button(program1, text="BMI Calculator", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=BMI, justify=LEFT)
                btn_calculateBMI.grid(row=1, column=0, pady=20)

                btn_trainingplan = Button(program1, text="Generate Training Plan", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=TrainingQuestions, justify=LEFT)
                btn_trainingplan.grid(row=2, column=0, pady=20)

                btn_exit = Button(program1, text="Exit", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=Exit, justify=LEFT)
                btn_exit.grid(row=3, column=0, pady=20)
               
            def ReturnToMenu():
                screen1.destroy()
                main_screen()

            def Registration_Success():
                tkinter.messagebox.showinfo("Registered!", "Please Login with the same details")
                main_program_screen()                
   
            def Register_user():
                Database()
                if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
                    ErrorMsg = Label(screen1, text="Please complete the required fields!", fg="red")
                    ErrorMsg.grid(row=8, column=1)
                else:
                    cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
                    if cursor.fetchone() is not None:
                        ErrorMsg2 = Label(screen1, text="Username already exists!", fg="red")
                        ErrorMsg2.grid(row=8, column=1)
                    elif PASSWORD.get() != VERIFYPASSWORD.get():
                            ErrorMsg3 = Label(screen1, text="Passwords do not match!", fg="red")
                            ErrorMsg3.grid(row=8,column=1)
                    else:
                        cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                        conn.commit()
                        USERNAME.set("")
                        PASSWORD.set("")
                        FIRSTNAME.set("")
                        LASTNAME.set("")
                        VERIFYPASSWORD.set("")
                        Registration_Success()
                    cursor.close()
                    conn.close()

            Message = Label(screen1, text="Please enter details below!", font=('arial',10), justify=LEFT)
            Message.grid(row=1, column=0, pady=6, padx=12)

            LblUsername = Label(screen1, text="Username:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblUsername.grid(row=2, column=0, pady=8, padx=30)

            User = Entry(screen1, textvariable=USERNAME, font=('arial',10), bd=2, justify=RIGHT)
            User.grid(row=2, column=1, pady=8, padx=23)

            LblPassword = Label(screen1, text="Password:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblPassword.grid(row=3, column=0, pady=8)

            Pass = Entry(screen1, textvariable=PASSWORD, font=('arial',10), bd=2, show="*", justify=RIGHT)
            Pass.grid(row=3, column=1, pady=8)

            LblVerifyPass = Label(screen1, text="Verify Pass:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblVerifyPass.grid(row=4, column=0,pady=8)

            Verify = Entry(screen1, textvariable=VERIFYPASSWORD, font=('arial',10), bd=2, show="*", justify=RIGHT)
            Verify.grid(row=4, column=1, pady=8)

            LblFirstName = Label(screen1, text="Firstname:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblFirstName.grid(row=5, column=0, pady=8)

            FirstN = Entry(screen1, textvariable=FIRSTNAME, font=('arial',10), bd=2, justify=RIGHT)
            FirstN.grid(row=5, column=1, pady=8)

            LblLastName = Label(screen1, text="Lastname:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblLastName.grid(row=6, column=0, pady=8)

            LastN = Entry(screen1, textvariable=LASTNAME, font=('arial',10), bd=2, justify=RIGHT)
            LastN.grid(row=6, column=1, pady=8)

            RegisterButton = Button(screen1, text="Register", width=10, height=1, command=Register_user, justify=LEFT)
            RegisterButton.grid(row=7, column=1, padx=20, pady=10)

            ReturnToMenu = Button(screen1, text="Back", width=10, height=1, command=ReturnToMenu, justify=LEFT)
            ReturnToMenu.grid(row=7, column=0)

    if __name__ == '__main__':
        root = Tk()
        application = Register(root)
        root.mainloop()

#========================LOGIN=============================#



def Login():
    Delete1()
    class Login:
        def __init__(self, root):
            global screen2, USERNAME, PASSWORD
            self.root = root
            self.root.title("Login")
            self.root.geometry("390x180")

            screen2 = self.root
            screen2.grid()

            USERNAME = StringVar()
            PASSWORD = StringVar()
   
            def main_program_screen():
                global program1
                screen2.destroy()
                program1 = Tk()
                program1.title("Universal Fitness")
                program1.geometry("350x365")
               
                WelcomeMsg = Label(program1, text="Welcome to Universal Fitness!", bg="pink", width="36", height="2", font=('arial',12,'bold'
                                                                                                                            ), justify=LEFT)
                WelcomeMsg.grid(row=0, column=0)
                btn_calculateBMI = Button(program1, text="BMI Calculator", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=BMI, justify=LEFT)
                btn_calculateBMI.grid(row=1, column=0, pady=15)

                btn_trainingplan = Button(program1, text="Generate Training Plan", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=TrainingQuestions, justify=LEFT)
                btn_trainingplan.grid(row=2, column=0, pady=15)

                btn_exit = Button(program1, text="Exit", fg="Blue", height="3", width="19", font=('arial',10,'bold'), bd=2, command=Exit, justify=LEFT)
                btn_exit.grid(row=3, column=0, pady=15)
           
            def Login_user():
                Database()
                if PASSWORD.get() == "" or USERNAME.get() == "":
                    ErrorMsg = Label(screen2, text="Please complete the required fields!", fg="red")
                    ErrorMsg.grid(row=5, column=1)
                else:
                    cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
                    if cursor.fetchone() is not None:
                        main_program_screen()
                    else:
                        ErrorMsg2 = Label(screen2, text="Invalid Login, please try again", fg="red")
                        ErrorMsg2.grid(row=5,column=1)
                    cursor.close()
                    conn.close()


            def ReturnToMenu():
                screen2.destroy()
                main_screen()
               
            Message = Label(screen2, text="Please enter Login details below!")
            Message.grid(row=1, column=0, pady=7, padx=9)
           
            LblUsername = Label(screen2, text="Username:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblUsername.grid(row=2, column=0, padx=15)

            USERNAME = Entry(screen2, textvariable=USERNAME, font=('arial',10), bd=2, justify=RIGHT)
            USERNAME.grid(row=2, column=1, pady=6, padx=20)

            LblPassword = Label(screen2, text="Password:", font=('arial',10,'bold'), bd=2, justify=LEFT)
            LblPassword.grid(row=3, column=0)

            PASSWORD = Entry(screen2, textvariable=PASSWORD, font=('arial',10), bd=2, show="*", justify=RIGHT)
            PASSWORD.grid(row=3, column=1)

            LoginButton = Button(screen2, text="Login", width=10, height=1, command=Login_user, justify=LEFT)
            LoginButton.grid(row=4, column=1, padx=20, pady=15)

            ReturnToMenu = Button(screen2, text="Back", width=10, height=1, command=ReturnToMenu, justify=LEFT)
            ReturnToMenu.grid(row=4, column=0)

           
    if __name__ == '__main__':
        root = Tk()
        application = Login(root)
        root.mainloop()
       
main_screen()

	
