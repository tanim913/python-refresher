import sys
import timeit

list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)

print(sys.getsizeof(list1), "bytes")
print(sys.getsizeof(tuple1), "bytes")

print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))
