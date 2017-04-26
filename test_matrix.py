from matrix import Matrix

a = Matrix([[1, 2], [3, 4]])
#print(a)

b = Matrix.filled(rows=2, cols=2, value=1)
#print(b)

'''
print(a.data == [[1, 2], [3, 4]]) 
#a.data = [[0,0], [0,0]]          # it does not work, and it shouldn't!'''
print(a.data == [[1, 2], [3, 4]])
internal = a.data                 # PROBLEM HERE
internal[0][0] = 42
print(a.data == [[1, 2], [3, 4]])

print("Should print 1: ", a[0,0])
print("Should print 3: ", a[1,0])
a[0,1] = 42
print(a.data == [[1, 42], [3, 4]])

a = Matrix([[1, 2], [3, 4]])
c = a.T
print(type(c) is Matrix)
print(c.data == [[1, 3], [2, 4]])
a[0, 0] = 42
print(c.data == [[1, 3], [2, 4]])

a = Matrix([[1, 2], [3, 4]])
b = Matrix.filled(2, 2, 1)
d = a + b
print(type(d) is Matrix)
print(d.data == [[2, 3], [4, 5]])

a = Matrix([[1, 2]])
b = Matrix([[3], [4]])
c = a * b
d = b * a
print(type(c) is Matrix)
print(type(d) is Matrix)
print(c.data == [[11]])
print(d.data == [[3, 6], [4, 8]])


a = Matrix([[1, 2], [3, 4]])
e = 2 * a
print(type(e) is Matrix)
print(e.data == [[2, 4], [6, 8]])
