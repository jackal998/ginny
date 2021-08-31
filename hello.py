# Program to make a simple
# login screen 
 
from google_db import gsheet_find, gsheet_update
from werkzeug import get_machine_id
from encryptor import *
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import pyautogui

tries=3
logged=False

# defining a function that will
# get the name and password and
# print them on the screen
def submit(name_var,passw_var):
    global tries, logged
    
    name = name_var.get()
    password = passw_var.get()

    db_pwd = gsheet_find(name,'password')

    if db_pwd == None:
        tries -= 1
        tkinter.messagebox.showinfo("Alert Message", "帳號或密碼錯誤,剩餘"+str(tries)+"次機會，將鎖定帳號")
    else:
        if encomp(password, db_pwd):

            # check or update uuid
            local_uuid = get_machine_id().decode()
            db_uuid = gsheet_find(name,'uuid')
            if db_uuid == None:
                gsheet_update(name, 'uuid', local_uuid)
            elif db_uuid != local_uuid:
                tkinter.messagebox.showinfo("Alert Message", "帳號不允許在此設備上運作，請找管理員!")
                exit()

            tkinter.messagebox.showinfo("Alert Message", "登入成功!")
            name_var.set("")
            passw_var.set("")
            logged = True
            login_window.destroy()
        else:
            tries -= 1
            if(tries == 0):
                tkinter.messagebox.showinfo("Alert Message", "帳號已鎖定，請找管理員!")
                exit()
            else:
                tkinter.messagebox.showinfo("Alert Message", "帳號或密碼錯誤,剩餘"+str(tries)+"次機會，將鎖定帳號")

def login_window_init():

    login_window=tk.Tk()
    login_window.title("登入")
    login_windowfont = tkFont.Font(family="FangSong", size=11)

    # get screen width and height
    ws = login_window.winfo_screenwidth() # width of the screen
    hs = login_window.winfo_screenheight() # height of the screen
    w = 220
    h = 80
    # calculate x and y coordinates for the Tk login_window window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen 
    # and where it is placed
    login_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    # declaring string variable
    # for storing name and password
    name_var=tk.StringVar()
    passw_var=tk.StringVar()

    # creating a label for
    # name using widget Label
    name_label = tk.Label(login_window, text = '輸入帳號', font=('calibre',10, 'bold'))
    name_label.configure(font=login_windowfont)

    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(login_window,textvariable = name_var, font=('calibre',10,'normal'))
    name_entry.configure(font=login_windowfont)
    
    # creating a label for password
    passw_label = tk.Label(login_window, text = '輸入密碼', font = ('calibre',10,'bold'))
    passw_label.configure(font=login_windowfont)
    
    # creating a entry for password
    passw_entry=tk.Entry(login_window, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    passw_entry.configure(font=login_windowfont)
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(login_window,text = '送出', command = lambda: submit(name_var,passw_var))
    login_window.bind('<Return>', lambda event: submit(name_var,passw_var))
    
    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1, pady=5)

    return login_window

login_window = login_window_init()
# performing an infinite loop
# for the window to display
login_window.mainloop()

if logged:
    size = pyautogui.size()
    print(size)

    image_path = 'src/img/thumb.png'

    buttonx = None
    while (buttonx == None):
        try:
            buttonx, buttony = pyautogui.locateCenterOnScreen(image_path)
        except Exception as e:
            print(e)
            
    pyautogui.click(buttonx, buttony)

    pyautogui.moveTo(960, 540, 0.3)
    pyautogui.moveTo(400, 800, duration=1)     # 用2秒移动到(100, 200)位置

    # #When program finds image, print the location
    pyautogui.alert('現在滑鼠的座標是：{}'.format(pyautogui.position()))
    last_pos = pyautogui.position()

    move_times = 0

    try:
        while move_times < 100:
            new_pos = pyautogui.position()
            if last_pos != new_pos:
                print(new_pos)
                last_pos = new_pos
                move_times +=1
    except KeyboardInterrupt:
        print('\nExit')

    pyautogui.alert('好玩ㄇ？')