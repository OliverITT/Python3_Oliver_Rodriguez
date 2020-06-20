def burbuja(lista):
    num = len(lista)
    i = 0
    while i < num:
        j = i
        while j < num:
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            j = j + 1
        i = i + 1



l= [10,4,6,72,2,4,90,224,643,1]


burbuja(l)

print(l)
