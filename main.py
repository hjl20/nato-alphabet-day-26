import pandas


def nato_alphabetize():
    file = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_alphabet = {row.letter:row.code for (index, row) in file.iterrows()}

    user_word = input("Enter a word to translate into the NATO alphabet: ")

    nato_word = [nato_alphabet[letter.upper()] for letter in list(user_word)]

    print(nato_word)


nato_alphabetize()
