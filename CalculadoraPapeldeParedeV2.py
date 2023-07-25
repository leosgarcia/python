'''
Sistema para calcular a quantidade de rolos de papel de parede a
ser comprada baseado nas informações de metros quadrados da área
a ser aplicado, quantos metros quadrados o rolo cobre, preço do
rolo e uma folga de 10%.
'''

class CalculadoraPapelDeParede:
    def __init__(self, preco_do_rolo, cobertura_por_rolo, folga=1.10):
        self.preco_do_rolo = preco_do_rolo
        self.cobertura_por_rolo = cobertura_por_rolo
        self.folga = folga

    def calcular_quantidade_rolos(self, altura, largura):
        area_a_ser_coberta = altura * largura
        quantidade_de_rolos_necessarios = (area_a_ser_coberta / self.cobertura_por_rolo) * self.folga
        return int(quantidade_de_rolos_necessarios) + 1 if quantidade_de_rolos_necessarios % self.cobertura_por_rolo != 0 else int(quantidade_de_rolos_necessarios)

    def calcular_preco_total(self, quantidade_de_rolos):
        return quantidade_de_rolos * self.preco_do_rolo


# Dados do problema
preco_do_rolo = float(input("Digite o preço do rolo: "))
cobertura_por_rolo = float(input("Digite a cobertura do rolo: "))

# Criar a instância da calculadora de papel de parede
calculadora = CalculadoraPapelDeParede(preco_do_rolo, cobertura_por_rolo)

# Entrada do usuário
altura = float(input("Digite a altura: "))
largura = float(input("Digite largura: "))
area_a_ser_coberta = altura * largura

# Cálculos
quantidade_de_rolos_necessarios = calculadora.calcular_quantidade_rolos(altura, largura)
preco_total = calculadora.calcular_preco_total(quantidade_de_rolos_necessarios)

# Saída
print("A área total a ser coberta é de {} m²".format(area_a_ser_coberta))
print("Quantidade de rolos a serem comprados:", quantidade_de_rolos_necessarios)
print("Preço total: R$", preco_total)
