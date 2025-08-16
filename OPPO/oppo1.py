import sys
from math import inf

n,a,b,c,d = map(int,input().split())

nums = list(map(int,input().split()))

low = min(nums)-1
high = max(nums)+1

def cost(num,target):
    if num == target:
        return 0
    if num<target:
        if b>=2*a:
            return a*(target-num)
        else:
            return (target-num)//2*b+(target-num)%2*min(a,b+c)

    if num>target:
        if d>=2*c:
            return c*(num-target)
        else:
            return (num-target)//2*d+(num-target)%2*min(c,a+d)

costs = [[0 for _ in range(n)] for _ in range(high-low+1)]

mincost = inf
for i in range(high-low+1):
    sum = 0
    for j in range(n):
        costs[i][j] = cost(nums[j],low+i)
        sum += costs[i][j]
    mincost = min(mincost,sum)


print(mincost)

print("hi")