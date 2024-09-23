import random
import time
import threading

# Function to merge two sorted arrays
def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    l, r = 0, 0
    result = []
    while len(left) > l and len(right) > r:
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    if len(left) > l:
        result += left[l:]
    if len(right) > r:
        result += right[r:]

    return result

# Merge Sort with manual thread creation
def merge_sort(array, num_threads=1):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Function to sort left or right in separate threads
    def threaded_sort(arr, result_container, idx):
        result_container[idx] = merge_sort(arr, num_threads//2)

    if num_threads > 1:
        left_result = [None]
        right_result = [None]

        # Create threads for sorting left and right parts
        left_thread = threading.Thread(target=threaded_sort, args=(left, left_result, 0))
        right_thread = threading.Thread(target=threaded_sort, args=(right, right_result, 0))

        # Start threads
        left_thread.start()
        right_thread.start()

        # Wait for both threads to complete
        left_thread.join()
        right_thread.join()

        # Merge the sorted left and right
        return merge(left_result[0], right_result[0])
    else:
        left_sorted = merge_sort(left, num_threads)
        right_sorted = merge_sort(right, num_threads)
        return merge(left_sorted, right_sorted)

# Main function to generate random list and perform merge sort
def main():
    # Configurable parameters
    num_threads = int(input("Enter the number of threads: "))
    array_size = int(input("Enter the size of the array: "))

    # Generate a random list of numbers
    random_list = [random.randint(0, 10000) for _ in range(array_size)]

    print(f"Random List: {random_list[:10]} ... (showing first 10 numbers)")

    # Time the sorting process
    start_time = time.time()
    sorted_list = merge_sort(random_list, num_threads)
    end_time = time.time()

    print(f"Sorted List: {sorted_list[:10]} ... (showing first 10 numbers)")
    print(f"Time taken to sort: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
