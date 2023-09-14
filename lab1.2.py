text = input( "Введите текст: ")
vowels = ['a','e','i','o','u']
vowelCount = 0
consonantCount = 0
vowelList = []
for char in text:
    if char.isalpha():
        if char.lower() in vowels:
            vowelCount+=1
            if char.lower() not in vowelList:
                vowelList.append(char.lower())
            else :
                consonantCount +=1

if vowelCount == consonantCount:
    print("Гласные буквы: ",vowelList)
else:
    print("Количество гласых букв: ", vowelCount)
    print ( "Количество согласных букв:", consonantCount)

wordCount = len(text.split())
print("Количество слов в текте: ", wordCount)
