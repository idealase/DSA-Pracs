import DSAsorts, csv, timeit
import matplotlib.pyplot as plt

names_list = []
times = {}

with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        names_list.append(row[0])


for i in range(1, 2000, 50):
    sorting_list = names_list.copy()
    print("Insertion Sorting " + str(i) + " items...")
    start_time = timeit.default_timer()
    DSAsorts.insertion_sort(sorting_list[0:i])
    end_time = timeit.default_timer()
    total_time = (end_time - start_time)
    times[i] = total_time
    print(total_time)

print(times)


plt.bar(range(len(times)), list(times.values()), align='center', color="green")
plt.xticks(range(len(times)), list(times.keys()), rotation=70)
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Insertion Sort Time Complexity Growth")
plt.savefig("ins.png")
plt.show()
