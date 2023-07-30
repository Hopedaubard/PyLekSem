def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivor = array[0]
    less = [i for i in array[1:] if i <= pivor]
    greather = [i for i in array[1:] if i > pivor]
    return quick_sort(less) + [pivor] + quick_sort(greather)

print(quick_sort([14, 5, 6, 77, 8]))