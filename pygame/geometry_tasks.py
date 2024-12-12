
def distance():
    A = list(input("введите координаты точки А: ").split(" "))     
    B = list(input("введите координаты точки B: ").split(" "))
    K1 = (int(B[0]) - int(A[0]))**2
    K2 = (int(B[1])- int(A[1]))**2
    G = (K1+K2)**0.5
    return G



def triangle_square():
    A = list(map(int,(input("введите координаты точки А: ").split(" "))))     
    B = list(map(int,(input("введите координаты точки B: ").split(" "))))
    C = list(map(int,(input("введите координаты точки C: ").split(" "))))
    A_B = [B[0]-A[0],B[1]-A[1]]
    A_C = [C[0]-A[0],C[1]-A[1]]
    return abs((A_B[0]*A_C[1]-A_C[0]*A_B[1])/2)


def E():
    A = list(map(int,(input("введите координаты точки А: ").split(" "))))     
    B = list(map(int,(input("введите координаты точки B: ").split(" "))))
    if (A[0]*B[0]+A[1]*B[1]) == 0:
        return 2
    if (A[0]*B[1]-A[1]*B[0]) == 0:
        return 1 
    return 0




def F():
    A = list(map(int,(input("введите координаты точки А: ").split(" "))))     
    B = list(map(int,(input("введите координаты точки B: ").split(" "))))
    C = list(map(int,(input("введите координаты точки C: ").split(" "))))     
    D = list(map(int,(input("введите координаты точки D: ").split(" "))))
    V_A = [B[0]-A[0], B[1]-A[1]]
    V_B = [D[0]-C[0], D[1]-C[1]]
    if (V_A[0]*V_B[1]-V_A[1]*V_B[0]) == 0 or (V_A[0]*V_B[1]-V_A[1]*V_B[0]) <=0 or (V_A[0]*V_B[0]+V_A[1]*V_B[1]) < 0:
  
        return "NO"
    return "YES"
print(F())
    