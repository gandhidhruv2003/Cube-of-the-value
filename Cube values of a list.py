import numpy as np
try:
    def cube_of_values():
        n = int(input("Enter the number of elements in list: "))
        l = []
        for i in range(n):
            num = int(input("Enter a number: "))
            l.append(num)
            
        mat = np.array(l)
        print(mat)
        mat_cube = mat**3
        print(mat_cube)
    cube_of_values()
except ValueError:
    print("Enter a string")
except:
    print("Enter correctly")
