#input é uma função que permite perguntar algo ao usuário, comentario de uma linha
#print é a função para aparecer para o usuário a mensagem
# str quer dizer string
# o # tbm serve para desativar uma função

#nome = input("Qual é o seu nome?")

'''
Bloco
de
Comentário
Permite que várias linhas se tornem um comentario
'''

#print("Olá,",nome,". Tudo bem com você?")
#print(type(nome))

a = 10
b = 5,8
c = "Rio de Janeiro"
d = True

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)

print("Tipo da var a: ", type(a)) #recebendo int, (para numeros inteiros)
print("Tipo da var b: ", type(b)) #tipo float, (para numeros reais)
print("Tipo da var c: ", type(c)) #tipo string (alfanumérico)
print("Tipo da var d: ", type(d)) # tipo boolean (True ou False)

a = 20
print("a: ", a)
b = "São Paulo"
print("b: ", b)
print("Tipo da varl a: ", type(a))
print("Tipo da var b: ", type(b))

a = input("informe um número: ")
b = input("informe outro número: ")
print("a: ", a, " - b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c: ", c) # juntar um termo com outro, dizemos que concatenou as strings de a e b
print("Tipo da var c: ", type(c))
d = int(a)
print("d: ", d)
print("Tipo da var d: ", type(d))

#precisa mudar de string para float ou int caso queira realizar uma conta, pois com o str ele só concatena
a = float(input("informe um número: "))
b = float(input("informe outro número: "))
print("a: ", a, " - b: ", b)
print("Tipo da var a: ", type(a))
print("Tipo da var b: ", type(b))
c = a + b
print("c: ", c)
print("Tipo da var c: ", type(c))

