def criacaoTabelaDax() -> None:
    with open("processoEtapas.txt", "r", encoding="UTF-8") as arquivo:
        texto = arquivo.read()

    linhas = texto.split('\n')
    textoNovo = []
    for i, linha in enumerate(linhas, start=1):
        palavras = linha.split(';')
        if i == len(linhas):
            string = "{ " + str(i) + ", " + palavras[1] + ", " + f'"{palavras[2]}"' + ", " + f'"{palavras[3]}"' + " }"
        else:
            string = "{ " + str(i) + ", " + palavras[1] + ", " + f'"{palavras[2]}"' + ", " + f'"{palavras[3]}"' + " },\n"
        textoNovo.append(string)
    
    with open("processoEtapasNovos.txt", "w", encoding="UTF-8") as arquivo:
        arquivo.writelines(textoNovo)

criacaoTabelaDax()