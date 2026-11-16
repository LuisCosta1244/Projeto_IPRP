def ler_linhas(nome):
    with open("nome.txt","r",encoding = "utf-8") as f:
        return f.read().split("\n")
    
def extrair_corpo(linhas):
    inicio = 0
    fim = len(linhas)
    for i , linha in enumerate(linhas):
        if linha[0,12] == "*** START OF":
            inicio = i + 1
        if linha[:10] == "*** END OF":
            fim = i
    return linhas[inicio:fim]
    
def tokenizar(texto):
    texto = texto.lower()
    for i in range(len(texto)):
        if texto[i].isalpha() == True and (i == 0 | texto[i].isalpha() != True):
        if i != 0 and (texto[i - 1].isalpha() and texto[i + 1]isalpha()):