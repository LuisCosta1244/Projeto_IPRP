def ler_linhas(nome):
    with open("nome.txt","r",encoding = "utf-8") as f:
        return f.read().split("\n")
