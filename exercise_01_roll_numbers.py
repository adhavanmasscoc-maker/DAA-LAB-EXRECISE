import math

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and arr[low] <= target <= arr[high]:
        probes += 1

        if low == high:
            if arr[low] == target:
                return low, probes
            return -1, probes

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, probes
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, probes


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high:
        probes += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, probes
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, probes


# Student roll numbers
roll_numbers = list(range(1, 10001))

target = int(input("Enter roll number to search: "))

idx_i, probes_i = interpolation_search(roll_numbers, target)
idx_b, probes_b = binary_search(roll_numbers, target)

print("\nInterpolation Search")
print("Position:", idx_i)
print("Probes:", probes_i)

print("\nBinary Search")
print("Position:", idx_b)
print("Probes:", probes_b)
