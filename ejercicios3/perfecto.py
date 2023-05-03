num1=0
while num1<= 1000:
    num1 += 1
    i=1
    sum=0
    while i<num1:
        if num1%i==0:
            sum += i
        i+=1
        print(f' es perfecto el numero{num1}')
#terminar de coparlo