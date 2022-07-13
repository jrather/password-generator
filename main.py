#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pword_lett = ""
for index in range(0, nr_letters):
  random_number = random.randint(0, 51)
  pword_lett += letters[random_number]
#print(pword_lett)

pword_sym = ""
for index in range(0, nr_symbols):
  random_number = random.randint(0, 8)
  pword_sym += symbols[random_number]
#print(pword_sym)
#total_numbers += nr_symbols

pword_num = ""
for index in range(0, nr_numbers):
  random_number = random.randint(0, 9)
  pword_num += numbers[random_number]
#print(pword_num)
p_total = (pword_num + pword_sym + pword_lett)
p_rand = random.sample(list(p_total), len(p_total))
print(f"Your password is {pword_lett}{pword_sym}{pword_num}")
p_rand_str = ''.join(random.sample(p_rand, len(p_rand)))
print(f"Your random password is {p_rand_str} ")


#total_numbers += nr_numbers
#print(total_numbers)