# This problem is Find all duplicates in an array.
# Since elements are from 1 to n, and each appears at most twice, we can use a frequency array.
def findDuplicates(arr):
    n = len(arr)

    freq = [0] * (n + 1)

    result = []

    for num in arr:
        freq[num] += 1

    for i in range(n+1):
        if freq[i] == 2:
            result.append(i)

    return result

arr = [2, 3, 1, 2, 3]

print(findDuplicates(arr))