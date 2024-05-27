def permutations(array):
    if len(array) <= 1:
        return [array]
    else:
        perms = []
        for i in range(len(array)):
            first_element = array[i]
            remaining_elements = array[:i] + array[i + 1:]
            for perm in permutations(remaining_elements):
                perms.append([first_element] + perm)
        return perms

print(permutations(['a', 'b', 'c', 'd']))

