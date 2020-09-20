#sim eu fiz da maneira mais burra possivel
pessoastotais = 0
escolha = 0
pessoastotais = 0
quantidademas = 0
idademas = 0 
idademastotal = 0
pessoastotais = 0
quantidadefem = 0
idadefem = 0
idadefemtotal = 0
idademediamulheres = 0
idademediahomens = 0
idademediageral = 0

while pessoastotais<9:
    escolha = int(input("Qual é seu sexo, 1 para masculino 0 para feminino:"))
    if escolha>0:
        pessoastotais = pessoastotais + 1
        quantidademas = quantidademas + 1 
        
        idademas = int(input("Qual a sua idade::"))
        idademastotal = idademastotal + idademas


    else:
        pessoastotais = pessoastotais + 1
        quantidadefem = quantidadefem + 1 
        
        idadefem = int(input("Qual a sua idade:"))
        idadefemtotal = idadefemtotal + idadefem

idademediamulheres=  idadefemtotal/quantidadefem
print("a idade media das mulheres é:", idademediamulheres)
idademediahomens = idademastotal/ quantidademas
print("a idade media dos homens é:", idademediahomens)
idademediageral = idademediahomens+ idademediamulheres
print("a idade media de todos é :", idademediageral)


