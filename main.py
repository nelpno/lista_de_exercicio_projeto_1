def to_mb(tamanho_em_bytes):
    tamanho_em_bytes = float(tamanho_em_bytes)
    return float(tamanho_em_bytes / (1024 * 1024))


def percentual_por_usuario(lista, total):
    percentual = (lista[3] / total) * 100
    # percentual = "{0:.2f}".format(percentual)
    lista.insert((len(cada_usuario)), percentual)


def espaco_medio_ocupado(lista, total):
    media = 0
    elementos = len(lista)
    media = total / (elementos + 1)
    # media = "{0:.2f}".format(media)
    return media


# MAIN
usuarios = []
posicao = 1
total = media = 0
with open("usuarios.txt", "r") as arquivo:
    valor = 0
    for linha in arquivo:
        usuarios.append(linha.split())

    for cada_usuario in usuarios:
        cada_usuario.insert(0, posicao)
        valor = to_mb(float(cada_usuario[2]))
        total += valor
        cada_usuario.insert((len(cada_usuario)), valor)
        posicao += 1

    for cada_usuario in usuarios:
        percentual_por_usuario(cada_usuario, total)

media = espaco_medio_ocupado(cada_usuario, total)

with open("relatorio.txt", "w") as arquivo:
    arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
    arquivo.write("--------------------------------------------------------------\n")
    arquivo.write("Nr.\tUsuário        \tEspaço utilizado\t% do uso\n\n")

    for cada_usuario in usuarios:
        percentagem = "{0:.2f}".format(round(cada_usuario[3], 2))
        arquivo.write(str(cada_usuario[0]) + '\t' + "{:<15}".format(cada_usuario[1]) + '\t' + "{:<16}".format(
            percentagem) + 'MB' + '\t' + "{0:.2f}".format(cada_usuario[4]) + '%' + '\n')

    arquivo.write('\n\nEspaço Total Ocupado: ' + "{0:.2f}".format(total) + ' MB')
    arquivo.write('\n\nEspaço médio Ocupado: ' + "{0:.2f}".format(media) + ' MB')
    arquivo.close()

with open("relatorio.txt", "r") as arquivo:
    print(arquivo.read())
