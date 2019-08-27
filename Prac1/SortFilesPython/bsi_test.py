import DSAsorts, csv, timeit
import matplotlib.pyplot as plt
import numpy as np

names_list = []

max_n = 2000

with open('RandomNames.csv', 'rt') as file:
    reader = csv.reader(file)
    for row in reader:
        names_list.append(row[0])

btimes = {}
for i in range(1, max_n, 50):
    sorting_list = names_list.copy()
    print("Bubble Sorting " + str(i) + " items...")
    start_time = timeit.default_timer()
    DSAsorts.bubble_sort(sorting_list[0:i])
    end_time = timeit.default_timer()
    total_time = (end_time - start_time)
    btimes[i] = total_time
    print(total_time)

print(btimes)

stimes = {}
for i in range(1, max_n, 50):
    sorting_list = names_list.copy()
    print("Selection Sorting " + str(i) + " items...")
    start_time = timeit.default_timer()
    DSAsorts.selection_sort(sorting_list[0:i])
    end_time = timeit.default_timer()
    total_time = (end_time - start_time)
    stimes[i] = total_time
    print(total_time)

print(stimes)

itimes = {}
for i in range(1, max_n, 50):
    sorting_list = names_list.copy()
    print("Insertion Sorting " + str(i) + " items...")
    start_time = timeit.default_timer()
    DSAsorts.insertion_sort(sorting_list[0:i])
    end_time = timeit.default_timer()
    total_time = (end_time - start_time)
    itimes[i] = total_time
    print(total_time)

print(itimes)


x = np.arange(len(itimes))
width = 0.35

fig, ax = plt.subplots()
irect = ax.bar(x - width, list(itimes.values()), width, alpha=0.7,
               label="Insertion")
brect = ax.bar(x, list(btimes.values()), width, alpha=0.7,
               label="Bubble")
srect = ax.bar(x + width, list(stimes.values()), width, alpha=0.7,
               label="Selection")

ax.set_ylabel('Time (s)')
ax.set_title('Sort Time Complexity Growth')


ax.legend()

fig.tight_layout()
plt.xticks(range(len(itimes)), list(itimes.keys()), rotation=70)
plt.xlabel("n")
plt.savefig("bsi.png")
plt.show()
