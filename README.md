# Cálculo de Salário e Horas Extras

Este programa em Python calcula o salário total de um trabalhador com base nos dias trabalhados e nas horas extras realizadas. Ele solicita ao usuário que informe o salário mensal, o número de dias trabalhados no mês e a quantidade de horas extras realizadas. Com essas informações, o programa realiza os cálculos necessários e exibe os valores correspondentes.

## Como funciona

1. O usuário insere:
   - O salário mensal.
   - O número de dias trabalhados no mês.
   - A quantidade de horas extras trabalhadas.

2. O programa realiza os seguintes cálculos:
   - **Salário proporcional aos dias trabalhados**
   - **Valor das horas extras trabalhadas**
   - **Salário total considerando as horas extras**

## Fórmulas utilizadas

- **Cálculo do salário proporcional aos dias trabalhados:**
  ```python
  salario_diario = salario / 22  # Considerando 22 dias úteis no mês
  salario_total = salario_diario * dias_trabalhados
  ```

- **Cálculo do valor das horas extras:**
  ```python
  salario_hora = salario_diario / 8  # Considerando 8 horas de trabalho por dia
  valor_hora_extra = salario_hora * 1.5  # Horas extras pagas com 50% a mais
  total_horas_extras = valor_hora_extra * horas_trabalhadas
  ```

- **Cálculo do salário total com horas extras:**
  ```python
  salario_total_com_extras = salario_total + total_horas_extras
  ```

## Exemplo de Entrada e Saída

### Entrada do usuário:
```
Digite o salário: 2200
Digite o número de dias trabalhados: 20
Digite o número de horas extras trabalhadas: 10
```

### Saída esperada:
```
Salário total: R$ 2000.00
Total de horas extras: R$ 187.50
Salário total com horas extras: R$ 2187.50
```

## Como Executar o Código

1. Instale o Python (caso ainda não tenha).
2. Salve o código em um arquivo `salario.py`.
3. No terminal ou prompt de comando, navegue até o diretório onde o arquivo está salvo.
4. Execute o comando:
   ```sh
   python salario.py
   ```
5. Insira os valores solicitados e veja os cálculos na tela.

## Observação
- O programa considera um mês com **22 dias úteis**.
- Cada dia tem **8 horas de trabalho**.
- Horas extras são pagas com **50% de acréscimo**.

## Autor
Este código foi desenvolvido para fins educativos e pode ser adaptado conforme necessário.

