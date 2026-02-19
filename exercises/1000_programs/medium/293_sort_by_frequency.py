def sort_by_frequency(arr):
    """
    Sort the elements of a list based on their frequency in descending order.
    If two elements have the same frequency, they are sorted in ascending order.
    """
    if not arr:
        return []

    # Count the frequency of each number manually
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Create a copy of the array to sort
    result = arr[:]

    # Sort by descending frequency, then by ascending value
    result.sort(key=lambda x: (-frequency[x], x))

    return result


if __name__ == "__main__":
    example = [4, 5, 6, 4, 5, 4]
    result = sort_by_frequency(example)
    print("Input:", example)
    print("Output:", result)
