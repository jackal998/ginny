# Program to make a simple
# login screen 
 
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import pyautogui

acc="ginny"
pwd="0607"

tries=3
logged=False

root=tk.Tk()
root.title("登入")
rootfont = tkFont.Font(family="FangSong", size=11)

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
w = 220
h = 80
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit(event=''):
    global acc, pwd, tries, logged
    
    name=name_var.get()
    password=passw_var.get()
    
    print("The name is : " + name)

    if(name == acc and password == pwd):
        tkinter.messagebox.showinfo("Alert Message", "登入成功!")
        name_var.set("")
        passw_var.set("")
        logged = True
        root.destroy()
        
    else:
        tries -= 1
        
        if(tries == 0):
            tkinter.messagebox.showinfo("Alert Message", "帳號已鎖定，請找管理員!")
            exit()
        else:
            tkinter.messagebox.showinfo("Alert Message", "帳號密碼錯誤,剩餘"+str(tries)+"次機會，將鎖定帳號")

# creating a label for
# name using widget Label
name_label = tk.Label(root, text = '輸入帳號', font=('calibre',10, 'bold'))
name_label.configure(font=rootfont)

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.configure(font=rootfont)
  
# creating a label for password
passw_label = tk.Label(root, text = '輸入密碼', font = ('calibre',10,'bold'))
passw_label.configure(font=rootfont)
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
passw_entry.configure(font=rootfont)
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = '送出', command = submit)
root.bind('<Return>', submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()

if logged:
    size = pyautogui.size()
    print(size)

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