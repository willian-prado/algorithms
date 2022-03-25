def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)

def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
