import random

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

fim = (".", "!", "?", ",")
def tokenizar(texto):
    texto = texto.lower() # em minúsculas
    tokens = [] # lista onde vai guardar os tokens finais
    palavra = "" # vai acumulando as letras da palavra atual
    for i in range(len(texto)):
        if texto[i].isalpha(): # se o carácter atual pertencer ao alfabeto
            palavra += texto[i] # acrescenta à palavra
        elif texto[i] in ("-", "'") and palavra != "" and i + 1 < len(texto) and texto[i + 1].isalpha():
            palavra += texto[i] # adiciona a letra à palavra quando o caracter atual é um hifen ou apostrofe e a palavra não está vazia (para garantir que estes simbolos estão no meio da palavra) e o próximo é uma letra
        else: # qualquer outro carácter termina a palavra
            if palavra != "": # limpa a variável e guarda na lista
                tokens.append(palavra) # adiciona à lista
                palavra = ""
            if texto[i] in fim: # se for um ponto, virgula, exclamação, ...
                if len(tokens) == 0 or tokens[-1] not in fim: # se estiver vazia ou se o último não for um sinal
                    tokens.append(texto[i]) # adiciona à lista
    if palavra != "": # se terminar numa letra, guarda a última palavra
        tokens.append(palavra)
    
    return tokens


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

def construir_bigramas(tokens):
    big={}
    for i in range(len(tokens)-1):
        palavra = tokens[i]
        seguinte = tokens[i+1]
        if palavra not in big:#se a palavra ainda n esta no principal criamos o sub
            big[palavra] = {}
        sub_dic = big[palavra]
        if seguinte in sub_dic:#contar frequencia do token seguinte
            sub_dic[seguinte] += 1
        else:
            sub_dic[seguinte] = 1
    return big

#2.2

def probabilidade(modelo,a,b): # recebe o dict e duas strings
    if a not in modelo or b not in modelo[a]: # a = palavra
        return 0.0                            # b = segunda palavra
    
    total_sucessores = sum(modelo[a].values()) # extrai apenas os valores
    
    return modelo[a][b] / total_sucessores

#2.3

def escolher_proxima(sucessores):
    c=0
    total = sum(sucessores.values())
    r = random.randint(1,total)
    for palavra, contagem in sucessores.items():
        acumulado += contagem
        if acumulado >= r:
            return palavra

    