def binary_search(sorted_collection, item):
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        current_item = sorted_collection[midpoint]
        if current_item == item:
            return midpoint
        elif item < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1

    return None  


sc = [2,4,6,8,9,36,56,57,64,87,89]
i = 87

index = binary_search(sc, i)

if __name__ == "__main__":
    import time
    start = time.process_time()
    print(f'Index {index}: Value {sc[index]}')
    print(f"Processing time: {time.process_time() - start}")