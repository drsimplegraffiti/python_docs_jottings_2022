print("\nhello world")
print(3 * "hi")

word="Punjabi"
print(f"the index is : {word[2]}" )
print(f"the negative index is : {word[-3]}" )
print(f"the sliced index is : {word[1:2]}" ) #start from index 1 and pick index 2 and exclude the rest of the words

# length of words
print(f"the length of words is : {len(word)}")



################################################################
#WORKING WITH LIST
animals = ["monkeys", "tiger", "lions"]
animals.append("cat")
print(animals)
print(f"the second animal on the list is : {animals[1]}")
print(f"slice the list of animals: {animals[2:3]}") #start from index 2, pick three and omit the rest
animals[1:2] = ["bear"]
print(f"replace the index 1 animal :{animals}")