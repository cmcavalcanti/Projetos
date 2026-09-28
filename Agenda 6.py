# ENTRADA DOS DADOS
# Solicita ao usuário que informe o valor total da compra
valor_total_compra = float(input("Digite o valor total da compra: (R$): "))
# PROCESSAMENTO DOS DADOS (Vai calcular o desconto de acordo com o valor de cada compra)
# Primeira Regra: Compras menores que R$ 200,00 desconto de 5%
if valor_total_compra < 200.00:
    percentual_desconto = 5
# Segunta regra: Compras entre R$ 200,00 e R$ 299,99 desconto de 10%
elif valor_total_compra >= 200.00 and valor_total_compra < 300.00:
    percentual_desconto = 10
# Terceira regra: Compras igual ou acima de R$ 300,00 desconto de 15%
else: 
    percentual_desconto = 15
valor_desconto = valor_total_compra * (percentual_desconto / 100)
# Calcula o valor total a ser pago após o desconto
valor_final_pago = valor_total_compra - valor_desconto
#SAÍDA DOS DADOS
# Mostra os resultados dos calculos de acordo com o valor das compras
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor total da compra: R$ {valor_total_compra:.2f}")
print(f"Valor do desconto: {percentual_desconto}%: R$ {valor_desconto:.2f})")
print(f"Valor total a ser pago: R$ {valor_final_pago:.2f}")