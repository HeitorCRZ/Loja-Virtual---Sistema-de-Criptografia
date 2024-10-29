'''Numero : 1'''
def binario(x) :
    '''

    Funcão : binario --- Tem como função converter um numero decimal inteiro para binario;

    x : Parametro que recebe o numero inteiro a ser convertido;

    return : Retorna o numero convertido para binario em formato de string;

    '''
    a = list()
    while x > 0 :
        if (x%2 == 0) :
            a.append(0)
        else :
            a.append(1)
        x =int( x / 2 )
    a.reverse()
    return "".join(map(str, a))
'''-----------------------------------------------------------------------------------------------------------'''
'''Numero : 2'''
def primo(x) :
    '''

    Funcão : binario --- Tem como função verificar se um numero é primo;

    x : Parametro que recebe o numero inteiro a ser verificado;

    return : Retorna 0 se não for primo ou 1 se for primo;

    '''
    primo = True
    if x == 0 :
        return 0
    else :
        if x == 2 :
            return 1
        else :
            for i in range (2,x) :
                if x % i == 0 :
                    return 0
                    primo = False
                    break
            if primo == True :
                return 1
'''-----------------------------------------------------------------------------------------------------------'''
'''Numero : 3'''