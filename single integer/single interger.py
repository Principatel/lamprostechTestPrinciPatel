#Single Integer
num = [1,1,2] #array containing duplicate elements
print("num =",num)
i = 0 #initializing i =0
n = len(num)
for i in range(0,n): #range from 0 to 3
    d=0
    for j in range(0,i):
        if(num[i] == num[j]): #comparing values 
            d=1
            break
        if(d==0):
            print(num[i]) #return distinct element from array
    