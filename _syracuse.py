# suite syracuse
#n = int (input ( 'give the number of term '))
#while n <= 0 :
    #resaisir le nombre de terme 
    #n = int (input ( 'give the number of terms: '))
    #u = int(input ('U0 ') 1)
    #for i in range (1, n+1) :
     #    if u % 2 == 0:
      #      usuiv = u /2
       #  else :
        #     usuiv = 3*u + 1
        #print (u,i ,'=', usuiv)
    #u = usuiv suite
def s(u):
    r=u%2 
    if r==0:
        v = int( u/2)
    else : 
        v = 3*u +1
        return v    
    u= int(input(""))
    v = s(u)
    print(u)
    print(v)

    while v!= 1:
        u=v  # affect
        v= s(u)
        print(v)

        

