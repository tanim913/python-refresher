list1 = [1, 2, 3]
print(list1)

list1.append(4)
print(list1)

# inserting in specific position
list1.insert(2, 7)
print(list1)

# .pop() removes the last item and also returns it
last_item = list1.pop()
# print(last_item)

ls = list()
ls.append(last_item)
print(ls)

list1.append(7)
print(list1)
# .remove(x) only removes one element of the list which is the first one
list1.remove(7)
print(list1)

ls.clear()
print(ls)

list1.reverse()
print(list1)

list1.sort()
print(list1)

# accesing elements from behind
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
# print(list1[-5]) out of bounds

# sorting without changing element in places

new_list = sorted(list1)
print(new_list)

l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l3[1:5])
print(l3[::2])
print(l3[::-1])
print(l3[::-1] + l3[1:])


# copying list
l4 = [1, 2, 3]
l5 = l4
l5.append(4)
# l4 also appends new elements because the starting pointer of l4 becomes the same pointer after assigning it to l5
print(l4)
# makes actual copy with different pointers
l5 = l4.copy()
l5 = list(l4)
l5 = l4[:]

# list comprehension
l6 = [1, 2, 3, 4]
l7 = [i*i for i in l6]
print(l7)
