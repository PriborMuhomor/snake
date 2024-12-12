import math
def task_B():
    A = list(input("введите координаты точки А: ").split(","))

    result = math.atan2(int(A[1]),int(A[0]))
    if result>0:
        result+= 2*math.pi
    print(result)
def task_C():
    A = list(input("введите координаты точки А: ").split(","))
    B = list(input("введите координаты точки B: ").split(","))
    length_B = vector_length(B)
    length_A = vector_length(A)
    cos_AB = dot_product(A,B)/(length_A*length_B)
    cos_AB = max(min(1,cos_AB),-1)
    print(math.acos(cos_AB))
def dot_product(V1,V2):
     
     return(int(V1[0])*int(V2[0])+int(V1[1])*int(V2[1]))
     
     

def vector_length(v):
        return sum(int(x) ** 2 for x in v) ** 0.5

task_C()