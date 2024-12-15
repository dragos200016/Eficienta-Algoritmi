import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Algoritmi de sortare

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
        

def timsort(arr):
    return sorted(arr)  # Timsort este deja implementat în Python prin funcția sorted()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# *Merge Sort*
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

# Funcție pentru generarea și sortarea listei
def sorteaza_lista(lista, algoritmi):
    rezultate = []
    for nume_sortare, functie_sortare in algoritmi:
        print(f"Se sortează lista cu {nume_sortare}...")
        copie_lista = lista.copy()
        start_time = time.time()
        copie_lista = functie_sortare(copie_lista) if nume_sortare == "Quick Sort" else functie_sortare(copie_lista)
        end_time = time.time()
        rezultate.append({
            "Algoritm de Sortare": nume_sortare,
            "Lungimea Listei": len(lista),
            "Timp (s)": end_time - start_time
        })
        print(f"Sortarea cu {nume_sortare} finalizată în {end_time - start_time:.4f} secunde.")
    return rezultate

# Generare liste și procesare sortare
def genereaza_si_sorteaza_liste(numar_liste, interval_lungime):
    algoritmi = [
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Shell Sort", shell_sort),
        ("Timsort", timsort),
        ("Merge Sort", merge_sort)
    ]
    
    rezultate = []
    print("Se generează și se sortează listele...")
    for i in range(numar_liste):
        lungime = random.randint(*interval_lungime)
        lista = [random.randint(0, 100000) for _ in range(lungime)]
        print(f"Lista {i + 1} generată cu lungimea {lungime}.")
        rezultate += sorteaza_lista(lista, algoritmi)
    return rezultate

# Salvare rezultate și grafic
def salveaza_si_grafic(rezultate):
    print("Se salvează rezultatele în CSV...")
    df = pd.DataFrame(rezultate)
    df.to_csv("rezultate_sortare.csv", index=False)
    print("Rezultatele au fost salvate în rezultatele_sortare.csv.")

    print("Se generează graficul...")
    timpuri_medii = df.groupby("Algoritm de Sortare")["Timp (s)"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(timpuri_medii["Algoritm de Sortare"], timpuri_medii["Timp (s)"])
    plt.title("Comparația Timpilor de Execuție ai Algoritmilor de Sortare")
    plt.xlabel("Algoritm")
    plt.ylabel("Timp Mediu (s)")
    plt.savefig("comparatie_sortare.png")
    plt.show()
    print("Graficul a fost salvat ca comparatie_sortare.png.")


if __name__ == "__main__":
    rezultate = genereaza_si_sorteaza_liste(10, (10, 1000))
    salveaza_si_grafic(rezultate)
