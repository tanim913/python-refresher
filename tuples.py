# tuples can not be changed like lists

t1 = (1,)
print(type(t1))
l1 = tuple([1, 2, 3, 4, 5, 6])
print(type(l1))
print(l1.count(3))
print(l1.index(3))

# unpacking tuple
# size of tuple should be equal to number of elements
my_tuple = ("Tanim", 25, "Dhaka")
name, age, city = my_tuple

nums = (1, 2, 3, 4, 5)
i1, *i2, i3 = nums
print(i2)
