#exércicio 1
idade = int(input("Insira sua idade"))
dade = int(input("Insira sua idade"))
 
if idade >16:
  print("eleitor obrigatório")
elif idade<16:
    print("Não Eleitor")

if dade>65 or 18:
   print("eleitor facultativo")


#exercício 2
a = float(input("Insira a variável A"))
b = float(input("Insira a variável B"))
c = float(input("Insira a variável C"))
   
   if a==0:
   print("não é equação do segundo grau")

delta = b**2 - 4*a*c

if delta>0:
   raiz1 = (-b + math.sqrt(delta)) / (2*a) 
   raiz2 = (-b - math.sqrt(delta)) / (2*a) 
   print("As raízes são:", raiz1, "e", raiz2)
elif delta ==0:
   raiz= -b/(2*a)
   print("A raiz é" , raiz)
else: 
   print("Não há raizes reais")