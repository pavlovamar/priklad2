import sys

class Text:
    def __init__(self):
        self.__text__ = None
        self.__vowels__ = 0
        self.__consonants__ = 0
        self.__vowel__ = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
        self.__vowels_with_diacritics__ = [193, 201, 205, 211, 218, 221, 225, 233, 237, 243, 250, 253, 282, 283, 366, 367]
        self.__consonants_with_diacritics__ = [268, 269, 270, 271, 327, 328, 344, 345, 352, 353, 356, 357, 381, 382]

    def count_letters(self):
        if self.__text__ == None:
            return print("There is no data.")
        for letter in self.__text__:
            if ord(letter) in self.__vowel__ or ord(letter) in self.__vowels_with_diacritics__:
                self.__vowels__ += 1
            elif ord(letter) in self.__consonants_with_diacritics__:
                self.__consonants__ +=1
            elif (ord(letter)>=65 and ord(letter)<=90) or (ord(letter)>=97 and ord(letter)<=122):
                self.__consonants__ += 1

    def load(self,adress):
        try:
            with open (adress, 'r', encoding = "utf-8") as input:
                self.__text__ = list(input.read())
        except FileNotFoundError:
            sys.exit ("The file has not been found.")
        except PermissionError:
            sys.exit ("You don't have the permission to open this file.")
        except IOError:
            sys.exit ("An error occured while opening the input file.")
        except KeyError:
            sys.exit ("An error occured while reading the input file.")
        except:
            sys.exit ("Something went wrong.")
    def save(self,adress):
        with open (adress, 'a', encoding = "utf-8") as output:
            output.write('\n\n'f"The are {self.__vowels__} vowels and {self.__consonants__} consonants in the text.")
    
object = Text()
object.load("input.txt")
object.count_letters()
object.save("input.txt")
