print('enter n blocks')
n = int(input())
print('enter m blocks')
m = int(input())
print('enter piece k')
k = int(input())


if (k%m==0 or k%n==0) and (k<n*m):
   print('yes, enjoy your choco')
else:
   print('no, try one more time')
