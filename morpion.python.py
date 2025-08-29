a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def display():
    print(f"{a[0]} | {a[1]} | {a[2]}")
    print("________")
    print(f"{a[3]} | {a[4]} | {a[5]} ")
    print("________")
    print(f"{a[6]} | {a[7]}|  {a[8]}|  ")
    turn = 1
    joueur = "x"
 
running = True
while running:
       display()
       if turn%2  == 0:
        joueur ="o"
       else:
        joueur ="x"
le_joueur = int(input("entrez un numéro entre  1-9 :"))
i=0
while i<9:
        if le_joueur==a[i]:
            a[i]= joueur
            break
        i = i+1
        turn = turn +1  
i=0 
while i < 7:
            if i in ([0 , 1, 2] and a[i]==a[i+3]==a[i+6]) or (i in [0 , 3 , 6] and a[i] == a[i+1 ]== a[i+2]):
                 print(f"{joueur}won ")
                 break 
            i += 1
if running and (a[0]==a[4]==a[8]) or (a[2]==a[4]==a[6]):
      print(f"{joueur} won")
         
                 

  
              

    
        
            
    
            
    
    

        
