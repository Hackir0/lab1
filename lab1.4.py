my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted_values = sorted(my_dict.values(), reverse=True)
top_three_values = sorted_values[:3]

top_three_keys = []
for key, value in my_dict.items():
    if value in top_three_values:
        top_three_keys.append(key)

print("Три ключа с самыми высокими значениями:", top_three_keys) # ['b', 'e', 'c']