def ler_linhas(nome):
    with open("nome.txt","r",encoding = "utf-8") as f:
        return f.read().split("\n")

#1.1

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

#1.2








#1.3

def contar_frequencias(tokens):
    frequencias = {}
    for token in tokens:
        if token in frequencias:
            frequencias[token]+=1
        else:
            frequencias[token]=1
    return frequencias

#1.4

def top_n(freqs, n):
    copia = freqs.copy() #Não podemos alterar freqs de acordo com o enunciado
    res = []
    for _ in range(min(n ,len(freqs))):
        max_i = None
        for i in copia:
            if max_i == 0 or copia[i] > copia[max_i]:
                max_i = i
        res.append(max_i ,copia[max_i])
        del(copia[max_i])#juntar o tuplo à lista resultado e apagar o mais frequente para o caso de ser mais que 1 no n
    return res

#início do 2
#2.1


