# Print all perfect square numbers between 1 and 100.
# num=int(input("Enter a number:"))
for i in range(1,101):
    root=int(i**0.5)
    if root*root == i:
        print(i)
# Print all Armstrong numbers between 1 and 100
for i in range(1,1001):
    num=i
    total=0
    length=len(str(num))
    while num>0:
        last=num%10
        total+=last**length
        num=num//10
    if total==i:
        print(i)

