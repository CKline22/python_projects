def hello():
    print("Hello, User")

def pack(a,b,c):
    return [a,b,c]

def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(my_lst)):
            if i ==0:
                print(f"first i eat {my_lst[0]}")
            else:
                print(f"next i eat {my_lst[i]}")


hello()
print(pack("a","b","c"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["steak", "burger", "icecream"])