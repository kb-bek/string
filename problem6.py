text = "My name is Tony"

text2 = text[:int(len(text) / 2)].lower()
text3 = text[int(len(text) / 2):].upper()

print(text2 + text3)