alphabet = "abcdefghijklmnopqrstuvwxyz"

# This class represents all five different rotors in the Enigma Machine
class Rotor():
    def __init__(self, mapping, step_position=[0], position=0):
        self.position = position  # An integer value which represents the position of the rotor
        self.m = mapping  # Maps each character to another character
        self.reverse_map = self.reverse_mapping()  # list that represents base mapping of rotor in reverse direction
        self.step_position = step_position  # tuple containing positions after the next rotor has turned

    # Works out the reverse of the origin mapping given when a chareacter is passed.
    def reverse_mapping(self):
        reverse_map = [0]*len(alphabet)
        for i in range(len(alphabet)):
            result = self.m[i]
            new_map = len(alphabet) - result
            reverse_map[(result+i) % len(alphabet)] = new_map
        return reverse_map

    # Passes a single character as an integer and use that to work out encryption going forward
    def forward_encryption(self, integer):
        forward_wiring_pref = self.m[self.position:] + self.m[:self.position]
        temp = (integer + forward_wiring_pref[integer]) % len(alphabet)
        return temp

    # Passes a single character as an integer and use that to work out encryption going backward
    def backward_encryption(self, integer):
        backward_wiring_pref = self.reverse_map[self.position:] + self.reverse_map[:self.position]
        temp = (integer + backward_wiring_pref[integer]) % len(alphabet)
        return temp

# This class allows us to swap the pairs of characters
class SwapPair:
    def __init__(self, mapping):
        self.m = mapping

    def encrypt(self, integer):
        temp = (integer + self.m[integer]) % len(alphabet)
        return temp


class Reflector(SwapPair):
    def __init__(self, mapping):
        SwapPair.__init__(self, mapping)
        self.check = self.valid_Reflector()

    # Checks that the reflector swaps the correct pairs of characters
    def valid_Reflector(self):
        check = True
        for i in range(len(self.m)):
            maps_to = (i + self.m[i]) % len(self.m)
            if (maps_to + self.m[maps_to]) % len(self.m) != i:
                check = False
        return check


class Plugboard(SwapPair):
    def __init__(self, mapping):
        SwapPair.__init__(self, mapping)
        self.check = self.valid_Plugboard()

    def valid_Plugboard(self):
        check = True
        for i in range(len(self.m)):
            if self.m[i] != 0:
                maps_to = (i + self.m[i]) % len(self.m)
                if (maps_to + self.m[maps_to]) % len(self.m) != i:
                    check = False
        return check

# This class takes all the features from the functions above and stores it all one enigma machine
class Enigma:
    def __init__(self, scrambler_list, reflector=Reflector([0]*26), plugboard=Plugboard([0]*26)):
        self.s = scrambler_list
        self.ref = reflector
        self.plug = plugboard

    def increment_Rotors(self):
        for i in range(len(self.s)):
            self.s[i].position = (self.s[i].position + 1) % len(alphabet)  # increment position of s[i]
            if self.s[i].position not in self.s[i].step_position:  # unless this means moving past push point
                break

    def forward_Rotor(self, int):
        for i in range(len(self.s)):
            int = self.s[i].forward_encryption(int)
        return int

    def backwards_Rotor(self, int):
        for i in range(len(self.s)):
            int = self.s[len(self.s)-1 - i].backward_encryption(int)
        return int

    def encrypt(self, text):
        # Applies encryption algorith on only plain text
        returnedTxt = ""
        for cipher in text:
            self.increment_Rotors()
            starting_int = alphabet.find(cipher)  # map the letter to its equivalent integer in the alphabet
            if cipher == " ":
                returnedTxt += " "
            elif starting_int == -1:
                returnedTxt += "*"
            else:
                int = self.plug.encrypt(starting_int)  # plugboard forward
                int = self.forward_Rotor(int)  # Rotor(s) forward
                if self.ref.m != [0]*len(alphabet):  # not null
                    int = self.ref.encrypt(int)  # reflector
                    int = self.backwards_Rotor(int)  # scramblers backward
                    int = self.plug.encrypt(int)  # plugboard backward
                    returnedTxt += alphabet[int]  # map from integer back to letter using alphabet, add to returnedTxt str
                else:
                    returnedTxt += alphabet[int]  # map from integer back to letter using alphabet, add to returnedTxt str
        return returnedTxt

# Rotors, reflectors and Plugboards To Be Used:-
        # Example rotor and reflectors taken from this site: http://users.telenet.be/d.rijmenants/en/enigmatech.htm
rotor_I = Rotor([4, 9, 10, 2, 7, 1, 23, 9, 13, 16, 3, 8, 2, 9, 10, 18, 7, 3, 0, 22, 6, 13, 5, 20, 4, 10], [17])
rotor_II = Rotor([0, 8, 1, 7, 14, 3, 11, 13, 15, 18, 1, 22, 10, 6, 24, 13, 0, 15, 7, 20, 21, 3, 9, 24, 16, 5], [6])
rotor_III = Rotor([1, 2, 3, 4, 5, 6, 22, 8, 9, 10, 13, 10, 13, 0, 10, 15, 18, 5, 14, 7, 16, 17, 24, 21, 18, 15], [23])
rotor_IV = Rotor([4, 17, 12, 18, 11, 20, 3, 19, 16, 7, 10, 23, 5, 20, 9, 22, 23, 14, 1, 13, 16, 8, 6, 15, 24, 2], [10])
rotor_V = Rotor([21, 24, 25, 14, 2, 3, 13, 17, 12, 6, 8, 18, 1, 20, 23, 8, 10, 5, 20, 16, 22, 19, 9, 7, 4, 11], [0])
rotor_VI = Rotor([9, 14, 4, 18, 10, 15, 6, 24, 16, 7, 17, 19, 1, 20, 11, 2, 13, 19, 8, 25, 3, 16, 12, 5, 21, 23],
                [0, 14])
rotor_VII= Rotor([13, 24, 7, 4, 2, 12, 22, 16, 4, 15, 8, 11, 15, 1, 6, 16, 10, 17, 3, 18, 21, 9, 14, 19, 5, 20],
                 [0, 14])
rotor_VIII = Rotor([5, 9, 14, 4, 15, 6, 17, 7, 20, 18, 25, 7, 3, 16, 11, 2, 10, 21, 12, 3, 19, 13, 24, 1, 8, 22],
                  [0, 14])
reflector_B = Reflector([24, 16, 18, 4, 12, 13, 5, 22, 7, 14, 3, 21, 2, 23, 24, 19, 14, 10, 13, 6, 8, 1, 25, 12, 2, 20])
reflector_C = Reflector([5, 20, 13, 6, 4, 21, 8, 17, 22, 20, 7, 14, 11, 9, 18, 13, 3, 19, 2, 23, 24, 6, 17, 15, 9, 12])
rotor_tester = Rotor([0] * 26)
plug_default = Plugboard([0] * 26)
possible_scramblers = [rotor_I, rotor_II, rotor_III, rotor_IV, rotor_V, rotor_VI, rotor_VII, rotor_VIII, rotor_tester]
possible_reflectors = [reflector_B, reflector_C]
main_scrambler_list = [rotor_I, rotor_II, rotor_III]
default_machine = Enigma(possible_scramblers,  reflector_B, plug_default)
