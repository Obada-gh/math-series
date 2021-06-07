
#0, 1, 1, 2, 3, 5, 8, 13, ...

'''
 F_{n}=F_{n-1}+F_{n-2}
'''


def fibonacci(n):
    if n==1 or n==0:
        return n

    return  fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))#5

#2, 1, 3, 4, 7, 11, 18, 29, ...

'''
Ln:={2              if n=0
    {1              if n = 1   wiki refrence :) 
    {Ln-1 + Ln-2    if n > 1
'''
def lucas(n):
    if n==0:
        return 2

    if n==1:
        return 1

    if n>1:
        return  lucas(n-1)+lucas(n-2)


print(lucas(5)) #11

'''
new series start with the optional numbers:
ex:
5,5,10,15,25,40
'''

#5,5,10,15,25,40 for (5,5,5)
def sum_series(n,optional1=0,optional2=1):
    if optional1==0 and optional2==1:
        return fibonacci(n)
    elif optional1==2 and optional2==1:
        return lucas(n)
    else:
        return anotherSeries(n,optional1,optional2)



def anotherSeries(a,b,c):
    if a==0 : 
        return b
    if a== 1 : 
        return c
    else:
        return anotherSeries(a-1,b,c)+ anotherSeries(a-2,b,c)


print(sum_series(5,5,5)) #40
print(sum_series(5,0,1)) #5  same fibonacci
print(sum_series(5,2,1)) #11 same lucas

      
        

  

        




    
 
    


        
    



