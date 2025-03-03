n = int(input('Enter your number:'))
for i in range(2,n):
    if (n %2)==0:
     print('Not a prime number')
     break
    else:
     print('Yes a prime number')