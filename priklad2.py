import sys

def compare_ASCII(line):
    '''Compares ASCII code of every letter in the file with list of vowels and consonants in order
    to count how many vowels and consonants are in the text'''
    vowel_count = 0
    consonant_count = 0
    vowels = [65, 69, 73, 79, 85, 89, 97, 101, 105, 111, 117, 121]
    vowels_with_diacritics = [193, 201, 204, 205, 211, 217, 218, 221, 225, 233, 236, 237, 243, 279, 350, 253]
    letters_with_diacritics = [268, 269, 270, 271, 327, 328, 344, 345, 352, 353, 356, 357, 381, 382]
    for letter in line:
        if ord(letter) in vowels or ord(letter) in vowels_with_diacritics:
            vowel_count += 1
        elif ord(letter) in letters_with_diacritics:
            consonant_count += 1
        elif (ord(letter)>65 and ord(letter)<90) or (ord(letter)>97 and ord(letter)<122):
            consonant_count += 1
    return vowel_count, consonant_count

def export(output):
    with open ("input.txt", 'a', encoding = "utf-8") as out:
        out.write('\n\n'f"There are {output[0]} vowels and {output[1]} consonants in the text.")

def load():                         
    try:
        with open ("input.txt", 'r', encoding = "utf-8") as input:
            line = list(input.read())
    except FileNotFoundError:
        sys.exit ("The file has not been found")
    except PermissionError:
        sys.exit ("You don't have the permission to open this file.")
    except IOError:
        sys.exit ("An error occured while opening the file with input data. Check if the file is in same directory as the script.")
    except KeyError:
        sys.exit ("An error ocuured while reading the input data. Check if the file contains the required attributes.")
    except:
        sys.exit ("Something went wrong.")
    return line

line = load()
result = compare_ASCII(line)
export(result)
