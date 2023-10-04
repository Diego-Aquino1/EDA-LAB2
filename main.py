import random
import time

# Generar números aleatorios y guardarlos en un archivo
def generar_numeros_aleatorios(cantidad):
    nombre_archivo = "numeros_aleatorios.txt"
    with open(nombre_archivo, "w") as archivo:
        for _ in range(cantidad):
            numero_aleatorio = random.uniform(0, 1)
            archivo.write(str(numero_aleatorio) + "\n")

def cargar_numeros_desde_archivo():
    nombre_archivo = "numeros_aleatorios.txt"
    with open(nombre_archivo, "r") as archivo:
        numeros = [float(line.strip()) for line in archivo]
    return numeros


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    tamaños = [10, 100, 1000, 5000, 10000, 200000, 500000, 1000000]

    print("Elija el algoritmo de ordenamiento:")
    print("1. Bubble Sort")
    print("2. Heap Sort")
    print("3. Insertion Sort")
    print("4. Selection Sort")
    print("5. Shell Sort")
    print("6. Merge Sort")
    print("7. Quick Sort")

    opcion = int(input("Ingrese el número correspondiente al algoritmo: "))
    print("Tiempo en Milisegundos")

    for tamaño in tamaños:
        generar_numeros_aleatorios(tamaño)
        numeros = cargar_numeros_desde_archivo()

        if opcion == 1:
            start_time = time.time()
            bubble_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t -> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 2:
            start_time = time.time()
            heap_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 3:
            start_time = time.time()
            insertion_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 4:
            start_time = time.time()
            selection_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 5:
            start_time = time.time()
            shell_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 6:
            start_time = time.time()
            merge_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        elif opcion == 7:
            start_time = time.time()
            quick_sort(numeros)
            end_time = time.time()
            print(f"{tamaño}\t-> {(end_time - start_time) * 1000:.2f}")
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 7 para seleccionar un algoritmo válido.")