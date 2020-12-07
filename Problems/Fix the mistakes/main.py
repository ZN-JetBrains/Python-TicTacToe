text = input().split()

for word in text:
    if word.startswith("https://") \
            or word.startswith("http://") \
            or word.lower().startswith("www."):
        print(word)
