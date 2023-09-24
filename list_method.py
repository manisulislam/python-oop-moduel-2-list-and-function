numbers= [41,52,65,85,96,49]
numbers.append(85)
print(numbers)

numbers.insert(2, 965)
print(numbers)

if 85 in numbers:
    numbers.remove(85)
print(numbers)

last = numbers.pop()
print(last, numbers)

if 965 in numbers:
    index= numbers.index(965)
    print(index)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)