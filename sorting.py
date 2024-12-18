import math

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j]<arr[min]):
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        aux = arr[i]
        j = i-1
        while j >=0 and arr[j] > aux:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux
    return arr

def quicksort(arr, left, right):
    l = left #index mais a esquerda
    r = right #index mais a direita
    i = math.floor((left+right)/2)
    pivot = arr[(int)(i)] #define pivô do vetor

    while(l<=r):
        while(arr[l]<pivot): #aproxima esquerda do pivô
            l+=1
        while(arr[r]>pivot): #aproxima direita do pivô
            r-=1
        if(l<=r):
            aux = arr[l]; #salva número em auxiliar
            arr[l] = arr[r] #coloca número da direita na esquerda
            arr[r] = aux #coloca número da esquerda na direita
            l+=1
            r-=1
    if(left < r):
        quicksort(arr, left, r)
    if(l < right):
        quicksort(arr, l, right)
    return arr

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, (n-i)):
            if(arr[j-1]>arr[j]):
                aux = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = aux
    return arr

def heap(arr, arr_len, maior):
    raiz = maior #raiz começa como maior
    l = 2*maior+1 #esquerda
    r = 2*maior+2 #direita

    #se esquerda for maior que o maior
    if l<arr_len and arr[l]>arr[raiz]: 
        raiz = l

    #se direita for maior que o maior
    if r<arr_len and arr[r]>arr[raiz]:
        raiz = r

    #se raiz nao for o maior
    if raiz != maior:
        arr[maior], arr[raiz] = arr[raiz], arr[maior] #swap
        heap(arr, arr_len, raiz) #faz heap com as sub-árvores
    
def heapsort(arr):
    n = len(arr)

    #reorganiza vetor(faz heap)
    for i in range(n//2-1, -1, -1):
        heap(arr, n, i)
    
    #troca elementos de posição, levando o maior para o final
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap(arr, i, 0) #refaz heap

    return arr

teste = [2, 5, 8, 9, 3, 4, 1]
#print(selection_sort(teste))
#print(insertion_sort(teste))
#print(quicksort(teste, 0, 6))
#print(bubblesort(teste))
print(heapsort(teste))