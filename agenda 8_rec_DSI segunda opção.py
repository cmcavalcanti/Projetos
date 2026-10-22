'''opções de resposta para pesquisa de satisfação são variáveis pois serão armazenadas'''
excelente = 0
bom = 0
ruim = 0
'''estrutura de repetição para incluir intrevistado, até que o pesquisador queira encerrar a pesquisa'''
while True:
    nome = input("Digite o nome do entrevistado: ")
    idade = int(input("Digite a idade: "))
    print("\nOpine sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))
    if opiniao == 1:
        excelente += 1
        print("Opinião registrada: EXCELENTE")
    elif opiniao == 2:
        bom += 1
        print("Opinião registrada: BOM")
    elif opiniao == 3:
        ruim += 1
        print("Opinião registrada: RUIM")
    else:
        print("Opinião inválida!")
    continuar = input("\nDeseja entrevistar outra pessoa? (s/n): ").lower()
    if continuar != "s":
        break
'''utilização das variaveis para relatar o resultado da pesquisa e quantidade de cada opinião'''
print("\n===== RESULTADO DA PESQUISA =====")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas BOM:", bom)
print("Quantidade de respostas RUIM:", ruim)