import pandas
game_is_on = True
words = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row["letter"]:row["code"] for (index, row) in words.iterrows()}

while game_is_on:
    try:
        user_input = input("Enter a word:").upper()
        words_letters = [f"{letter} for:{phonetic_dic[letter]}" for letter in user_input]
    except KeyError:
        print("Only,Letters in the alphabet please.")
    else:
        print(words_letters)
        game_is_on = False



