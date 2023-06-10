import re

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.;,:]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_de_palavras = re.sub(u'[,;.]',separa_palavras(texto))
    n_total_palavras = len(lista_de_palavras)

    tamanho_palavras = 0
    for i in range (n_total_palavras):
        tamanho_palavras = tamanho_palavras + len(lista_de_palavras[i]) #soma do tamanho de todas as palavras
        
        tamanho_medio_palavra = tamanho_palavras/n_total_palavras
    
        #type_token = n_palavras_diferentes(texto)/n_total_palavras
    
        #hapax_legomana = n_palavras_unicas(texto)/n_total_palavras

        #n_total_sentencas = len(separa_sentencas(texto))

        #n_total_frases = len(separa_frases(texto))
    
        #tamanho_medio_sentenca = tamanho_palavras/n_total_sentencas
    
        #complexidade_sentenca = n_total_frases/n_total_sentencas
    
        #tamanho_medio_frase = tamanho_palavras/n_total_frases

        #assinatura = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
        assinatura = [tamanho_medio_palavra]

    return assinatura

def calcula_tamanho(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_de_palavras = re.sub(u'[,;.]','',separa_palavras(texto))
    n_total_palavras = len(lista_de_palavras)

    tamanho_palavras = 0
    for i in range (n_total_palavras):
        tamanho_palavras = tamanho_palavras + len(lista_de_palavras[i]) #soma do tamanho de todas as palavras
        
        #tamanho_medio_palavra = tamanho_palavras/n_total_palavras
    
        #type_token = n_palavras_diferentes(texto)/n_total_palavras
    
        #hapax_legomana = n_palavras_unicas(texto)/n_total_palavras

        #n_total_sentencas = len(separa_sentencas(texto))

        #n_total_frases = len(separa_frases(texto))
    
        #tamanho_medio_sentenca = tamanho_palavras/n_total_sentencas
    
        #complexidade_sentenca = n_total_frases/n_total_sentencas
    
        #tamanho_medio_frase = tamanho_palavras/n_total_frases

        #assinatura = [tamanho_medio_palavra, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
        assinatura = [tamanho_palavras]

    return assinatura
