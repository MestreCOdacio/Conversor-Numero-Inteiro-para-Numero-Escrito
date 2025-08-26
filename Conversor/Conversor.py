# Essa função é responsável por processar os valores e organizar os componentes String na ordem certa.
def numero_para_extenso(n):
    if n > 999 or n < 0:
        return "Número fora do intervalo (0-999)"
    if n == 0:
        return "Zero"

    unidades = ["", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove"]
    dezenas_especiais = ["Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]
    dezenas = ["", "", "Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]
    centenas = ["", "Cento", "Duzentos", "Trezentos", "Quatrocentos", "Quinhentos", "Seiscentos", "Setecentos", "Oitocentos", "Novecentos"]

    partes = []

    # Essa parte que processa as centenas!
    c = n // 100
    if n == 100:
        return "Cem"
    if c > 0:
        partes.append(centenas[c])
    
    # Essa parte processa o resto do número (dezenas e unidades).
    resto = n % 100
    if resto > 0:
        # Adiciona o 'e' se já tiver uma centena.
        if c > 0:
            partes.append("e")

        # Processa as dezenas.
        d = resto // 10
        u = resto % 10

        if 10 <= resto and resto <= 19:
            partes.append(dezenas_especiais[u])
        else:
            if d > 0:
                partes.append(dezenas[d])
            if u > 0:
                if d > 0:
                    partes.append("e")
                partes.append(unidades[u])

    return " ".join(partes)


# --- Parte Principal do Código ---
numero_str = input('Insira um número. Use a seguinte formatação: "xxx.xxx.xxx": ')

try:
    # Separa os grupos e converte para inteiros
    grupos_numericos = [int(s) for s in numero_str.split('.')]

    print("-" * 30)
    print("Resultado por extenso:")

    # Processa cada grupo de número
    for grupo in grupos_numericos:
        print(f"Grupo {grupo}: {numero_para_extenso(grupo)}")

except ValueError:
    print("Erro: Formato de número inválido. Certifique-se de usar apenas números e pontos.")