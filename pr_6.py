


num =int(input("enter values"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 6
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")