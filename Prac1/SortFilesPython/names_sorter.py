import DSAsorts, csv, timeit

names_list = []


with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        names_list.append(row[0])


def sorter3000():
    sort_choice = input("Choose a sort (B)ubble, (I)nsertion, or (S)election: ")

    if sort_choice.upper() == "B":
        print("Bubble Sort")
        start_time = timeit.default_timer()
        sorted_nl = DSAsorts.bubble_sort(names_list[0:2000])
        end_time = timeit.default_timer()
        total_time = (end_time - start_time)
        print(total_time)
        with open('sorted_names.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for name in sorted_nl:
                writer.writerow(name)
    elif sort_choice.upper() == "I":
        print("Insertion Sort")
        start_time = timeit.default_timer()
        sorted_nl = DSAsorts.insertion_sort(names_list[0:2000])
        end_time = timeit.default_timer()
        total_time = (end_time - start_time)
        print(total_time)
        with open('sorted_names.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for name in sorted_nl:
                writer.writerow(name)
    elif sort_choice.upper() == "S":
        print("Selection Sort")
        start_time = timeit.default_timer()
        sorted_nl = DSAsorts.selection_sort(names_list[0:2000])
        end_time = timeit.default_timer()
        total_time = (end_time - start_time)
        print(total_time)
        with open('sorted_names.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            for name in sorted_nl:
                writer.writerow(name)
    else:
        print("Poor choice")


sorter3000()
