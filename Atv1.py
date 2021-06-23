#a)
def sequencia_a(adicao):
    sequencia = []
    i = 1
    r = 1 

    while i <= adicao:
        sequencia.append(r)
        r += 2
        i += 1
    return sequencia

#b)
def sequencia_b(adicao):
    sequencia = []
    i = 1
    r = 0

    while i <= adicao:
        r = r + i
        sequencia.append(r)
        i +=1
    return sequencia
    
#c)
def sequencia_c(adicao):
    sequencia = []
    i = 1

    while i <= adicao:
        r = i*i
        sequencia.append(r)
        i +=1
    return sequencia 

if __name__ == '__main__':
    adicao = 20

    print(sequencia_a(adicao))
    print(sequencia_b(adicao))
    print(sequencia_c(adicao))