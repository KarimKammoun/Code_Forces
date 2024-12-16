t = int(input())  # Number of test cases
for _ in range(t):
    n, k = map(int, input().split())
    a = list(range(1, n + 1))  # Create array a=[1,2,...,n]
    
    # The median index of the full array a
    mid_index = n // 2
    
    # Check if k is at the median index
    if a[mid_index] == k:
        # If the median of the array is k, one subarray suffices
        print(1)
        print(1)
    else:
        # Try splitting into multiple subarrays with odd lengths
        subarray_starts = []
        for i in range(1, n, 3):  # Start indices for subarrays
            subarray_starts.append(i)
            if len(subarray_starts) % 2 == 1:
                median_index = len(subarray_starts) // 2
                # Check if the median of these subarrays' medians equals k
                if a[subarray_starts[median_index] - 1] == k:
                    print(len(subarray_starts))
                    print(" ".join(map(str, subarray_starts)))
                    break
        else:
            # If no valid partition is found
            print(-1)