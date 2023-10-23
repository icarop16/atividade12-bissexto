 # Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Ano = int(input("Insira um ano: "))
if (Ano%4==0 and Ano%100!=0) or (Ano%400==0):
    print(f"{Ano} é um ano bissexto.")
else:
    print(f"{Ano} é um ano bissexto.")