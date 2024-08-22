#working keyboard
import tkinter as tk
win = tk.Tk()
win.geometry('500x350')

keyframe = tk.Frame(master=win, cursor='dot')
keyframe.pack(side='bottom')

screen = tk.Label(text='', bg='white', fg='black', width=40, height=10)
screen.pack(side='top')

keys = ['Q','W','E','R','T','Y','U','I','O','P',
        'A','S','D','F','G','H','J','K','L',
        'Z','X','C','V','B','N','M',' ',"'",'.','!',
        'Del', '->'
       ]
screenText = ''
#add text on the screen label
def printonscreen(letter):
    global screenText
    
    if letter == 'Del':
        screenText = screenText[:len(screenText)-1] #bug here where replace() would replace one letter but if there were 
                                                    # multiple instances it would delete those one by one instead
                                                    # of going in backwards order
    elif letter == '->':
        print(screenText)
    else:
        screenText += letter
    screen.config(text = screenText)

#set up keyboard
currentRow = 0
currentCol = 0
counter = 1
required = 10
for item in keys:
    new = tk.Button(
        keyframe,
        text = item,
        bd=10,
        fg='black',
        relief='raised',
        command = lambda item=item : printonscreen(item) #if command = press() it will execute the command upon startup
                                                #got the item=item from stack overflow, it's a late binding issue 
                                                # (causes all keys to execute the last key)
    )
    new.grid(row = currentRow, column = currentCol, padx=0.5, pady=1)
    if counter == required:
        if required == 40:
            break
        else:
            currentRow += 1
            currentCol = 0
            required += 10

    counter += 1
    currentCol += 1

win.mainloop()