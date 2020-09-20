

Meses = {
     1 : "janeiro",
     2 : "fevereiro" ,
     3 : "março" ,
     4 : "abril", 
     5 : "maio" , 
     6 :"junho",
     7:"julho" ,
     8:"agosto" ,
     9:"setembro" ,
     10 :"outubro" ,
     11:"novembro",
     13:"dezembro", 
}

x = int(input("Escreva o número do mês desejado:  "))
if x < 13:
     print (Meses.get(x))
    
   
    
else:
    print("Não existe mês correspondente a esse número.")

