
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root1 = Tk()  # root window
root1.title("Enigma Machine Emulator")

def encrypt1():
    pass

def encrypt():
    window = Toplevel(root1)


# make an Entry to take plaintext input, label it
plaintext_entry_label = ttk.Labelframe(root1, text="Enter Plaintext To Either Encrypt Or Decrypt:", padding="10 10 10 10")
plaintext_entry = Text(plaintext_entry_label, height=4, width=50)
plaintext_entry.focus()  # make the cursor appear in the plaintext entry box by default


# entry for displaying ciphertext output
ciphertext_entry_label = ttk.Labelframe(root1, text="Output Of CipherText:", padding="10 10 10 10")
ciphertext = ""
ciphertext_entry = Text(ciphertext_entry_label, height=4, width=50)
ciphertext_entry.insert(END, ciphertext)


settings_frame = ttk.Labelframe(root1, text="Settings", padding="10 10 10 10")
# dropdowns to select which scrambler to use
available_rotors = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'none']
pick = ttk.Labelframe(settings_frame, text='Rotor Configuration', padding="5 5 5 5")
select_rotor_1 = ttk.Combobox(pick, values=available_rotors, state='readonly', width=5)
select_rotor_1.current(0)  # set which one appears by default

select_rotor_2 = ttk.Combobox(pick, values=available_rotors, state='readonly', width=5)
select_rotor_2.current(8)

select_rotor_3 = ttk.Combobox(pick, values=available_rotors, state='readonly', width=5)
select_rotor_3.current(8)


# dropdown to select which reflector to use
available_reflectors = ["B", "C"]
pick4 = ttk.Labelframe(settings_frame, text='Reflectors Configuration')
select_reflector = ttk.Combobox(pick4, values=available_reflectors, state='readonly', width=2)
select_reflector.current(0)

# Entries to specify starting positions of rotors
set_pos = ttk.Labelframe(settings_frame, text='Start Position Configuration')
pos1 = ''
set1 = ttk.Entry(set_pos, textvariable=pos1, width=5)
pos2 = ''
set2 = ttk.Entry(set_pos, textvariable=pos2, width=5)
pos3 = ''
set3 = ttk.Entry(set_pos, textvariable=pos3, width=5)


# entry to add plugboard settings
plugboard_entry_label = ttk.Labelframe(settings_frame, text="Plugboard Configurations")
plugtext = ""
plugboard_entry_text = StringVar()
plugboard_entry_text.set(plugtext)
plugboard_entry = ttk.Entry(plugboard_entry_label, textvariable=plugboard_entry_text)

encrypt_button = ttk.Button(root1, text="Encrypt Message", command=encrypt)


# make a button that closes the window
close_button = ttk.Button(root1, text='Exit', command=root1.quit)


# PACK ALL THE THINGS!
plaintext_entry.grid(in_=plaintext_entry_label)
plaintext_entry_label.grid(column=0, row=0, padx=10, pady=10)

encrypt_button.grid(column=0, row=1)

ciphertext_entry.grid(in_=ciphertext_entry_label)
ciphertext_entry_label.grid(column=0, row=2, padx=10, pady=10)


settings_frame.grid(column=1, row=0, rowspan=3, padx=10, pady=10)
pick.grid(in_=settings_frame, column=0, row=0, padx=5, pady=5)
select_rotor_1.grid(in_=pick, padx=5, pady=5)
select_rotor_2.grid(in_=pick, column=1, row=0, padx=5, pady=5)
select_rotor_3.grid(in_=pick, column=2, row=0,  padx=5, pady=5)

set_pos.grid(in_=settings_frame, column=0, row=1, padx=5, pady=5)
set1.grid(in_=set_pos, column=0, row=1, padx=5, pady=5)
set2.grid(in_=set_pos, column=1, row=1, padx=5, pady=5)
set3.grid(in_=set_pos, column=2, row=1, padx=5, pady=5)

pick4.grid(in_=settings_frame, column=0, row=2, padx=5, pady=5)
select_reflector.grid(in_=pick4, padx=5, pady=5, sticky="ew")
pick4.grid_columnconfigure(0, weight=1)

plugboard_entry_label.grid(in_=settings_frame, row=3, padx=5, pady=5)
plugboard_entry.grid(in_=plugboard_entry_label, padx=5, pady=5)


close_button.grid(column=1, row=3, padx=10, pady=10)


# Run Graphical User Interface
root1.mainloop()
