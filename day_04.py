import inflect

p = inflect.engine()
number = int(input('Enter your number:'))
word = p.number_to_words(number).upper()
print(word) 
