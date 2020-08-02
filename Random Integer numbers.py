from tkinter import * # import the tkinter library .
from tkinter import ttk # import the ttk module . 
from random import randint # from the randim Lib import randint module .
def buttono(): # create a function .
    minimum = int(Entry.get(mini)) # get the value of 'Entry 1' and convert it to integer .
    maximum = int(Entry.get(maxi)) # get the value of 'Entry 2' and convert it to integer .
    if  maximum < minimum :
        tl.state('withdrawn')
        error.state('normal')
        error.lift()
        
    else :
        generate = randint(minimum, maximum)# generate a random nuber in range of the given values in 'mini' and 'maxi' .
        print(generate) # print the generated number .

window = Tk() # the main secondary window of the programme .
window.withdraw()  # hiding the main secondary window of the programme .
tl = Toplevel(bg = 'black' , bd = 6 ,  relief = 'ridge') # create the main window of the programe and design its borders .
tl.title("RANDOM NUMBERS GENERATOR") # specifying a title for the programme .
tl.geometry('360x400+450+150') # setting the programme geometry .
tl.resizable(False,False) # prevent the user from resizing the programme's window .
mini = ttk.Entry(tl , ) # ask the user to enter the minimum number .
mini.place(x = 25 , y = 150) # specifying  the first entry's place  .
maxi = ttk.Entry(tl) # ask the user to enter the maximum number .
maxi.place(x = 200 , y = 150) # specifying  the second entry's place .
label1 = Label(tl , text= "MIN" , bg = 'blue' ) # create a label to specify the kind of entry , design the lebel .
label1.place(x = 65 , y = 125) # specifying  the first  label's place .
label2 = Label(tl , text = "MAX" , bg = '#2cde5a') # create a label to specify the kind of entry , design the lebel .
label2.place(x = 240 , y = 125) # specifying  the second label's place .
button = Button( # create a button .
    tl , # the button's master .
    text ='GENERATE' , # the text on the button .
    bg = '#a92400' , # the background color of the button .
    activebackground = 'yellow' , # the color of the background of the button the moment the user click on it .
    fg = 'black' , # the color of the text on the button . 
    activeforeground = 'blue' , # the color of the color of the text which it is on  the button the moment the user click on the button .
    bd = 3 , # the button's border size .
    relief = "raised", # design the button's border .
    font = ('tahoma' , 10 , 'bold'), # design the font  of the text on the button .
    command = buttono  ) # the command of the button .
button.place( x = 140 , y = 320  ) # specify the button's place .
error = Toplevel(bg = 'black' , bd = 6 ,  relief = 'ridge')
error.state('withdrawn')
error.resizable(False,False)
error.geometry('300x120+450+300')
error.title('Error')
box = Label(error , text = " ERROR : 'MAX' < 'MIN'  , for example : \n " "'MIN'  =  2  " " , 'MAX' = 6  ;   6 > 2 ", bg = '#2cde5a' , font = ('tahoma' ,10, 'bold'))
box.place(x = 15 , y = 20)

def retry():
    tl.state('normal')
    error.state('withdrawn')
    tl.lift()
retry()
btn = Button(
    error ,
    text = '   OK   ',
    bg = 'red' ,
    activebackground = 'yellow' ,
    fg = 'black',
    activeforeground = 'blue' ,
    bd = 2 ,
    relief = "raised" ,
    font = ('tahoma' , 10 , 'bold'),
    command = retry
    )
btn.place(x = 115 , y = 80)
error.mainloop()
tl.mainloop() 
