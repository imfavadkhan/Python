import sys
number = int(input("Enter a number to write a table :"))
for i in range (1 ,11):
    print(f"{number} X {i} = {number * i}")

a = 12345
b = 12345567788654356667453
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(id(a))
print(id(b))