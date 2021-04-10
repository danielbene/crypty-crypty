import tkinter as tk

window = tk.Tk()

main_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

entry_key_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

main_frame.pack()
entry_key_frame.pack()

text_input = tk.Text(master=main_frame, width=50, height=15)
text_input.pack(side=tk.LEFT)

label = tk.Label(master=main_frame, text="kolbasz")
label.pack(side=tk.LEFT)

text_output = tk.Text(master=main_frame, width=50, height=15)
text_output.pack(side=tk.LEFT)

entry_key = tk.Entry(master=entry_key_frame)
entry_key.pack()

window.mainloop()
