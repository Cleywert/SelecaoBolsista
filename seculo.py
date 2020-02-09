def retornaSeculo(ano):
    ano_formatado = ano
    if len(ano_formatado)==3:
        ano_formatado = '0'+ano
    if len(ano_formatado)==2:
        ano_formatado = '00'+ano
    if len(ano_formatado)==1:
        ano_formatado = '000'+ano

    sec = int(ano_formatado[0]+ano_formatado[1])
    dec = int(ano_formatado[2]+ano_formatado[3])
    if dec == 00:
        return sec
    return sec+1

seculo = retornaSeculo(input("Digite um ano: "))
print(seculo)
