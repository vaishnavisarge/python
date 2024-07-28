def kidsWithCandies():
    candies=[2,3,5,1,3]
    extracandies=3
    max_candy=max(candies)
    for i in range(len(candies)):
        if candies[i]+extracandies>=max_candy:
            candies[i]=True
        else:
            candies[i]=False
    return candies
print(kidsWithCandies())