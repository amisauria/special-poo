def fibo(num):
    num1=0
    num2=1
    for i in range(1,num):
        num = num1 + num2
        num1 = num2
        num2 = num
        print(num2)

print(1)
fibo(19)
