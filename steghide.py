import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import subprocess


def center_window(width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

root = Tk()
root.title("Steghide Tool")
root.config()
window_width = 800
window_height = 400
center_window(window_width, window_height)

def steghide(message,password,carrier):
    subprocess.Popen(["Tools/hide in audio/steghide/steghide.exe"
                      ,"embed"
                      ,"-cf"
                      ,carrier
                      ,"-ef"
                      ,message
                      ,"-p"
                      ,password
                      ])
    messagebox.showinfo("Success","Message embedded successfully")


def steghide_extract(carrier,password):
        subprocess.getoutput(["Tools/hide in audio/steghide/steghide.exe"
                      ,"extract"
                      ,"-sf"
                      ,carrier
                      ,"-p"
                      ,password
                      ])
        messagebox.showinfo(title="info",message="file extracted sucessfully")
        

title= ttk.Label(root , text="Steghide tool hiding file inside file",font="Ubuntu 20 bold")
title.grid(row=0 ,column=0, columnspan=6 ,padx=20 ,pady=10)


title= ttk.Label(root , text="Steghide hide",font="Ubuntu 20 bold")
title.grid(row=1 ,column=0, columnspan=6 ,padx=10 ,pady=10)

#password
pass_label = ttk.Label(root,text="Enter password ")  
pass_label.grid(row=3 , column=3,padx=10, pady=10)

password = ttk.Entry(root,width=20)
password.grid(row=3 ,column=4) 


path_carrier_img_label= ttk.Label(root ,text = "path of the carrier file")
path_carrier_img_label.grid(row=3 , column=1 ,padx=10 ,pady=10)
    
path_carrier_img = ttk.Entry(root,width=50)
path_carrier_img.grid(row=3, column=2,padx=10,pady=10)



path_secret_message_label= ttk.Label(root ,text = "path of the secret mesaage")
path_secret_message_label.grid(row=4 , column=1 ,padx=10 ,pady=10)
    
path_secret_mesaage = ttk.Entry(root,width=50)
path_secret_mesaage.grid(row=4, column=2,padx=10,pady=10)
    
#select button carrier
def upload_carrier_file():
    name = filedialog.askopenfilename(title="select the carrie image")
    path_carrier_img.insert(0,name)

btn_select = ttk.Button(root, text="upload carrier",command = upload_carrier_file) 
btn_select.grid(row=6 , column=1 ,padx=10 ,pady=10 )


#uplaod secret message

def upload_secret_message():
    name = filedialog.askopenfilename(title="select the carrie image")
    path_secret_mesaage.insert(0,name)

btn_select = ttk.Button(root, text="upload sccret message",command = upload_secret_message) 
btn_select.grid(row=4 , column=3 ,padx=10 ,pady=10 )

#clear button

def clear_form():
    path_carrier_img.delete(0, 'end')
    password.delete(0, 'end')
    path_secret_mesaage.delete(0,'end')
    stego_file_path.delete(0,'end')
    extract.delete(0,'end')
    
btn_select = ttk.Button(root, text="clear",command = clear_form) 
btn_select.grid(row=6, column=2 ,padx=10 ,pady=10 )


#hide button
def hidebutton():
    carrier_fiile = path_carrier_img.get()
    secret_message = path_secret_mesaage.get() 
    passw= password.get()

    if carrier_fiile == '' or secret_message == '' or passw == '' :
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        steghide(secret_message,passw,carrier_fiile)

btn_hide = ttk.Button(root, text="hide",command = hidebutton) 
btn_hide.grid(row=6 , column=3 ,padx=10 ,pady=10 )



title= ttk.Label(root , text="Steghide extract",font="Ubuntu 20 bold")
title.grid(row=7 ,column=0, columnspan=6 ,padx=10 ,pady=10)

#btn extract 


extract_label= ttk.Label(root, text="the hidde file")
extract_label.grid(row=8 ,column=1 , padx=10 ,pady=10)

extract=  ttk.Entry(root, width=50)
extract.grid(row=8 ,column=2 ,padx=10,pady=10)


def extract_hidden_message():
     path = stego_file_path.get()
     passw= password.get()
     
     if path == '' or passw == '' :
         messagebox.showerror("Error", "Enter the password and select the path of stego file")
     else:
        steghide_extract(path,passw)


btn_extract = ttk.Button(root, text="extract", command=extract_hidden_message)
btn_extract.grid(row=8 , column=3 ,padx=10 ,pady=10)


def upload_stego_img():
    name = filedialog.askopenfilename(title="select file with secret message")
    stego_file_path.insert(0, name)
    
     
btn_upload = ttk.Button(root, text="upload",command=upload_stego_img)
btn_upload.grid(row=9 , column=3 ,padx=10 ,pady=10)

stego_img_label =  ttk.Label(root, text="select stego file")
stego_img_label.grid(row=9,column=1)

stego_file_path = ttk.Entry(root,width=50)
stego_file_path.grid(row=9 ,column=2) 


root.mainloop()