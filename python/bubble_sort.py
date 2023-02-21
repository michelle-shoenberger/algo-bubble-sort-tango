def bubble_sort(sequence):
    swaps = 0
    iterations = 0
    iter_swaps = 0
    previous, current = 0, 1
    while True:
        if sequence[previous] > sequence[current]:
            sequence[previous], sequence[current] = sequence[current], sequence[previous]
            swaps += 1
            iter_swaps += 1
        previous += 1
        current += 1
        if previous == len(sequence) - 1:
            iterations += 1
            if iter_swaps == 0:
                break
            iter_swaps = 0
            previous, current = 0, 1
    print(swaps)
    print(iterations)
    return sequence, swaps, iterations


