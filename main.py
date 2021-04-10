import tkinter as tk

window = tk.Tk()
window.minsize(1000, 400)

# ----- FRAMES -----
main_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

button_frame = tk.Frame(
    master=main_frame,
    borderwidth=1
)

entry_key_frame = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

# ----- BUTTONS -----
button_encrypt = tk.Button(
    master=button_frame,
    text="Encrypt",
    width=10,
    height=3
)

button_compare = tk.Button(
    master=button_frame,
    text="Compare",
    width=10,
    height=3
)

button_decrypt = tk.Button(
    master=button_frame,
    text="Decrypt",
    width=10,
    height=3
)

# ----- BUILD -----
main_frame.pack(fill=tk.BOTH, expand=True)
entry_key_frame.pack(fill=tk.BOTH)

text_input = tk.Text(master=main_frame, width=50, height=15)
text_input.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

button_frame.pack(side=tk.LEFT)
button_encrypt.pack(side=tk.TOP)
button_compare.pack(side=tk.TOP)
button_decrypt.pack(side=tk.TOP)

text_output = tk.Text(master=main_frame, width=50, height=15, bg="lightgrey")
text_output.config(state=tk.DISABLED)
text_output.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

label_key = tk.Label(master=entry_key_frame, text="Encryption key:")
label_key.pack(fill=tk.BOTH, side=tk.LEFT)
entry_key = tk.Entry(master=entry_key_frame)
entry_key.pack(fill=tk.BOTH)

window.mainloop()
