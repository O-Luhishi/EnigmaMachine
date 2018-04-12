from tkinter import *
from tkinter import ttk
import MachineLogic

class MainInterface:
    def __init__(self, parent):
        settings = ConfigurationWindow()
        self.parent = parent
        parent.title("Enigma Machine Emulator")
        self.initialiseWindow()
        settings.settingsWindow()
        settings.window.grab_set()

    def initialiseWindow(self):
        settings = ConfigurationWindow()
        enc = Encryption()
        global plaintext_entry, ciphertext_entry
        # make an Entry to take plaintext input, label it
        plaintext_entry_label = ttk.Labelframe(root1, text="Enter Plaintext To Encrypt/Decrypt:", padding="10 10 10 10")
        plaintext_entry = Text(plaintext_entry_label, height=4, width=50)
        plaintext_entry.focus()  # make the cursor appear in the plaintext entry box by default


        # entry for displaying ciphertext output
        ciphertext_entry_label = ttk.Labelframe(root1, text="Output Of CipherText:", padding="10 10 10 10")
        ciphertext = ""
        ciphertext_entry = Text(ciphertext_entry_label, height=4, width=50)
        ciphertext_entry.insert(END, ciphertext)

        #Encryption And Decryption Buttons
        btn_Encrypt = ttk.Button(root1, text="Encrypt Message", command=enc.encrypt)
        btn_Decrypt = ttk.Button(root1, text="Decrypt Cipher", command=enc.encrypt)

        # Configuration Button To Open settings
        btn_Configuration = ttk.Button(root1, text="Configure Machine", command=settings.settingsWindow)

        # Exit Button To Close Program Safely
        btn_Exit = ttk.Button(root1, text='Exit', command=root1.quit)


        # PACK ALL THE THINGS!
        plaintext_entry.grid(in_=plaintext_entry_label)
        plaintext_entry_label.grid(column=0, row=0, padx=10, pady=10)

        btn_Encrypt.grid(sticky="w", column=0, row=1, padx=10, pady=10)
        btn_Decrypt.grid(sticky="e", column=0, row=1, padx=10, pady=10)

        ciphertext_entry.grid(in_=ciphertext_entry_label)
        ciphertext_entry_label.grid(column=0, row=2, padx=10, pady=10)

        btn_Configuration.grid(sticky="w", column=0, row=3, padx=10, pady=10)
        btn_Exit.grid(sticky="e",column=0, row=3, padx=10, pady=10)

class ConfigurationWindow:
    def settingsWindow(self):
        global select_rotor_1, select_rotor_2, select_rotor_3
        self.window = Toplevel(root1)
        self.window.wm_attributes("-topmost",1)
        self.window.focus()
        #self.window.grab_set()
        self.window.title("Enigma Machine")

        settings_frame = ttk.Labelframe(self.window, text="Configure Machine", padding="10 10 10 10")
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
        lbl_plugboard = ttk.Labelframe(settings_frame, text="Plugboard Configurations")
        plugtext = ""
        txt_plugboard = StringVar()
        txt_plugboard.set(plugtext)
        plugboard_entry = ttk.Entry(lbl_plugboard, textvariable=txt_plugboard)

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

        lbl_plugboard.grid(in_=settings_frame, row=3, padx=5, pady=5)
        plugboard_entry.grid(in_=lbl_plugboard, padx=5, pady=5)

        btn_Save = ttk.Button(self.window, text="Save Settings", command= lambda: self.saveWindow(select_rotor_1.current(), select_rotor_2.current(), select_rotor_3.current(), select_reflector.current(), plugboard_entry.get(), set1.get(), set2.get(), set3.get()))
        btn_Save.grid(column=1, row=3, padx=5, pady=5)

    def saveWindow(self, rotor, rotors2, rotors3, reflectors, entryPlug, sets1, sets2, sets3):

        global rotor1, rotor2, rotor3, reflector, plugboard, set1, set2, set3
        rotor1 = rotor
        rotor2 = rotors2
        rotor3 = rotors3
        reflector = reflectors
        plugboard = entryPlug
        set1 = sets1
        set2 = sets2
        set3 = sets3
        self.window.destroy()

    def getRotor1(self):
        return rotor1
    def getRotor2(self):
        return rotor2
    def getRotor3(self):
        return rotor3
    def getReflector(self):
        return reflector
    def getPlugBoard(self):
        return plugboard
    def getSet1(self):
        return set1
    def getSet2(self):
        return set2
    def getSet3(self):
        return set3

class Encryption:
    def __init__(self):
        pass
    def encrypt(self):
        settingsPage = ConfigurationWindow()
        plugboard = BuildPlugboard()
        # tidy entry of plaintext
        plain = plaintext_entry.get(1.0, END).strip()
        plain = plain.lower()

        # check can process plain, or display error message
        total = 0
        for c in plain:
            if c.isalpha() or c == " ":
                total += 1
        if total != len(plain):
            tkinter.messagebox.showerror("Error", "Invalid plaintext")

        # put the right scramblers and reflector in the machine
        scram_list = [
            MachineLogic.possible_scramblers[settingsPage.getRotor1()],
            MachineLogic.possible_scramblers[settingsPage.getRotor2()],
            MachineLogic.possible_scramblers[settingsPage.getRotor3()]
        ]
        refl = MachineLogic.possible_reflectors[settingsPage.getReflector()]

        # make a Plugboard from the entry
        plug = plugboard.build_plugboard(settingsPage.getPlugBoard())
        if not plug.valid_Plugboard():
            tkinter.messagebox.showerror("Error", "This is not a valid plugboard:\n not mapped in pairs")

        # set the starting orientations of the rotors
        orient_list = [settingsPage.getSet1(), settingsPage.getSet2(), settingsPage.getSet3()]
        for i in orient_list:
            if len(i) > 1 or not (i.isalpha() or i == ""):
                tkinter.messagebox.showerror("Error", "Invalid setting for starting position:\n "
                                                       "must be a single letter or blank")
            break
        for i in range(len(scram_list)):
            rotor = scram_list[i]
            rotor.position = MachineLogic.alphabet.find(orient_list[i])

        # define the machine to be used for encryption
        current_machine = MachineLogic.Enigma(scram_list, refl, plug)

        # do the encryption
        cipher = current_machine.encrypt(plain)
        ciphertext_entry.replace(1.0, END, cipher)

class BuildPlugboard:
    def __init__(self):
        pass
    def build_plugboard(self, map_string):
        length = len(MachineLogic.alphabet)
        new_plug_map = [0] * length
        if len(map_string) != 0:
            pairs = map_string.split()
            for pair in pairs:
                if not (pair[0].isalpha() and pair[2].isalpha() and pair[1] == ":" and len(pair) == 3):
                    tkinter.messagebox.showerror("oh no!", "This is not a valid plugboard:\n invalid entry of settings")
            for pair in pairs:
                index1 = MachineLogic.alphabet.find(pair[0])
                index2 = MachineLogic.alphabet.find(pair[2])
                new_plug_map[index1] = (index2 - index1) % length
                new_plug_map[index2] = (index1 - index2) % length
            new_plug = MachineLogic.Plugboard(new_plug_map)
            return new_plug
        else:
            new_plug = MachineLogic.Plugboard(new_plug_map)
            return new_plug

if __name__ == "__main__":
    root1 = Tk()
    app = MainInterface(root1)
    root1.mainloop()
