import math
import timeit


def progress_bar(progress, total):

    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "░" * (100 - int(percent))
    print(f"\r |{bar}| {percent:.2f}%", end="\r")

num_list = [x * 5 for x in range(2000,3000)]
results = []

for i, x in enumerate(num_list):
    progress_bar(i + 1, len(num_list))
    results.append(math.factorial(x))