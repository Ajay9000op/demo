n=11
rev=0
c=n
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)
n=c
if n!=c:
    count=0 
    for i in range(1,n+1):
        if n%i==0:
            count+=1


    if count==2:
        count=0
        for i in range(1,rev+1):
            if rev%i==0:
                count+=1
        if count==2:
            print('empir number')
        else:
            print('not empir number')
    else:
        print('not empir number')
else:
    print('not empir number')

n=19

while n>9:
    sum=0
    while n!=0:
        r=n%10
        sum+=r**2
        n//=10
    n=sum

if n==1 or n==7:
    print('happy number')
else:
    print('not happy number')