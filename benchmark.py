import time
import random
import matplotlib.pyplot as plt
import psutil
import platform
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort

def benchmark_sort(sort_func, sizes):
    times = []
    for size in sizes:
        # Generate random array
        arr = [random.randint(0, 1000) for _ in range(size)]
        
        # Measure runtime
        start_time = time.time()
        sort_func(arr)
        end_time = time.time()
        
        # Calculate elapsed time
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    return times

def plot_results(sizes, insertion_times, selection_times, bubble_times):
    plt.figure(figsize=(14, 7))

    # Plot raw times
    plt.subplot(2, 2, 1)
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time vs. Array Size')
    plt.legend()
    plt.grid(True)

    # Plot with log-scaled y-axis
    plt.subplot(2, 2, 2)
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.yscale('log')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds, log scale)')
    plt.title('Sorting Time vs. Array Size (Log Scale)')
    plt.legend()
    plt.grid(True)

    # Plot with log-scaled x-axis
    plt.subplot(2, 2, 3)
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, selection_times, label='Selection Sort', marker='o')
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.xscale('log')
    plt.xlabel('Array Size (log scale)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time vs. Array Size (X Log Scale)')
    plt.legend()
    plt.grid(True)

    # Plot for larger sizes only
    large_sizes = [size for size in sizes if size >= 100]
    insertion_times_large = [insertion_times[sizes.index(size)] for size in large_sizes]
    selection_times_large = [selection_times[sizes.index(size)] for size in large_sizes]
    bubble_times_large = [bubble_times[sizes.index(size)] for size in large_sizes]

    plt.subplot(2, 2, 4)
    plt.plot(large_sizes, insertion_times_large, label='Insertion Sort', marker='o')
    plt.plot(large_sizes, selection_times_large, label='Selection Sort', marker='o')
    plt.plot(large_sizes, bubble_times_large, label='Bubble Sort', marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Time vs. Array Size (Large Sizes)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def print_system_info():
    print("System Information:")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB")
    print()

# Define Sizes to Test
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Print system information
print_system_info()

# Benchmark each sorting algorithm
print("Benchmarking Insertion Sort...")
insertion_times = benchmark_sort(insertion_sort, sizes)
print("Benchmarking Selection Sort...")
selection_times = benchmark_sort(selection_sort, sizes)
print("Benchmarking Bubble Sort...")
bubble_times = benchmark_sort(bubble_sort, sizes)

# Plot results
plot_results(sizes, insertion_times, selection_times, bubble_times)
