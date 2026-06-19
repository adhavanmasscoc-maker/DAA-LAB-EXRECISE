import random

def interpolation_search_float(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if abs(arr[low] - target) < 1e-9:
                return low, comparisons
            return -1, comparisons

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if abs(arr[pos] - target) < 1e-9:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


sizes = [10000, 50000, 100000]

print(f"{'Size':<10}{'Comparisons'}")
print("-" * 25)

for size in sizes:
    arr = sorted(random.uniform(0.0, 1000.0) for _ in range(size))

    target = arr[random.randint(0, size - 1)]

    index, comparisons = interpolation_search_float(arr, target)

    print(f"{size:<10}{comparisons}")
