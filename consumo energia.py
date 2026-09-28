'''consumo de energia'''
print("=" * 45)
print("  ⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡  ")
print("=" * 45)
''' 1. Entrada de dados do usuário'''
aparelho = input("Digite o nome do seu eletrodomestico: ").strip()
potencia = float(input(f"Digite a potência do {aparelho} em Watts (W): "))
horas_dia = float(input(f"Digite o tempo médio de uso diário de seu {aparelho} em horas: "))
'''Cálculo do consumo mensal em kWh'''
'''Fórmula: (Potência * Horas * 30 dias) / 1000'''
consumo_mensal = (potencia * horas_dia * 30) / 1000
'''Cálculo do custo estimado (Valor fictício de R$ 0,75 por kWh)'''
tarifa_kwh = 0.75
custo_estimado = consumo_mensal * tarifa_kwh
'''Exibição dos resultados formatados'''
print("\n" + "-" * 45)
print(f"📊 RESUMO DO CONSUMO - {aparelho.upper()}")
print("-" * 45)
print(f"🔹 Aparelho: {aparelho}")
print(f"🔹 Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"🔹 Custo estimado: R$ {custo_estimado:.2f}/mês (Tarifa: R$ {tarifa_kwh:.2f}/kWh)")
print("=" * 45)