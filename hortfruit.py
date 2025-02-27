# Exibindo o cabeçalho
print('======= HORT- FRUIT FORNY ========')
print()
print('LISTA DE ALIMENTOS OFERECIDOS:')
print('1- Brócolis: R$ 5,65/kg')
print('2- Cebola: R$ 3,33/kg')
print('3- Pimentão Verde: R$ 6,05/kg')
print('4- Quiabo: R$ 10,99/kg')
print('5- Repólho: R$ 3,49/kg')
print('6- Hortelã: R$ 39,51/kg')
print('7- Louro Verde: R$ 9,21/kg')
print('8- Batata Baroa: R$ 13,32/kg')
print('9- Salsa: R$ 5,65/kg')
print('10- Manjericão: R$ 9,26/kg')

# Dicionário de preços por kg
precos = {
    1: 5.65,  # Brócolis
    2: 3.33,  # Cebola
    3: 6.05,  # Pimentão Verde
    4: 10.99, # Quiabo
    5: 3.49,  # Repólho
    6: 39.51, # Hortelã
    7: 9.21,  # Louro Verde
    8: 13.32, # Batata Baroa
    9: 5.65,  # Salsa
    10: 9.26  # Manjericão
}

# Inicializando o carrinho de compras
carrinho = {}

# Loop para permitir que o usuário escolha os alimentos
while True:
    try:
        compras = int(input('Digite o número correspondente aos alimentos que deseja comprar (ou 0 para finalizar): '))
        
        if compras == 0:
            break
        
        if compras not in precos:
            print("Número inválido. Tente novamente.")
            continue
        
        quantidade = float(input(f'Quantos kg de {list(precos.keys())[compras-1]} você deseja? '))
        
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero. Tente novamente.")
            continue
        
        # Adicionando ao carrinho
        if compras in carrinho:
            carrinho[compras] += quantidade
        else:
            carrinho[compras] = quantidade

    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

# Calculando o total da compra
total = sum(precos[item] * quantidade for item, quantidade in carrinho.items())

# Exibe o total da compra
print(f"\nTotal da sua compra: R$ {total:.2f}")

# Pergunta sobre sacolas
sacolas = input("Você deseja adicionar sacolas para carregar os alimentos? [s/n]").strip().lower()
qntsac = 0
total2 = total
if sacolas == 's':
    qntsac=int(input('Quantas sacolas deseja? '))
    total2 = total + (0.50*qntsac)
print(f"Você comprou R$ {total2:.2f} em produtos e adicionou {qntsac} sacolas para carregar.")
if sacolas == 'n': 
    print(f"Você comprou R$ {total:.2f} em produtos e adicionou {qntsac} sacolas para carregar.")
