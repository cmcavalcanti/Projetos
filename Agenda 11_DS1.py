import sys
from colorama import Fore, Style, init
'''Inicializa o colorama para compatibilidade de cores no terminal'''
init()
def obter_alerta_reservatorio(nivel):
    """Retorna a mensagem e a cor correspondente ao nível do reservatório."""
    configuracoes_niveis = [{"situacao": "Muito baixo (crítico)", "cor": Fore.RED},{"situacao": "Baixo", "cor": Fore.YELLOW},{"situacao": "Médio", "cor": Fore.GREEN},{"situacao": "Alto", "cor": Fore.CYAN},{"situacao": "Muito alto (alerta)", "cor": Fore.BLUE},]
    '''Valida se o nível está dentro do intervalo de 1 a 5'''
    if 1 <= nivel <= 5:
        return configuracoes_niveis[nivel - 1]
    return None
def exibir_status(nivel):
    """Exibe a situação atual com a cor correta e restaura o estilo padrão."""
    dados = obter_alerta_reservatorio(nivel)
    if dados:
        print(f"\n[ALERTA] -> Nível {nivel}: {dados['cor']}{dados['situacao']}{Style.RESET_ALL}\n")
    else:
        print(f"\n{Fore.RED}Erro: Nível {nivel} está fora do intervalo operacional (1 a 5).{Style.RESET_ALL}\n")
'''Loop Contínuo do Sistema'''
if __name__ == "__main__":
    print("==============================================")
    print("   SISTEMA DE MONITORAMENTO DE RESERVATÓRIO   ")
    print("==============================================")
    print("Instruções: Digite um número de 1 a 5 para checar o status.")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    while True:
        '''Recebe a entrada do teclado e remove espaços extras'''
        entrada = input("Informe o nível atual da água: ").strip().lower()
        '''Condição de saída do loop contínuo'''
        if entrada == "sair":
            print(f"\n{Fore.LIGHTBLACK_EX}Desligando o sistema de monitoramento...{Style.RESET_ALL}")
            break
        '''Validação do tipo de dado inserido (deve ser um número inteiro)'''
        try:
            nivel_usuario = int(entrada)
            exibir_status(nivel_usuario)
        except ValueError:
            '''Captura o erro caso o usuário digite texto (que não seja 'sair') ou símbolos'''
            print(f"{Fore.RED}Entrada inválida! Por favor, insira um número inteiro entre 1 e 5 ou digite 'sair'.{Style.RESET_ALL}\n")
