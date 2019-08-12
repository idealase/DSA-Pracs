import DSAsorts, csv, timeit

with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    names_list = []
    for row in reader:
        names_list.append(row[0])

sort_choice = input("Choose a sort (B)ubble, (I)nsertion, or (S)election: ")

if sort_choice.upper() == "B":
    print("Bubble Sort")
    startTime = timeit.default_timer()
    DSAsorts.bubble_sort(names_list)
    endTime = timeit.default_timer()
    total_time = (endTime - startTime)
    print(total_time)
elif sort_choice.upper() == "I":
    print("Insertion Sort")
    startTime = timeit.default_timer()
    DSAsorts.insertion_sort(names_list)
    endTime = timeit.default_timer()
    total_time = (endTime - startTime)
    print(total_time)
elif sort_choice.upper() == "S":
    print("Selection Sort")
    startTime = timeit.default_timer()
    DSAsorts.selection_sort(names_list)
    endTime = timeit.default_timer()
    total_time = (endTime - startTime)
    print(total_time)
else:
    print("Poor choice")
