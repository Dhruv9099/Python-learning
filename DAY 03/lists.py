marks =[30,50,60]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])

#ordered collection 
#add  element to list
list.append(marks,40)
marks.append(80)

print(marks)


#insert alphabets and numberic also
marks.insert(1,'ABBLE')
print(marks)

#negative index  
print(marks[-2])
print(marks[len(marks)-1]) #positve index
print(marks[4-5])            #positive index

if 40 in marks: 
    print("yes 40 is  present")
else:
    print("no")

if "AB" in "ABBLE":
    print("AB is  present")

# Pirnt  the elements from a particular index till end of the
    print(marks[0:])

# JUMP index
A = [1,2,3,4,5,6,7,8,9,10]
print("print A",A)
print("A LIST IN ODD ",A[0:10:2])  # odd
print("A LIST IN EVEN", A[1:10:2])  # even
print("3 step jump" ,A[1:10:3])  # even

print("even reverse", A[-1:-10:-2])  # even reverse
#Jump  2 means take every second element


list= [i*i for i in range(10)]

print(list)

list=[i*i for i in range(10) if
    i%2==0]
print(list)




l= [11,45,1,2,6,4]
print("l list",l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(4))
m=l
m[0]=100
print("m list",m)
print("l list",l)


#with copy met#hod
n= l.copy()
n[0]=200
print(m)
print(l)
print(n)


# extend
m=[900,1000,8222]
l.extend(m)
print("l", l)
print("m", m)
k= m+l
print("K" , k)