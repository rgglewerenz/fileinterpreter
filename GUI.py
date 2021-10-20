"""
    University Honor Code
    Ross Lewerenz
    10-11-2021
    Project
"""
#imports
from os import times
from tkinter import *
from tkinter import font
from tkinter import filedialog
import Math
import math
import NewFile
import threading

#Root config
root = Tk()
root.geometry("1870x960")
root.title("File Interpreter")

#Makes the Icon Image
root.iconbitmap('Images/Icon Image.ico')


#Output Var
output = StringVar()
output.set("This is the output")

#Varriables used in Font sizes
increseRatio= 1.5
decreaseRatio = 0.9

#Vars used to check if user has already pressed the understand button
userUndertandsVar = StringVar()
userUndertandsVar.set("False")

#Vars used to set the commads so that it wont have to call Math.py Everytime
sumVar = StringVar()
sumVar.set("")
avgVar = StringVar()
avgVar.set("")
stdDvVar = StringVar()
stdDvVar.set("")
pdtVar = StringVar()
pdtVar.set("")
medVar = StringVar()
medVar.set("")
modeVar = StringVar()
modeVar.set("")
frqLstVar = StringVar()
frqLstVar.set("")

#Font spesific function
fontsizestrvar = StringVar()
fontsizestrvar.set("11")
def getFont(size):
    fontsizestr = fontsizestrvar.get()
    fontsize =int(math.log(int(fontsizestr)* int(math.sqrt(xsize()*ysize()))))
    print(fontsize)
    fonttype = "Ariel "
    if size == "reg":
        fontTotalreg = fonttype + str(fontsize)
        return fontTotalreg
    if size == "small":
        fontTotalsmall = fonttype + str(int(fontsize*decreaseRatio))
        return fontTotalsmall
    if size == "big":
        fontTotalBig = fonttype + str(int(fontsize*increseRatio))
        return fontTotalBig

#Background Image
bkg_img = PhotoImage(file="Images/background-large.png")
backgroundImage = Label(root, image=bkg_img)

#Sets the vars so that it wont call Math.py all the time
def setVars():
    sumVar.set("The sum is " + str(Math.sumList(file1List)))
    avgVar.set(Math.avgLst(file1List))
    stdDvVar.set(Math.stdDv(file1List))
    modeVar.set(Math.mode(file1List))
    pdtVar.set(Math.product(file1List))
    medVar.set(Math.median(file1List))
    frqLstVar.set(Math.FrqLst(file1List))

#Function that creates widjets, and edits their proporties
def createLables():
    #Title Label 
    title_lbl.config(
                    text= "Thank you for running this program, what would you like to do with your data?", 
                    background="lightSteelBlue4",
                    font = getFont("big")
                    )
    #Output Label
    ans_lbl.config(
                    textvariable=output, background="lightSteelBlue4", 
                    wrap= 300, 
                    font= getFont("small")
                    )
    #Informative Label
    notice_lbl.config(
                    text="Please note that, in order for this program to work you must use a file that has each value separated by a comma. Thank you for your patience", 
                    background="lightSteelBlue3", 
                    font= getFont("small")
                    )
def createBtn():
    #Sum Button
    btn_sum.config(
                    text="Calculate Sum",
                    command=sumClick, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    #Standard Deviation Button
    btn_stdDev.config(
                        text="Calculate Standard Deviation",
                        command=sdClick, 
                        background="lightSteelBlue4", 
                        font = getFont("small"),
                        wrap= int((xsize()/8)*1.5)                     
                    )
    #Product Button
    btn_mult.config(
                    text="Calculate Product",
                    command= pdctClick, 
                    background="lightSteelBlue4", 
                    font = getFont("reg"), 
                    wrap= xsize()/8 
                    )
    #Mode Button
    btn_mode.config(
                    text="Calculate Mode",
                    command=modeClick, 
                    background="lightSteelBlue4", 
                    font = getFont("reg"), 
                    wrap= xsize()/8 
                    )
    #Averge Button
    btn_avg.config(
                    text="Calculate Average",
                    command=avgClick, 
                    background="lightSteelBlue4",
                    font = getFont("reg"),
                    wrap= xsize()/8 
                    )
    #Median Button
    btn_med.config(
                    text="Calculate Median",
                    command=medianClick, 
                    background="lightSteelBlue4", 
                    font = getFont("reg"),
                    wrap= xsize()/8 
                    )
    #Frequency List Button
    btn_frq.config(
                        text="Finds the frequency of numbers", 
                        command=frqClick, 
                        background="lightSteelBlue4",
                        font= getFont("small"),
                        wrap= int((xsize()/8)*1.25)
                        )
    #Input File Button
    btn_file.config(
                    text="Press this to choose your file", 
                    command=revisedFile, 
                    background="lightSteelBlue4",
                    font = getFont("reg"), 
                    wrap= int((xsize()/8)*1.5)
                    )
    #Understand Button
    btn_undrst.config(
                        text="I understand", 
                        command=undrstClick, 
                        background="lightSteelBlue3",  
                        font =getFont("reg"),
                        wrap= xsize()/8                      
                        )
    #Output File Button
    btn_newFile.config( 
                        text="This button takes the data given and turns it into a txt file with the data used, and all of the functions above", 
                        command=newFileClick, 
                        background="lightSteelBlue4",  
                        font =getFont("small"),
                        wrap= int((xsize()/8)*2)
                        )

#Click Functions
#These Functions make it so that when you click their respective button they perform the action that they are linked to above
#The output.set() function is what changes the display once the button is clicked
def sumClick():
    if sumVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(sumVar.get())
def avgClick():
    if avgVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(avgVar.get())
def sdClick():
    if stdDvVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(stdDvVar.get())
def modeClick():
    if modeVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(modeVar.get())
def pdctClick():
    if pdtVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(pdtVar.get())
def medianClick():
    if medVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(medVar.get())
def frqClick():
    if frqLstVar.get() == "":
        output.set("Please enter a file location before atempting to evaluate it")
    else:
        output.set(frqLstVar.get() +"\n The 1st number is the item and the 2nd is the frequency")

#Confirm buttons
def undrstClick():
    userUndertandsVar.set("True")
    btn_undrst.destroy()
    notice_lbl.destroy()

#This is what runs when you want to dump this data into a new txt file
def newFileClick():
    try:
        file1List == 1
    except NameError:
        revisedFile()
    location = filedialog.askdirectory(title= "Select a folder to Place the New Data File", initialdir="/")
    NewFile.setFullString(file1List)
    lastOutput = "The data that is used is" + NewFile.getFullsting() + "\nThe sum is " + sumVar.get() + "\n" + medVar.get()+ "\n" + pdtVar.get()+ "\n" + avgVar.get()+ "\n" + stdDvVar.get()+ "\n" + modeVar.get()+ "\nThe frequency list is " + frqLstVar.get()
    output.set(NewFile.newFile(lastOutput,location))    
            

#This function converts a list of anything into a list of only the numbers
def convert(fileList):
    file = []
    b=0
    if fileList == []:
        return []
    else:
        for i in fileList:
            try:
                file.append(str(float(fileList[b])))
                b= b+1
            except ValueError:
                b=b+1
        return file

#This finction creates a file explorer window that allows the user to choose the file they would like to edit
def revisedFile():
    fileList = []
    global file1List
    filename = filedialog.askopenfilename(initialdir = "/", 
                                            title = "Select a File to Run Through the Program", 
                                            filetypes = (("Text files", "*.txt*"), 
                                                        ("CSV Files","*.csv*"),
                                                        ("All Files","*.*")))
    File = open(filename,"r+")
    doc = File.read()
    #Closes the file, so that it doesn't have to have the file loaded in the background
    File.close()
    fileList= doc.split(",")
    file1List  = convert(fileList)
    setVars()

#Funtion used for calculating spacing
def spacing():
    #creates Widgets
    createBtn()
    createLables()

    #spesific colums
    colum1= 0.5/7
    colum2=1.5/7
    colum3=2.5/7
    colum4=3.5/7
    colum5=4.5/7
    colum6=5.5/7
    colum7=6.5/7

    #constants
    widWidth =1/7
    widHeight = 1/8

    #spesific rows
    row1 = 0.5/5
    row2 = 1.5/5
    row3 = 2.5/5
    row4 = 3.5/5
    row5 = 4/5

    #Makes a bar the whole width of the screen
    widWidthFull = 1

    #Lables
    #Title Label
    title_lbl.place(
                    anchor= N, 
                    relx =  colum4 , 
                    rely = row1, 
                    relwidth= widWidthFull,
                    relheight= widHeight
                    )
    #Output Label
    ans_lbl.place(
                    anchor= N, 
                    relx = colum2 , 
                    rely = row3, 
                    #doubles the width
                    relwidth =widWidth*2,
                    #doubles the height 
                    relheight= widHeight*2
                )
    #Informative Label
    notice_lbl.place(
                        anchor= N, 
                        #Had to move it slightly to the right
                        relx = colum3+0.1, 
                        rely = row5, 
                        #Makes it wider by a factor of 6 to fit the large ammount of text
                        relwidth = widWidth*6, 
                        relheight =widHeight
                    )

    #Standard Buttons
    #Sum Button
    btn_sum.place(
                    anchor= N, 
                    relx = colum1, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    #Standard Deviation Button
    btn_stdDev.place(
                    anchor= N, 
                    relx = colum2, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight=widHeight
                    )
    #Product Button
    btn_mult.place(
                    anchor= N, 
                    relx = colum3, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight= widHeight
                    )
    #Mode Button
    btn_mode.place(
                    anchor= N, 
                    relx =  colum4,
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight=widHeight
                    )
    #Average Button
    btn_avg.place(
                    anchor= N, 
                    relx = colum5, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight=widHeight
                )
    #Median Button 
    btn_med.place(
                    anchor= N, 
                    relx = colum6, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight=widHeight
                    )
    #Frequency List Button
    btn_frq.place(
                    anchor= N, 
                    relx = colum7, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight=widHeight
                    )

    #Program Manipulation Buttons
    #Input File Button
    btn_file.place(
                    anchor= N, 
                    #had to move it sligtly to the right
                    relx = colum4+0.01, 
                    rely = row3, 
                    #doubles the width
                    relwidth= widWidth*2, 
                    relheight= widHeight
                    )   
    #Undertand Button
    btn_undrst.place(
                    anchor= N, 
                    relx = colum7, 
                    rely = row5, 
                    relwidth = widWidth, 
                    relheight =widHeight
                    )
    #Output Button
    btn_newFile.place(
                        anchor=N, 
                        #had to move it slightly to the right
                        relx= colum6 +0.03, 
                        #centers it in the middle of the y axsis
                        rely=0.5,
                        relwidth = widWidth*2, 
                        relheight =widHeight                        
                    )   
    #runs the command every 0.1 second
    threading.Timer(0.1, spacing).start()

def ysize():
    alllist=root.winfo_geometry()
    splitlist = alllist.split("+")
    xylist= splitlist[0].split("x")
    yvar = xylist[1]
    xvar = xylist[0]
    print(yvar)
    print(xvar)
    return int(yvar)
def xsize():
    alllist=root.winfo_geometry()
    splitlist = alllist.split("+")
    xylist= splitlist[0].split("x")
    yvar = xylist[1]
    xvar = xylist[0]
    print(yvar)
    print(xvar)
    return int(xvar)

#function that runs once the start button is clicked
def start():
    btn_Start.destroy()
    spacing()

#Labels
title_lbl = Label(root)
ans_lbl = Label(root)
notice_lbl = Label(root)

#Buttons
btn_sum = Button(root)
btn_stdDev = Button(root)
btn_mult = Button(root)
btn_mode = Button(root)
btn_avg = Button(root)
btn_med = Button(root)
btn_file = Button(root)
btn_frq = Button(root)
btn_undrst= Button(root)
btn_confirm = Button(root)
btn_newFile = Button(root)

#Creates the start button, This is required in order to kick off the program to reduce lag
btn_Start = Button(
                    root,
                     text = "Start Button", 
                     command=start,
                     background="LightSteelBlue2", 
                     font="Arial 50", 
                     width=10,
                     height=5
                   )
    


#Positioning start button
btn_Start.place(anchor=N, relx = 0.5, rely= 0.25)

#BackGround Image Placement
backgroundImage.place(x=0,y= 0)

#main root loop
root.mainloop()
