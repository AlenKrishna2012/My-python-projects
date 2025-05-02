import tkinter as tk
import time
def update_time():
	current_time = time.strftime('%r')
	label.config(text=current_time)
	label.after(1000, update_time)
root = tk.Tk()
root.title("Digital Clock")
label = tk.Label(root, font=('calibri', 40,'bold'), background='black',foreground='white')
label.pack(fill='both',expand=1)
update_time()
root.mainloop()