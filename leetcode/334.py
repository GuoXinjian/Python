def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    t=0
    i=3
    for n in nums:
        if n >=t:
            i-=1
            if i==0:
                return True
        else:
            i=3
        t=n
    return False

nums=[2,1,5,0,4,6]
print(increasingTriplet(nums))