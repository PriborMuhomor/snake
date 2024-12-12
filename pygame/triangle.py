
def sort(array):

    for j in range(len(array)):
        swapped = False

        for i in range(len(array)-1):
        
            if array[i]<array[i+1]:
            
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                swapped = True
        if not swapped:
            
            break
    return array        

def is_positive(array):
    for i in range(len(array)):
        if array[i] <= 0:
            return False
    return True    
            
class TriangleChecker:
    def __init__(self, sides = [0,0,0]):
        self.sides = sort(sides)



    def istriangle(self):
       try:
        if not is_positive(self.sides):
            print("только положительные числа")      
        elif (self.sides[1]+self.sides[2]) >= self.sides[0]:
            print("получилось")
        else:
             print("не получилось")
       except TypeError:
           print("только числа")

Triangle = TriangleChecker([30,20,40])  

Triangle.istriangle()




