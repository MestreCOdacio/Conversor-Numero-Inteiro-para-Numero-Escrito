def extenso_para_numero(texto_por_extenso):
    """
    Converte um número escrito por extenso (entre 0 e 999) para um inteiro.
    Exemplo: "Vinte e Três" -> 23
    """
    
    # Cria dicionário de palavras para números.
    mapa_de_numeros = {
        'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4, 'cinco': 5,
        'seis': 6, 'sete': 7, 'oito': 8, 'nove': 9, 'dez': 10,
        'onze': 11, 'doze': 12, 'treze': 13, 'quatorze': 14, 'quinze': 15,
        'dezesseis': 16, 'dezessete': 17, 'dezoito': 18, 'dezenove': 19,
        'vinte': 20, 'trinta': 30, 'quarenta': 40, 'cinquenta': 50,
        'sessenta': 60, 'setenta': 70, 'oitenta': 80, 'noventa': 90,
        'cem': 100, 'cento': 100, 'duzentos': 200, 'trezentos': 300,
        'quatrocentos': 400, 'quinhentos': 500, 'seiscentos': 600,
        'setecentos': 700, 'oitocentos': 800, 'novecentos': 900
    }

    # Preparação da entrada do usuário
    palavras = texto_por_extenso.lower().split()

    # Processamento das palavras para calcular o total.
    total = 0
    for palavra in palavras:
        if palavra in mapa_de_numeros:
            total += mapa_de_numeros[palavra]

    return total

# --- Bloco Principal do Programa ---
try:
    entrada_usuario = input("Escreva um número por extenso (ex: duzentos e cinquenta e um): ")
    
    resultado_numerico = extenso_para_numero(entrada_usuario)
    
    print(f"\n> O número correspondente é: {resultado_numerico}")

except:
    print("Ocorreu um erro inesperado.")