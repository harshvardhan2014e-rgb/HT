lst = ['apple', 'banana', 'mango', 'grape', 'Guava']

print("Length of the list is: ", len(lst))
print("First element of the list is: ", lst[0])
print("Last element of the list is: ", lst[-1])

lst.append('orange')
print("List after appending an element: ", lst)

lst.remove('banana')
print("List after removing an element: ", lst)

lst.sort()
print("List after sorting: ", lst)

lst.pop(1)
print("List after popping an element: ", lst)

lst.reverse()
print("List after reversing: ", lst)

print("Multiplying the list by 2: ", lst * 2)

lst = lst[:4]
print("Sliced list: ", lst)

lst.clear()
print("List after clearing: ", lst)