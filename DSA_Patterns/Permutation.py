def permutation(s, current="", l=None):
    if l is None:
        l = []

    if len(s) == 0:
        l.append(current)
        return l

    for i in range(len(s)):
        ch = s[i]
        remaining = s[:i] + s[i+1:]
        permutation(remaining, current + ch, l)

    return l

print(permutation("abc"))


# class Solution(object):
#     def checkInclusion(self, s1, s2):

#         if len(s1) > len(s2):
#             return False

#         count_s1 = {}
#         count_s2 = {}

#         # Count s1
#         for ch in s1:
#             count_s1[ch] = count_s1.get(ch, 0) + 1

#         # First window
#         for ch in s2[:len(s1)]:
#             count_s2[ch] = count_s2.get(ch, 0) + 1

#         if count_s1 == count_s2:
#             return True

#         left = 0

#         # Slide window
#         for right in range(len(s1), len(s2)):

#             # Remove left character
#             old = s2[left]
#             count_s2[old] -= 1

#             if count_s2[old] == 0:
#                 del count_s2[old]

#             left += 1

#             # Add new right character
#             new = s2[right]
#             count_s2[new] = count_s2.get(new, 0) + 1

#             if count_s1 == count_s2:
#                 return True

#         return False