sentence='Python is a versatile, high-level programming language known for its simplicity, readability, and powerful libraries, making it a popular choice for web development, data science, automation, and artificial intelligence. 🚀'

split_words= sentence.split()
total_words= len(split_words)
reverse_word= split_words[::-1]
print(f'total word in this \"{sentence}\" sentence is\n \"{total_words}\"')
print(reverse_word)