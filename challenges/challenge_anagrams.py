def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)


def merge(left, right, merged):
    left_index = 0
    right_index = 0
    merged_index = 0

    while (left_index < len(left) and right_index < len(right)):
        if left[left_index] < right[right_index]:
            merged[merged_index] = left[left_index]
            left_index += 1
        else:
            merged[merged_index] = right[right_index]
            right_index += 1

        merged_index += 1

    for left_index in range(left_index, len(left)):
        merged[merged_index] = left[left_index]
        merged_index += 1

    for right_index in range(right_index, len(right)):
        merged[merged_index] = right[right_index]
        merged_index += 1

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
