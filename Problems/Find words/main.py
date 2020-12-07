words = input().split()
searched_words = [word for word in words if word.endswith("s")]
output = " ".join(searched_words)
output = output.replace(" ", "_")
print(output)
