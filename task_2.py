s = input()
dictionary = dict()
sheriff = {'s': 1, 'h': 1, 'e': 1, 'r': 1, 'i': 1, 'f': 2}
for simb in s:
    dictionary[simb] = 0
for simb in sheriff:
    dictionary[simb] = 0
for simb in s:
    dictionary[simb] += 1
count = -1
for i in sheriff:
    if count == -1:
        count = int(dictionary[i] / sheriff[i])
    else:
        count = min(count, int(dictionary[i] / sheriff[i]))
print(count)