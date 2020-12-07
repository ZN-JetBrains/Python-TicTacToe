words = input().split()
stripped_words = [word.strip(",.!?") for word in words]

text = ""
for word in stripped_words:
    text += word + " "

text = text.lower().strip()
print(text)
