# import random
# word_list = ["abrak", "koni", "zaruba"]
# comp_choice = random.choice(word_list)
# list_blanks = []
#
# for j in range(len(comp_choice)):
#     list_app = list_blanks.append("x")
#
# tries =0
#
# while(True):
#     guess = input("Guess a letter").lower()
#
#     for i in range(len(comp_choice)):
#         letter_in_compchoice = comp_choice[i]
#         if letter_in_compchoice == guess:
#             list_blanks[i] = letter_in_compchoice
#
#     if guess not in comp_choice:
#         tries += 1
#         if tries == 8:
#             print("You used all attempt(")
#             break
#     print(list_blanks)
#
#     if "x" not in list_blanks:
#         print("You win!")
#         break

# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# lives = 6
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# print(f'Pssst, the solution is {chosen_word}.')
#
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     for position in range(word_length):
#         letter = chosen_word[position]
#
#         if letter == guess:
#             display[position] = letter
#
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     print(stages[lives])

# def greet(name, location):
#     print(f"{name}")
#     print(f"am in {location}")
#     print("unstoppable!")
#
# greet(location= "Warzsaw", name = "Yana")
#

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if (number % i == 0):
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
#
# def yana(new_text, new_shift):
#     cifer_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = position + shift
#         cifer_text += alphabet[new_position]
#     print((cifer_text))
# yana(new_text = text, new_shift = shift)
#
#
# def decode()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         # TODO-3: What happens if the user enters a number/symbol/space?
#
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
# from art import logo
#
# print(logo)
#
#
# should_end = False
# while not should_end:
#
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#
#     shift = shift % 26
#
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart == "no":
#         should_end = True
#         print("Goodbye")

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# dictionary = {}
# print(dictionary)
# dictionary["1"] = "one"
# dictionary["2"] = "two"
#
# print(dictionary["1"])
# for i in dictionary:
#     print(dictionary[i])

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
#
# print(order["main"][2])

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
#
#
# print(dict["a"])








