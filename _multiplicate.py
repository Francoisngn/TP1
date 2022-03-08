
# return a result n & p are int
# produit = 0  
#while n>=1:
 #   if n%2 ==1:
        # we affect
  #      produit += p
   #         n >>=1
    #        p <<=1
     #       return  produit


def multiplication_egyptienne(a,b):
    #b= int(input(" "))
    #a =int(input(""))
    

    i=0 #init
    while a != 0:
        if(a%2) == 1:  # a is odd = impair
            i = i+b
        b = b*2
        a = a//2
    return(i)

resultat=multiplication_egyptienne(13,23)
print(resultat)
