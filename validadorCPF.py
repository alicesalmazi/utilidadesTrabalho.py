import string

def validaCPF(texto):
    retorno = []
    textoTratado = ''.join(char for char in texto if char not in string.punctuation)
    if not all(caractere == textoTratado[0] for caractere in textoTratado):
        numeros = [int(digito) for digito in textoTratado]
        for _ in range(9,11):
            resultado = []
            if _ == 9:
                varAux = 9
            else:
                varAux = 10
            for i in range(varAux):
                resultado.append(numeros[i] * (varAux + 1 - i))
            medidaAux = sum(resultado) % 11
            if medidaAux in [0,1]:
                valorDigito = 0
            else:
                valorDigito = 11 - medidaAux
            if valorDigito == numeros[_]:
                retorno.append(True)
            else: 
                retorno.append(False)
    else:
        return "Válido=False"
    if all(retorno):
        return "Válido=True"
    else:
        return "Válido=False"

while True: 
    entrada = input("Digite o CPF para validação (para sair aperte o enter): ")
    if entrada != "":
        print( "Válido" if validaCPF(entrada) == True else "Inválido") 
    else:
        break