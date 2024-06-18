
 
def Hanoi(n , source, destination, auxiliary):
    if n==1:
        print (source,"----->",destination)
    else:
        Hanoi(n-1, source, auxiliary, destination)
        Hanoi(1, source, destination, auxiliary)
        Hanoi(n-1, auxiliary, destination, source)
    
#Hanoi(3,'A','B','C') 

def Hanoicount(n):
    if n==1:
        return 1
    else:
        step_count1 = Hanoicount(n-1)
        step_count2 = Hanoicount(1)
        step_count3 = Hanoicount(n-1)

        count = step_count1+step_count2+step_count3
        return count
    
        #return 2*Hanoicount(n-1)+1
   
#Hanoicount(7)

def hanoipuzzle(n):
    print("here are the", Hanoicount(n), "step of hanoi puzzel of", n , "disks")
    Hanoi(3,'A','C','B') 

hanoipuzzle(3)
