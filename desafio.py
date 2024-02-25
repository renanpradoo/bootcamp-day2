### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

CTE = 1000
try:
    name = input('Digite seu nome: ')
    if(len(name)) == 0:
        raise ValueError('Nome nao pode estar vazio')
        exit()
    elif any(char.isdigit() for char in name):
        raise ValueError('Nao pode conter numeros no nome.')
        exit()
except ValueError as e:
    print(e)
    exit()

try:
    salario = float(input('Digite seu salario: '))
    if salario < 0:
        raise ValueError('Salario nao pode ser negativo.')
        exit()
except ValueError as e:
    print(e)    

try:
    bonus = float(input('Digite seu bonus: '))
    if bonus < 0:
        raise ValueError('Bonus nao pode ser negativo.')
        exit()
except ValueError as e:
    print(e)    


bonus_final = CTE + salario * bonus
print(f'{name}, seu bonus final eh: {bonus_final:.0f}')
