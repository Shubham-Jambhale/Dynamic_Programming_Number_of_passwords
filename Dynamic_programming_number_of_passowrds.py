def num_passwords(nums) :
    length=len(nums)
    #matrix initialization
    matrix=[0]*(length+1)
    matrix[0]=1
    i=1
    #iterating over the array to check no of passwords formed
    while i < (length+1):
        #for removing duplicates
        common=0
        for j in range(i-1,0,-1):
            if nums[i-1]==nums[j-1]:
                common=matrix[j-1]
                break  
    #there are always 2^n possible combinations of passowrds and hence we are multiplying by 2 
        matrix[i]= 2 * matrix[i-1]-common
        i+=1
    return matrix[-1]-1