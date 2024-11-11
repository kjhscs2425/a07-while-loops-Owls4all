# write a factorial function, given n, you return n!
def factorial(n):
    counter=0
    product=1
    while True:
        counter +=1
        product *= counter
        if counter == n:
            break
    return product
number=int(input('give me a positive integer\n>>>'))
result=factorial(number)
print(f'{number}! = {result}')