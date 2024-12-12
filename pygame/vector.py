command = input("B A V: ")


def calculating(is_add = True):
    A = list(input("введите координаты точки А: ").split(","))     
    B = list(input("введите координаты точки B: ").split(","))
    def f(A,B):
        for i in range(len(A)):
            if A[i] not in "1,2,3,4,5,6,7,8,9,0".split(",") or B[i] not in "1,2,3,4,5,6,7,8,9,0".split(","):
                return(True) 
        return(False)    
        
    while len(A or B) != 2:
        A = list(input("введите координаты точки А(их должно быть две): ").split(","))     
        B = list(input("введите координаты точки B(их должно быть две): ").split(","))

    while f(A,B):
        A = list(input("введите координаты точки А(только цифры): ").split(","))     
        B = list(input("введите координаты точки B(только цифры): ").split(","))

    res = []
    for i in range(len(A)):
        if is_add:
            res.append(int(A[i])+int(B[i]))
        else:
            res.append(int(A[i])-int(B[i]))
    res = sum(res)
    return res

if command == "B":    
    print(calculating())
if command == "A":   
    print(calculating(False))
if command == "V":   
   print(calculating(False))