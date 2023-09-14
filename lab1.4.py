my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 74, 'f': 20}
sorted_values = sorted(my_dict.values(), reverse=True)
top_three_values = sorted_values[:3]

topThreeKeys = []
for key, value in my_dict.items():
    if value in top_three_values:
        topThreeKeys.append(key)

print("Три ключа с самыми высокими значениями:", topThreeKeys)
