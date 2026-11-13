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

def info(linhas):
    i=len(linhas)
    c=0
    for linha in linhas:
        linha=linha.split(" ")
        for l in linha: #VERIFICAR SE É PARA CONTAR ESPAÇOS OU NAO
            c+=len(l)
    return print(f"{i} linhas e {c} caractéres")

def contar_frequencias(tokens):
    frequencias = {}
    for token in tokens:
        if token in frequencias:
            frequencias[token]+=1
        else:
            frequencias[token]=1
    return frequencias
        


