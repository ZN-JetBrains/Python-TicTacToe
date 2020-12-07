text = input()

processed_text = ""

for char in text:
    if char.islower():
        processed_text += char
    else:
        if char == text[0]:
            processed_text += char.lower()
        else:
            processed_text += "_" + char.lower()

print(processed_text)
