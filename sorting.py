import math
import time
import matplotlib.pyplot as plt
import numpy

def selection_sort(arr):
    comparisons = 0
    movements = 0
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            comparisons +=1
            if(arr[j]<arr[min]):
                min = j
        movements += 1
        temp = arr[min]
        movements += 1
        arr[min] = arr[i]
        movements += 1
        arr[i] = temp
    return comparisons, movements

def insertion_sort(arr):
    comparisons = 0
    movements = 0
    for i in range(1, len(arr)):
        aux = arr[i]
        movements += 1
        j = i-1
        while j >= 0 and arr[j] > aux:
            comparisons += 1
            arr[j+1] = arr[j]
            movements += 1
            j -= 1
        arr[j+1] = aux
        movements += 1
    return comparisons, movements

def shellsort(arr):
    comparisons = 0;
    movements = 0;
    n = len(arr)
    gap = 1
    while gap < n:
        gap = gap * 3 + 1
    while gap>0: #enquanto gap for maior que 0
        i=gap;
        while i<n: #enquanto i menor que o tamanho do vetor
            j=i-gap
            comparisons += 1
            while j>=0:
                comparisons += 1
                if(arr[j+gap]>arr[j]):
                    break
                else:
                    arr[j+gap], arr[j] = arr[j], arr[j+gap]
                    movements += 4
                j=j-gap
            i+=1
        gap=gap//3
    return comparisons, movements


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
    comparisons = 0
    movements = 0
    n = len(arr)
    for i in range(n):
        for j in range(1, (n-i)):
            comparisons += 1
            if(arr[j-1]>arr[j]):
                movements += 1
                aux = arr[j-1]
                arr[j-1] = arr[j]
                movements += 1
                arr[j] = aux
                movements += 1
    #return arr, comparisons, movements
    return comparisons, movements

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

def mergesort(arr):
    n = len(arr)
    if n>1:
        i = n//2
        left = arr[:i]
        right = arr[i:]
        mergesort(left)
        mergesort(right)

        a = b = c = 0
        while a<len(left) and b < len(right):
            if(left[a]<right[b]):
                arr[c] = left[a]
                a+=1
            else:
                arr[c] = right[b]
                b+=1
            c+=1
        while a < len(left):
            arr[c] = left[a]
            a+=1
            c+=1
        while b < len(right):
            arr[c] = right[b]
            b+=1
            c+=1
    return arr

testeBuffer = []
comp = []
move = []
n = []
clock = []
for j in range(1, 101):
    teste = []
    n.append(j*10)
    for i in range(10*j):
        teste.append(i+1)
    teste.reverse()
    testeBuffer = teste.copy()
    start_time = time.time()
    tuple = shellsort(teste)
    end_time = time.time()
    clock.append((end_time - start_time)*1e3)
    move.append(tuple[1])
    comp.append(tuple[0])

x_axis = numpy.array(n)
y_clock = numpy.array(clock)
y_movement = numpy.array(move)
y_comp = numpy.array(comp)

deg = 1.25

m, b = numpy.polyfit(x_axis, y_comp, deg)
y_comp_pred = m * x_axis + b

m, b = numpy.polyfit(x_axis, y_movement, deg)
y_move_pred = m * x_axis + b

m, b = numpy.polyfit(x_axis, y_clock, deg)
y_clock_pred = m * x_axis + b


fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
fig.axes[0].set_title('comparações x tamanho')
fig.axes[1].set_title('movimentações x tamanho')
fig.axes[2].set_title('tempo (seg) x tamanho')
ax1.scatter(x_axis, y_comp)
ax1.plot(x_axis, y_comp_pred, color='red')
ax2.scatter(x_axis, y_movement)
ax2.plot(x_axis, y_move_pred, color='red')
ax3.scatter(x_axis, y_clock)
ax3.plot(x_axis, y_clock_pred, color='red')

plt.show()

teste = [2, 5, 8, 9, 3, 4, 1]

start_time = time.time()
#print(selection_sort(teste))
print(shellsort(teste))
#print(shellsort(teste))
#print(quicksort(teste, 0, 6))
#print(bubblesort(teste))
end_time = time.time()
print(f"--- {(end_time - start_time)*1e3} segundos ---")
#print(heapsort(teste))
#print(mergesort(teste))