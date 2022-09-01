try:
    def cubes():
        n = int(input("Enter the number of elements in list: "))
        list_num = [1]
        for i in range(n):
            num = int(input("Enter a number: "))
            list_num.append(num)
        list_num.pop(0)
        print("Input: " + str(list_num))
        for x in list_num:
            res = (x, x**3)
            print(res)
    cubes()
except ValueError:
    print("Enter number of elements.")
except:
    print("Enter correctly")