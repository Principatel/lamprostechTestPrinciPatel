#The sum of two elements
num = [2,4,5] #Array of integer num
target = 9 #sum of two in elements in num such that its value is equal to target value
i = 0 #initializing i=0
for i in num: 
    for j in range(0,num[i]):
        if(num[i] + num[j] == target):  #sum of num[i] and num[j] should be equal to value of target
            print([i,j]) #return the indices whose sum is equal to target
            #print([num[i],num[j]])  #print the value of num[i] & num[j] whose sum is equal to target