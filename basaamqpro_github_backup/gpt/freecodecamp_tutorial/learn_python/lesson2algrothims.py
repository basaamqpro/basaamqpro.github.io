# Hello World Example

unsorted_numbers = [5, 2, 9, 1, 5, 6]


for i in range(len(unsorted_numbers) - 1):
    print("sorting", unsorted_numbers)

    if unsorted_numbers[i] > unsorted_numbers[i + 1]:
        larger_number = unsorted_numbers[i]
        smaller_number = unsorted_numbers[i + 1]
        unsorted_numbers[i] = smaller_number
        unsorted_numbers[i + 1] = larger_number
    else:
        continue

print("Sorted numbers:", unsorted_numbers)