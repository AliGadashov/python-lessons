""""

x = int(input("Enter a number 1: "))  #string input
y = int(input("Enter a number 2: "))

print(type(x))
print(type(y))

total = x + y

print(type(total))

print("The total is: ", total)

"""
#######################################################################################################
"""
# Example of types
x = "100"  # string
y = 50    # integer
z = 25.5  # float
a = True  # boolean
b = None  # NoneType
c = [1, 2, 3]  # list
d = (4, 5, 6)  # tuple
e = {7, 8, 9}  # set
f = {"key": "value"}  # dictionary
g = b"byte string"  # bytes
h = bytearray(b"byte array")  # bytearray
i = complex(1, 2)  # complex number
j = range(5)  # range object
k = frozenset([10, 11, 12])  # frozenset
l = memoryview(b"memory view")  # memoryview
m = lambda x: x * 2  # function
n = type(x)  # type object
o = Exception("error")  # exception
p = iter([1, 2, 3])  # iterator
q = map(lambda x: x * 2, [1, 2, 3])  # map object
r = filter(lambda x: x > 1, [1, 2, 3])  # filter object
s = zip([1, 2], ['a', 'b'])  # zip object
t = slice(1, 3)  # slice object
u = property(lambda self: "property")  # property object
v = super()  # super object
w = Ellipsis  # Ellipsis object
x = NotImplemented  # NotImplemented object
y = __import__('math')  # module object
z = type  # type object
"""

 