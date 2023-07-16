'''
Sistema para calcular a quantidade de rolos de papel de parede a
ser comprada baseado nas informações de metros quadrados da área
a ser aplicado, quantos metros quadrados o rolo cobre, preço do
rolo e uma folga de 10%.
'''

# Dados do problema
preco_do_rolo = float(input("Digite o preço do rolo: "))
cobertura_por_rolo = float(input("Digite a cobertura do rolo: "))
folga = 1.10

# Entrada do usuário
altura = float(input("Digite a altura: "))
largura = float(input("Digite largura: "))
area_a_ser_coberta = altura * largura


# Cálculos
quantidade_de_rolos_necessarios = (area_a_ser_coberta / cobertura_por_rolo) * folga  # Quantidade de rolos necessários
rolos = int(quantidade_de_rolos_necessarios) # Cálculo da parte inteira dos rolos
if quantidade_de_rolos_necessarios % cobertura_por_rolo != 0:  # Verifica se há uma fração de rolo a ser adicionada
    rolos += 1
preco_total = rolos * preco_do_rolo

# Saída
print("A área total a ser coberta é de {} m²".format(area_a_ser_coberta))
print("Quantidade de rolos a serem compradas:", rolos)
print("Preço total: R$", preco_total)
