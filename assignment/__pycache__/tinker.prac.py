import tkinter as tk
window=tk.Tk()
window.title("my first tkinter")
label=tk.Label(window,text="hello world !", font=("Aial",18))
label.pack()
window.geometry("400x400")
button=tk.Button(window,text="click me")
button.pack(padx=100,pady=50)
frame=tk.Frame(window)
frame.pack()

window.mainloop()