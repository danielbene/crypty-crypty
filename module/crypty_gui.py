import tkinter as tk
from module import crypty_cipher as cip

window = tk.Tk()
window.minsize(1000, 400)

# ----- FRAMES -----
frm_main = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

frm_buttons = tk.Frame(
    master=frm_main,
    borderwidth=1
)

frm_enc_key = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)

# ----- WIDGETS -----
txt_input = tk.Text(master=frm_main, width=50, height=15)
txt_output = tk.Text(master=frm_main, width=50, height=15, bg="lightgrey")
txt_output.config(state=tk.DISABLED)
lbl_key = tk.Label(master=frm_enc_key, text="Encryption key:")
ent_key = tk.Entry(master=frm_enc_key)

# ----- BUTTONS -----
btn_encrypt = tk.Button(
    master=frm_buttons,
    text="Encrypt",
    width=10,
    height=3
)

btn_compare = tk.Button(
    master=frm_buttons,
    text="Compare",
    width=10,
    height=3
)

btn_decrypt = tk.Button(
    master=frm_buttons,
    text="Decrypt",
    width=10,
    height=3
)


# nice-to-have: copy to clipboard from output window
def init_gui():
    init_binds()

    frm_main.pack(fill=tk.BOTH, expand=True)
    frm_enc_key.pack(fill=tk.BOTH)

    txt_input.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    frm_buttons.pack(side=tk.LEFT)
    btn_encrypt.pack(side=tk.TOP)
    btn_compare.pack(side=tk.TOP)
    btn_decrypt.pack(side=tk.TOP)

    txt_output.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    lbl_key.pack(fill=tk.BOTH, side=tk.LEFT)
    ent_key.pack(fill=tk.BOTH)

    window.mainloop()


def init_binds():
    # <Button-1> event represents LMB click
    btn_compare.bind("<Button-1>", compare)
    btn_encrypt.bind("<Button-1>",
                     lambda event, mode="enc": crypt(event, mode))
    btn_decrypt.bind("<Button-1>",
                     lambda event, mode="dec": crypt(event, mode))


def crypt(event, mode):
    # nice-to-have: using other optional ciphers
    text = txt_input.get("1.0", tk.END)
    key = ent_key.get()

    txt_output.config(state=tk.NORMAL)
    txt_output.delete("1.0", tk.END)
    if mode == "enc":
        txt_output.insert("1.0", cip.encrypt_vigenere(text, key))
    else:
        txt_output.insert("1.0", cip.decrypt_vigenere(text, key))
    txt_output.config(state=tk.DISABLED)


def compare(event):
    # nice-to-have: this. do it at the end
    print("Compare pressed")
