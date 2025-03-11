def obter_frase():
    """Solicita ao usuário uma frase e garante que não esteja vazia."""
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        print("Erro: A entrada não pode estar vazia. Tente novamente.")


def analisar_frase(frase):
    """Realiza análise e manipulação da frase fornecida."""
    num_caracteres = len(frase)
    palavras = frase.split()
    num_palavras = len(palavras)
    maior_palavra = max(palavras, key=len) if palavras else ""
    frase_invertida_caracteres = frase[::-1]
    frase_invertida_palavras = " ".join(reversed(palavras))
    frase_maiuscula = frase.upper()
    frase_minuscula = frase.lower()
    tupla_palavras = tuple(palavras)

    return {
        "num_caracteres": num_caracteres,
        "num_palavras": num_palavras,
        "maior_palavra": maior_palavra,
        "frase_invertida_caracteres": frase_invertida_caracteres,
        "frase_invertida_palavras": frase_invertida_palavras,
        "frase_maiuscula": frase_maiuscula,
        "frase_minuscula": frase_minuscula,
        "tupla_palavras": tupla_palavras,
    }


def exibir_resultados(analise):
    """Exibe os resultados da análise da frase."""
    print("\n=== Resultados da Análise ===")
    print(f"Número de caracteres: {analise['num_caracteres']}")
    print(f"Número de palavras: {analise['num_palavras']}")
    print(f"Maior palavra: {analise['maior_palavra']}")
    print(f"Frase invertida por caracteres: {analise['frase_invertida_caracteres']}")
    print(f"Frase invertida por palavras: {analise['frase_invertida_palavras']}")
    print(f"Frase em maiúsculas: {analise['frase_maiuscula']}")
    print(f"Frase em minúsculas: {analise['frase_minuscula']}")
    print(f"Tupla de palavras: {analise['tupla_palavras']}")


def main():
    frase = obter_frase()
    analise = analisar_frase(frase)
    exibir_resultados(analise)


if __name__ == "__main__":
    main()
