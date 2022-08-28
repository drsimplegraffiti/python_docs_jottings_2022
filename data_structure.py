fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
count=fruits.count('apple')
print(count)

get_orange_index=fruits.index("orange")
print(get_orange_index)

fruits.reverse()
print(f"reversed fruits: {fruits}")

fruits.sort()
print(f"sorted {fruits}")

fruits.pop()
print(f"popped one out: {fruits}")