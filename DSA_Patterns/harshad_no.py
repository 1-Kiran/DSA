# A Harshad number, also called a Niven number, is a number that is divisible by the sum of its digits.

# Example
# 18 → 1 + 8 = 9
# 18 % 9 = 0

# Therefore, 18 is a Harshad number.

# Correction to the PDF: The PDF states that 42 is not a Harshad number. However, 4 + 2 = 6 and 42 % 6 = 0, so 42 is a Harshad number.

n=18
digits_sum=sum(int(i) for i in str(n))
if n%digits_sum==0:
    print(f"{n} is a Harshad Numbers")
else:
    print(f"{n} is not a Harshad Numbers")