# 21: Conversor de Temperatura

# try:
#     temp = float(input('Digite a temperatura em C: '))

#     if isinstance(temp, float):
#         k = 2.5
#         temp_f = temp * k
#         print(f'A temp em outra base eh : {temp_f}')
# except ValueError as e:
#     print(f'Tipo de input invalido: {e}')
    

# 22: Verificador de Palíndromo
    
# try:

#     word = input('Digite uma palavra ou frase: ')

#     if isinstance(word, str):
#         word_x = word.replace(" ", "").lower()
#         if word_x == word_x[::-1]:
#             print('Eh um palindromo')
#         else:
#             print('Nao eh palindromo')
# except ValueError as e:
#     print(f'Tipo de input invalido: {e}')

# if isinstance(word, str):

# 23: Calculadora Simples
    
# try:
#     temp1 = float(input('Digite a o primeiro num: '))
#     temp2 = float(input('Digite a o segundo num: '))

#     if isinstance(temp1, float) and isinstance(temp2, float):
#         temp3 = temp1 / temp2
#         print(f'Resultado : {temp3}')
# except ValueError as e:
#     print(f'Tipo de input invalido: {e}')
# except ZeroDivisionError as e:
#     print(f'Tipo de input invalido: {e}')

# 24: Classificador de Números

# 25: Conversão de Tipo com Validação

numeros = input('Digite numeros separados por virgula: ')
numeros_split = numeros.split(',')
numeros_list = []

try:
    for n in numeros_split:
        numeros_list.append(int(n.strip()))
    print(numeros_list)
except TypeError as e:
    print(f"Tipo invalido de numero: {e}")
except AttributeError as e:
    print(f"Tipo invalido de numero: {e}")
except ValueError as e:
    print(f"Tipo invalido de numero: {e}")    