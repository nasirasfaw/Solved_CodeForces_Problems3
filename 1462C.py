t = int(input())
for _ in range(t):
    x = int(input())
    
    a = list(range(9, 0, -1))
    if x > 45:
        print(-1)
    else:
        nums = []
        for i in range(len(a)):
            nums.append(a[i])
            if sum(nums) > x:
                break
        if sum(nums) > x:
            nums[-1] = x - sum(nums[:len(nums)-1])
        nums.sort()
        nums1 = [str(d) for d in nums]
        nums1 = "".join(nums1)
        print(int(nums1))
