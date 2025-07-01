# # modules
# from random import choice
# from string import digits, ascii_letters
# import tkinter
# from sys import exit
# from time import sleep
# import os
# # variables
# root = tkinter.Tk()
# target = tkinter.PhotoImage(file = 'target.png')
# X = Y = R = 32
# W, H = 960, 540
# # keybutton = digits + ascii_letters
# interval = 1_000
# percentum = 0
# second = 300
# flag = True
# X_coord_doll = choice(range(R, W - R))
# Y_coord_doll = choice(range(R, H - R))
#
# Phantasia = set()
# while len(Phantasia) != 3:
#     Phantasia = {choice(range(int(second * 0.1), int(second - second * 0.1 + 1), int(second // 6.6))) for i in range(3)}
# Phantasia = tuple(Phantasia)
#
# ERROR_999 = choice([i for i in range(int(second * 0.1), int(second - second * 0.1 + 1), int(second // 6.6)) if i not in Phantasia])
#
# bg_image = tkinter.PhotoImage(file = 'horror.gif')
# bg_label = tkinter.Label(root,
#                          image=bg_image)
#
# bg_label.place(x=0,
#                y=0,
#                relwidth=1,
#                relheight=1)
#
# bg_label.image = bg_image
#
# # functions
# def esc(event):
#     if event.keysym == 'Escape':
#         root.destroy()
#         exit('easter egg')
#
# # def shot(event):
# #     if event.keysym == 'choice_keybutton':
# #         print('SHOT')
#
# # def new_target():
# #     global X, Y, second, flag
# #     if not flag:
# #         return
# #     X = choice(range(R, W - R))
# #     Y = choice(range(R, H - R))
# #     Button.place(x = X, y = Y)
# #     choice_keybutton = choice(keybutton)
# #     Button.configure(text = choice_keybutton)
# #     second += 1
# #     print(f'sec: {second}')
# #     Label.configure(text = count)
# #     if second >= 300:
# #         flag = False
# #         Button.destroy()
# #     else:
# #         root.after(interval, new_target)
# def new_target():
#     global X, Y, second, flag, percentum  # choice_keybutton
#     if not flag:
#         return
#     X = choice(range(R, W - R))
#     Y = choice(range(R, H - R))
#     Button.place(x = X,
#                  y = Y)
#     # choice_keybutton = choice(keybutton)
#     # Button.configure(text = choice_keybutton)
#     # Удаляем предыдущую привязку, если она была
#     if hasattr(root, '_current_key_binding'):
#         root.unbind(root._current_key_binding)
#     # Создаем новую привязку для текущей клавиши
#     # root._current_key_binding = f'<{choice_keybutton}>'
#     # root.bind(root._current_key_binding, lambda i: counter())
#     second -= 1
#     secundans.configure(text = second)
#     # print(f'count: {count}')
#     # print(f'sec: {second}, target key: {choice_keybutton}')
#     centum.configure(text=percentum)
#     percentum += 1
#     if second == 0:
#         flag = False
#         Button.destroy()
#     else:
#         root.after(interval, new_target)
#     if percentum == 100:
#         print('ФИНАЛЬНЫЙ СКРИМЕР')
#     if second in Phantasia:
#         print('СКРИМЕР-ГАЛЛЮЦИНАЦИЯ')
#     if second == ERROR_999:
#         bg_image.configure(file = 'ERROR_999.gif')
#
#
# def counter():
#     global percentum, Button
#     if percentum >= 2:
#         percentum -= 2
#     Button.place_forget()
#
# # widgets
# Button = tkinter.Button(root,
#                         activebackground = '#F80000',
#                         activeforeground = '#FFFFFF',
#                         anchor = 'center',
#                         background = 'systemButtonFace',
#                         borderwidth = 0,
#                         cursor = '',
#                         disabledforeground = 'systemDisabledText',
#                         font = 'bold',
#                         foreground = 'systemButtonText',
#                         highlightbackground = 'systemButtonFace',
#                         highlightcolor = 'systemWindowFrame',
#                         highlightthickness = 0,
#                         image = target,
#                         justify = 'center',
#                         padx = 0,
#                         pady = 0,
#                         relief = 'raised',
#                         repeatdelay = 0,
#                         repeatinterval = 0,
#                         takefocus = True,
#                         text = '',
#                         textvariable = None,
#                         underline = -1,
#                         wraplength = 0,
#                         command = counter,
#                         compound = 'center',
#                         default = 'normal',
#                         height = R,
#                         overrelief = 'raised',
#                         state = 'normal',
#                         width = R)
#
# centum = tkinter.Label(root,
#                        text = percentum,
#                        background = 'systemButtonFace')
#
# secundans = tkinter.Label(root,
#                           text = second,
#                           background = 'systemButtonFace')
#
# doll_image = tkinter.PhotoImage(file = "doll.gif")
# doll = tkinter.Button(root,
#                           file = 'doll.gif')
# doll.image = doll_image
# doll.place(x = X_coord_doll,
#            y = Y_coord_doll)
# # code
# def main():
#     root.title('Depths')
#     root.geometry(str(W)+'x'+str(H))
#     root.bind('<Key>', esc)
#     centum.place(x = W // 2,
#                  y = R // 2)
#     secundans.place(x = W - R,
#                     y = R // 2)
#     root.after(500, new_target)
#     root.mainloop()
#
# # entry point
# if __name__ == '__main__':
#     # os.pa
#     main()
#     pass


from random import choice
from string import digits, ascii_letters
import tkinter
from sys import exit
from time import sleep

# variables
root = tkinter.Tk()
target = tkinter.PhotoImage(file='OLD57_Depths_050425060425/target.png')
X = Y = R = 32
W, H = 960, 540
interval = 1_000
percentum = 0
second = 30
flag = True

# Инициализация координат куклы
X_coord_doll = choice(range(R, W - R))
Y_coord_doll = choice(range(R, H - R))

# Генерация особых моментов
Phantasia = set()
while len(Phantasia) != 3:
    Phantasia = {choice(range(int(second * 0.1), int(second - second * 0.1 + 1), int(second // 6.6))) for i in range(3)}
Phantasia = tuple(Phantasia)

ERROR_999 = choice(
    [i for i in range(int(second * 0.1), int(second - second * 0.1 + 1), int(second // 6.6)) if i not in Phantasia])

# Загрузка фонового изображения
try:
    bg_image = tkinter.PhotoImage(file='OLD57_Depths_050425060425/horror.gif')
    bg_label = tkinter.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_image
except:ERROR_999
    print("Не удалось загрузить фоновое изображение")
    bg_label = tkinter.Label(root, bg='black')
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Загрузка изображения куклы
try:
    doll_image = tkinter.PhotoImage(file="OLD57_Depths_050425060425/doll.gif")
except:
    print("Не удалось загрузить изображение куклы")
    doll_image = None


# functions
def esc(event):
    if event.keysym == 'Escape':
        root.destroy()
        exit('easter egg')


def new_target():
    global X, Y, second, flag, percentum, X_coord_doll, Y_coord_doll

    if not flag:
        return

    X = choice(range(R, W - R))
    Y = choice(range(R, H - R))
    Button.place(x=X, y=Y)

    second -= 1
    secundans.configure(text=second)
    centum.configure(text=percentum)
    percentum += 1

    if second == 0:
        flag = False
        Button.destroy()
    else:
        root.after(interval, new_target)

    if percentum == 100:
        print('ФИНАЛЬНЫЙ СКРИМЕР')

    if second in Phantasia:
        print('СКРИМЕР-ГАЛЛЮЦИНАЦИЯ')

    if second == ERROR_999:
        try:
            error_image = tkinter.PhotoImage(file='OLD57_Depths_050425060425/ERROR_999.gif')
            bg_label.configure(image=error_image)
            bg_label.image = error_image
            doll.place(x=X_coord_doll, y=Y_coord_doll)
        except:
            print("Не удалось загрузить изображение ошибки")


def counter():
    global percentum, Button
    if percentum >= 2:
        percentum -= 2
    Button.place_forget()


# widgets
Button = tkinter.Button(
    root,
    image=target,
    command=counter,
    borderwidth=0,
    highlightthickness=0,
    compound='center',
    height=R,
    width=R
)

centum = tkinter.Label(
    root,
    text=percentum,
    background='systemButtonFace',
    font=('Arial', 14)
)

secundans = tkinter.Label(
    root,
    text=second,
    background='systemButtonFace',
    font=('Arial', 14)
)

doll = tkinter.Button(
    root,
    image=doll_image,
    borderwidth=0,
    highlightthickness=0
)
doll.image = doll_image
doll.place_forget()


# code
def main():
    root.title('Depths')
    root.geometry(f'{W}x{H}')
    root.bind('<Key>', esc)

    centum.place(x=W // 2, y=R // 2)
    secundans.place(x=W - R, y=R // 2)

    root.after(500, new_target)
    root.mainloop()


# entry point
if __name__ == '__main__':
    main()