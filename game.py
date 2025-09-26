import sys
import subprocess
import tkinter as tk



root = tk.Tk()
root.title("Twisted Breakout")
root.geometry("200x200")
root.configure(bg="grey")


def play_game():
    root.destroy()
    subprocess.Popen([sys.executable, "main.py"])
    

def reset_game():
    subprocess.Popen([sys.executable, "reset.py"])
    


play_button = tk.Button(root, text="start", width=15, height=2,  bg="grey", fg="black", command=play_game)
play_button.pack(pady=(20, 20))

reset_button = tk.Button(root, text="reset", width=15, height=2,  bg="grey", fg="red", command=reset_game)
reset_button.pack(pady=(40,20))



root.mainloop()