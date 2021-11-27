import timeit
import random

def bubble_sort(list): 
    for i in range(0,len(list)-1):  
        for j in range(len(list)-1):  
            if(list[j]>list[j+1]):  
                temp = list[j] 
                list[j] = list[j+1]  
                list[j+1] = temp 
    return list  

def selection_sort(list):
    for i in range(len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[min]):
                min = j
        if(min != i):
            list[i], list[min] = list[min], list[i]
    return list

def quick_sort(list):
    if len(list) < 2: 
        return list
    pivot_element = random.choice(list)
    esq = [i for i in list if i < pivot_element]
    med = [i for i in list if i==pivot_element]
    dir = [i for i in list if i > pivot_element]
    return quick_sort(esq) + med + quick_sort(dir)

def merge_sort(list):
	if len(list) > 1:
		mid = len(list)//2
		left = list[:mid]
		right = list[mid:]
		merge_sort(left)
		merge_sort(right)
		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				list[k] = left[i]
				i += 1
			else:
				list[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			list[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			list[k] = right[j]
			j += 1
			k += 1

def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1      
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp

def heapify(list, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and list[i] < list[l]:
        max = l
    if r < n and list[max] < list[r]:
        max = r
    if max != i:
        list[i],list[max] = list[max],list[i]
        heapify(list, n, max)

def heap_sort(list):
    n = len(list)
    for i in range(n, -1, -1):
        heapify(list, n, i)
    for i in range(n-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)

def create_random_list(n):
    list = []
    for i in range(0,n):
        n = random.randint(1,200000)
        list.append(n)
    print("Tamanho da lista: " + str(len(list)))
    return list

def create_asc_list(n):
    i = 1
    j = 0
    list = []
    while j < n:
        list.append(i)
        i += 1
        j += 1
    return list

def create_desc_list(n):
    i = 0
    j = n
    list = []
    while i < n:
        list.append(j)
        i += 1
        j -= 1
    return list

def check_sorted(list, type):
    flag = 0
    i = 1
    if type == 'asc':
        while i < len(list):
            if(list[i] < list[i - 1]):
                flag = 1
            i += 1
    else:
        while i < len(list):
            if(list[i] > list[i - 1]):
                flag = 1
            i += 1
    return flag

def random_list():
    #Bubble Sort
    list = create_random_list(100000)
    print("Bubble sort")
    start = timeit.default_timer()
    bubble_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Selection Sort
    list = create_random_list(100000)
    print("Selection sort")
    start = timeit.default_timer()
    selection_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Insertion Sort
    list = create_random_list(100000)
    print("Insertion Sort")
    start = timeit.default_timer()
    insertion_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Quick Sort
    list = create_random_list(100000)
    print("Quick Sort")
    start = timeit.default_timer()
    quick_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Merge Sort
    list = create_random_list(100000)
    print("Merge Sort")
    start = timeit.default_timer()
    merge_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Heap Sort
    list = create_random_list(100000)
    print("Heapsort")
    start = timeit.default_timer()
    heap_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")



def ordered_asc():
    #Bubble Sort
    list = create_asc_list(100000)
    print("Bubble sort")
    start = timeit.default_timer()
    bubble_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Selection Sort
    list = create_asc_list(100000)
    print("Selection sort")
    start = timeit.default_timer()
    selection_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Insertion Sort
    list = create_asc_list(100000)
    print("Insertion Sort")
    start = timeit.default_timer()
    insertion_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Quick Sort
    list = create_asc_list(100000)
    print("Quick Sort")
    start = timeit.default_timer()
    quick_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Merge Sort
    list = create_asc_list(100000)
    print("Merge Sort")
    start = timeit.default_timer()
    merge_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Heap Sort
    list = create_asc_list(100000)
    print("Heapsort")
    start = timeit.default_timer()
    heap_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

def ordered_desc():
    #Bubble Sort
    list = create_desc_list(100000)
    print("Bubble sort")
    start = timeit.default_timer()
    bubble_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Selection Sort
    list = create_desc_list(100000)
    print("Selection sort")
    start = timeit.default_timer()
    selection_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Insertion Sort
    list = create_desc_list(100000)
    print("Insertion Sort")
    start = timeit.default_timer()
    insertion_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.") 
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Quick Sort
    list = create_desc_list(100000)
    print("Quick Sort")
    start = timeit.default_timer()
    quick_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Merge Sort
    list = create_desc_list(100000)
    print("Merge Sort")
    start = timeit.default_timer()
    merge_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

    #Heap Sort
    list = create_desc_list(100000)
    print("Heapsort")
    start = timeit.default_timer()
    heap_sort(list)
    stop = timeit.default_timer()
    exec = stop - start
    print("Algoritmo executado em " + str(exec) + " segundos.")
    if(not check_sorted(list, "asc")):
        print("Ordenado!")
    else: 
        print("Não está ordenado.")
    print("=========================================================")

def main():
    print("----------------- Lista aleatória: ----------------- ")
    random_list()

    print("----------------- Lista ordenada asc: ----------------- ")
    ordered_asc()

    print("----------------- Lista ordernada desc: ----------------- ")
    ordered_desc()

if __name__ == "__main__":
    main()