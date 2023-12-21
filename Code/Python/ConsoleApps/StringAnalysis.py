#Alright lets see if I remember anything about Python

prompt = input("You: ");

length = len(prompt);

wordcount = prompt.split()
count = len(wordcount)

sCharacters = 0
sCharacterslist = ["!","?",",","~","`"]

for x in prompt:
    if x in sCharacterslist:
        sCharacters += 1
        continue

print("Characters: ",length)
print("Words: ",count)
print("Special Characters: ",sCharacters)