def lcs(str1,str2,m,n):
    if(m==0 or n==0):
        return 0
    if(str1[m]==str2[n]):
        return 1 + lcs(str1,str2,m-1,n-1)
    else:
        return max(lcs(str1,str2,m,n-1),lcs(str1,str2,m-1,n))

str1 = 'bhaskar'
str2 = 'askar'
print(lcs(str1,str2,len(str1)-1,len(str2)-1))