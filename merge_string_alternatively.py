def alternative_string(s1,s2):
    i=0
    j=0
    result=""
    while(i<len(s1) and j<len(s2)):
        result+=s1[i]+s2[j]
        i=i+1
        j=j+1
    return result
s1=input("Enter string 1:")
s2=input("Enter string 2:")
print(alternative_string(s1,s2))