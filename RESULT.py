# modules
from random import choice
from string import digits, ascii_letters
import tkinter
from sys import exit
from time import sleep

# variables
root = tkinter.Tk()
target = tkinter.PhotoImage(file = 'OLD57_Depths_050425060425/target.png')
X = Y = R = 32
W, H = 960, 540
interval = 1_000
second = percentum = 15
flag = True
Phantasia = set()
while len(Phantasia) != 3:
    Phantasia = {choice(range(30, 271, 60)) for i in range(3)}
print(Phantasia)
bg_image = tkinter.PhotoImage(file = 'OLD57_Depths_050425060425/horror.gif')
bg_label = tkinter.Label(root,
                         image=bg_image)

bg_label.place(x=0,
               y=0,
               relwidth=1,
               relheight=1)

bg_label.image = bg_image

# functions
def esc(event):
    if event.keysym == 'Escape':
        root.destroy()
        exit('easter egg')

def new_target():
    global X, Y, second, flag, percentum
    if not flag:
        return
    X = choice(range(R, W - R))
    Y = choice(range(R, H - R))
    Button.place(x = X,
                 y = Y)
    if hasattr(root, '_current_key_binding'):
        root.unbind(root._current_key_binding)
    second += 1
    secundans.configure(text = second)
    percentum += 1
    centum.configure(text = percentum)
    if second >= 300:
        flag = False
        Button.destroy()
    else:
        root.after(interval, new_target)
    if percentum == 100:
        print('ФИНАЛЬНЫЙ СКРИМЕР')
def counter():
    global percentum, Button
    if percentum >= 1:
        percentum -= 2
    Button.place_forget()

# widgets
Button = tkinter.Button(root,
                        activebackground = '#F80000',
                        activeforeground = '#FFFFFF',
                        anchor = 'center',
                        background = 'systemButtonFace',
                        borderwidth = 0,
                        cursor = '',
                        disabledforeground = 'systemDisabledText',
                        font = 'bold',
                        foreground = 'systemButtonText',
                        highlightbackground = 'systemButtonFace',
                        highlightcolor = 'systemWindowFrame',
                        highlightthickness = 0,
                        image = target,
                        justify = 'center',
                        padx = 0,
                        pady = 0,
                        relief = 'raised',
                        repeatdelay = 0,
                        repeatinterval = 0,
                        takefocus = True,
                        text = '',
                        textvariable = None,
                        underline = -1,
                        wraplength = 0,
                        command = counter,
                        compound = 'center',
                        default = 'normal',
                        height = R,
                        overrelief = 'raised',
                        state = 'normal',
                        width = R)

centum = tkinter.Label(root,
                       text = percentum,
                       background = 'systemButtonFace')

secundans = tkinter.Label(root,
                          text = second,
                          background = 'systemButtonFace')

# code
def main():
    root.title('Depths')
    root.geometry(str(W)+'x'+str(H))
    root.bind('<Key>', esc)
    centum.place(x = W // 2,
                 y = R // 2)
    secundans.place(x = W - R,
                    y = R // 2)
    root.after(500, new_target)
    root.mainloop()

# entry point
if __name__ == '__main__':
    main()
