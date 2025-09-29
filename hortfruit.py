
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

# Nomes dos alimentos para facilitar a exibição
nomes_alimentos = {
    1: "Brócolis",
    2: "Cebola", 
    3: "Pimentão Verde",
    4: "Quiabo",
    5: "Repólho",
    6: "Hortelã",
    7: "Louro Verde",
    8: "Batata Baroa",
    9: "Salsa",
    10: "Manjericão"
}

# Inicializando o carrinho de compras
carrinho = {}

# Loop para permitir que o usuário escolha os alimentos
while True:
    try:
        compras = int(input('Digite o número correspondente aos alimentos que deseja comprar (ou 0 para finalizar): '))
        
        if compras == 0:
            break
        
        if compras not in precos: #se o número digitado não estiver na lista preços, ele exibirá a mensagem de erro
            print("Número inválido. Tente novamente.")
            continue
        
        quantidade = float(input(f'Quantos kg de {nomes_alimentos[compras]} você deseja? ')) 
        #para cada alimento selecionado será exibido a mensagem perguntando o kg
        
        if quantidade <= 0: #mensagem de erro
            print("A quantidade deve ser maior que zero. Tente novamente.")
            continue
        
        #adicionando ao carrinho
        if compras in carrinho: 
            carrinho[compras] += quantidade #mostra a quantidade de alimentos e o kg
        else:
            carrinho[compras] = quantidade #caso não tenha compras no carrinho
            
        print(f"{quantidade}kg de {nomes_alimentos[compras]} adicionado ao carrinho!")

    except ValueError: #mensagem de erro para valor inválido
        print("Entrada inválida. Por favor, insira um número.")

#calculando o total da compra
total = sum(precos[item] * quantidade for item, quantidade in carrinho.items())

#exibindo o carrinho atual
print("\\n===== SEU CARRINHO =====")
if carrinho: #se no carrinho
    for item, quantidade in carrinho.items(): 
        subtotal = precos[item] * quantidade
        print(f"{item}- {nomes_alimentos[item]}: {quantidade:.2f}kg - R$ {subtotal:.2f}")
    print(f"\\nTotal da sua compra: R$ {total:.2f}")
else:
    print("Seu carrinho está vazio.")
    total = 0

#pergunta se deseja remover itens
resposta_remover = input("\\nDeseja remover algum produto do seu carrinho? [S/N]: ").strip().upper()

if resposta_remover == 'S' and carrinho:
    while True:
        try:
            print("\\n===== ITENS NO CARRINHO =====")
            for item, quantidade in carrinho.items():
                print(f"{item}- {nomes_alimentos[item]}: {quantidade:.2f}kg")
            
            item_numero = int(input("\\nDigite o número do item que deseja remover (ou 0 para sair da remoção): "))
            
            if item_numero == 0:
                break
                
            if item_numero not in carrinho:
                print("Item não encontrado no carrinho. Tente novamente.")
                continue
            
            quantidade_atual = carrinho[item_numero]
            print(f"Quantidade atual de {nomes_alimentos[item_numero]}: {quantidade_atual:.2f}kg")
            
            opcao_remover = input("Deseja remover [T]udo ou uma [Q]uantidade específica? ").strip().upper()
            
            if opcao_remover == 'T':
                #remove o item completamente
                del carrinho[item_numero]
                print(f"{nomes_alimentos[item_numero]} foi removido completamente do carrinho!")
                
            elif opcao_remover == 'Q':
                quantidade_remover = float(input("Quantos kg deseja remover? "))
                
                if quantidade_remover <= 0:
                    print("A quantidade deve ser maior que zero.")
                    continue
                elif quantidade_remover >= quantidade_atual:
                    del carrinho[item_numero]
                    print(f"{nomes_alimentos[item_numero]} foi removido completamente do carrinho!")
                else:
                    carrinho[item_numero] -= quantidade_remover
                    print(f"{quantidade_remover:.2f}kg de {nomes_alimentos[item_numero]} foi removido do carrinho!")
            else:
                print("Opção inválida. Use T para tudo ou Q para quantidade.")
                continue
                
            #recalcula o total
            total = sum(precos[item] * quantidade for item, quantidade in carrinho.items())
            
            if carrinho:
                print(f"\\nNovo total: R$ {total:.2f}")
                continuar = input("Deseja remover mais itens? [S/N]: ").strip().upper()
                if continuar != 'S':
                    break
            else:
                print("Carrinho vazio!")
                total = 0
                break
                
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

#exibindo o carrinho final
print("\\n===== CARRINHO FINAL =====")
if carrinho:
    for item, quantidade in carrinho.items():
        subtotal = precos[item] * quantidade
        print(f"{nomes_alimentos[item]}: {quantidade:.2f}kg - R$ {subtotal:.2f}")
    print(f"\\nTotal: R$ {total:.2f}")
else:
    print("Seu carrinho está vazio.")

#pergunta sobre sacolas (só se houver itens no carrinho)
if carrinho:
    sacolas = input("\\nVocê deseja adicionar sacolas para carregar os alimentos? [s/n]: ").strip().lower()
    qntsac = 0
    total2 = total
    
    if sacolas == 's':
        qntsac = int(input('Quantas sacolas deseja? '))
        total2 = total + (0.50 * qntsac)
        print(f"\\nVocê comprou R$ {total:.2f} em produtos e adicionou {qntsac} sacolas por R$ {0.50 * qntsac:.2f}.")
        print(f"TOTAL FINAL: R$ {total2:.2f}")
    else:
        print(f"\\nVocê comprou R$ {total:.2f} em produtos e não adicionou sacolas.")
        print(f"TOTAL FINAL: R$ {total:.2f}")
else:
    print("\\nNenhuma compra realizada.")