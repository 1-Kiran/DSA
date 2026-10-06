def permutation(s,current="",l=[]):
    if len(s)==0:
        l.append(current)
        return
    for i in range(len(s)):
        ch=s[i]
        remaining=s[:i]+s[i+1:]

        permutation(remaining,current+ch,l)
    return l

print(permutation("abc"))