if True:
    print("if condition execute")
else:
    print("else condition execute")

price = 343
if price > 100:
    print("price is greater than 100")
elif price < 100:
    print("price is less than 100")
else:
    print("price is equal to 100 ")


price = 50
quantity = 5
if price*quantity < 500:
    print("price*quantity is less than 500")
    print("price =", price)
    print("quantity =", quantity)


def main():
    x, y = "2", "2"
    if (x > y):
        print("x is greater than y")
    elif(x == y):
        print("x and y are equal.")
    else:
        st= ("x isnot greater than y")
        print(st)

main()

def main():
    a, b = "2", "2"
    st=("a is less than y") if (a<b) else ("a is not less than y")
    print(st)

main()
