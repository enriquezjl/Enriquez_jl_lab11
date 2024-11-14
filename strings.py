combined = []

print("Enter 10 words:")
index = 1
while index < 11:
    word = input(f"Enter word {index}: ")
    combined.append(word)
    index += 1
 
print("/nWords and their lengths:")
for i, word in enumerate(combined, 1):
    print(f"Word {i}: {word}, Length: {len(word)}")
    
    