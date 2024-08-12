def reverseVowels(s):
    s=list(s)
    vowels=('a','e','i','o','u','s','I','O','U','E')
    i=0
    j=len(s)-1
    while i<j:
        if s[i] in vowels and s[j] in vowels:
            s[i],s[j]= s[j],s[i]
            i=i+1
            j=j-1
        if s[i] not in vowels:
            i+=1
        if s[j] not in vowels:
            j-=1
    return "".join(s)
print(reverseVowels('hello'))

