import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# letter = True

# while letter:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         print(output_list)
#         letter = False
#     except KeyError:
#         print("Sorry only letters are allow")
#         letter = True

def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters are allow")
        generate_nato()
    else: 
        print(output_list)
generate_nato()

