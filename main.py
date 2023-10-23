student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# My solution
# with open("nato_phonetic_alphabet.csv") as nato_file:
#     nato_list = nato_file.readlines()
#     print(nato_list)
#     nato_dictionary = {letter.split(",")[0]: letter.split(",")[1].strip() for letter in nato_list if 'letter' not in letter}
#     print(nato_dictionary)

# Video solution
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dictionary)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# My solution
# user_input = input("Enter a word: ")
# nato_user_input = [code for (letter, code) in nato_dictionary.to if letter in user_input]
# print(nato_user_input)

# Video solution
word = input("Enter a word: ").upper()

output_list = [nato_dictionary[letter] for letter in word]
print(output_list)
