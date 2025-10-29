import string
caminho = r"C:\Users\alice.salmazi\Downloads\PowerBI - BD + PY\PowerBI - BD + PY\colunas.txt"

def tratarColunasTabelas(nomeDaColuna: str, colunas: str) -> None:
    colunasTratadas = colunas.split(',')
    listaColunas = []

    listaColunas.append("--------------------------------")
    listaColunas.append(nomeDaColuna)

    for i in range(0, len(colunasTratadas), 2):
        nome = ''.join(caractere for caractere in colunasTratadas[i] if caractere == "_" or not caractere in string.punctuation and not caractere == ' ')
        listaColunas.append(nome + "\n")
    
    listaColunas.append("\n")
    
    with open(caminho, 'a', encoding="UTF-8") as arquivo:
        arquivo.writelines(listaColunas)

nomeDaColuna = input("Digite o nome da coluna: ")
entrada = input("Digite: ")
tratarColunasTabelas(nomeDaColuna, entrada)