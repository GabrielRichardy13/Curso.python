#Sorteando um item na lista

'''Um professor quer sortear 
um dos seus quatro alunos para 
apagar o quadro. Faça um programa 
que ajude ele, lendo o nome dos 
alunos e escrevendo na tela o nome 
do escolhido.'''

from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 =  input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

print (f'Entre {n1}, {n2}, {n3} e {n4} o escolhido foi {choice(lista)}')