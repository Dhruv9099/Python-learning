try:
    l=[1,2,3]
    i=int(input("Enter the index: "))
    print(l[i])
except:
    print("Some Error Occured")

finally:
    print("Program Executed !")