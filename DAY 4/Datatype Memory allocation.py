# date 08/3/2024
# The sys.getsizeof() Built-in Function The standard library's sys module provides the [getsizeof()]
# The size of an object in bytes
import sys

# Integer size
sys.getsizeof(int())       # Output: 28
print(sys.getsizeof(int()))

i=int(0)
print(i,type(i))         # Output: 0 <class
print('Integer Size with 0: ',sys.getsizeof(i), 'Bytes')   # Output: Integer Size 
i =1
print('Integer Size with 1: ',sys.getsizeof(i), 'Bytes')       # Output: Integer Size 1 Bytes

# Float size
f=float()
print("Float Size: ",sys.getsizeof(f), "Bytes")               # Output: Float Size:  24 Bytes
f=5.5                                                        # Reason: A float is stored as a mantissa and exponent.         
print("float value with 5.5:" ,sys.getsizeof(5.5))            