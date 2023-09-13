string = "fefwef"
numberOfVowels = 0
numberOfConsonants = 0
for i in string:
    if (i == 'a' or i == 'A' or 'i' or 'I' or
            i == 'e' or i == 'E' or i == 'y' or i == 'Y'
            or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
        numberOfVowels += 1
    else:
        numberOfConsonants += 1

print("Гласные = ", numberOfVowels, "Согласные", numberOfConsonants)
