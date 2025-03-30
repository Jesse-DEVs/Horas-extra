def obter_float(mensagem):
    while True:
        try:
            valor  = float(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
        

def obter_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
         
          
salario = obter_float("Digite o salário: ")
dias_trabalhados = obter_int("Digite o número de dias trabalhados: ")
horas_trabalhadas = obter_float("Digite o número de horas extras trabalhadas: ")

def calcular_salario(salario, dias_trabalhados):
    salario_diario = salario / 22  # Considerando 22 dias úteis no mês
    salario_hora = salario_diario / 8  # Considerando 8 horas de trabalho por dia
    salario_total = salario_diario * dias_trabalhados
    return salario_total
print("Salário total: R$ %.2f" % calcular_salario(salario, dias_trabalhados))
def calcular_horas_extras(salario, horas_trabalhadas):
    salario_diario = salario / 22  # Considerando 22 dias úteis no mês
    salario_hora = salario_diario / 8  # Considerando 8 horas de trabalho por dia
    valor_hora_extra = salario_hora * 1.5  # Considerando 50% a mais para horas extras
    total_horas_extras = valor_hora_extra * horas_trabalhadas
    return total_horas_extras
print("Total de horas extras: R$ %.2f" % calcular_horas_extras(salario, horas_trabalhadas))
def calcular_salario_total(salario, dias_trabalhados, horas_trabalhadas):
    salario_total = calcular_salario(salario, dias_trabalhados) + calcular_horas_extras(salario, horas_trabalhadas)
    return salario_total
print("Salário total com horas extras: R$ %.2f" % calcular_salario_total(salario, dias_trabalhados, horas_trabalhadas))