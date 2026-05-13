def contains_duplicate(arr):
    seen = {}
    for n in arr:
        if n in seen:
            return True
        seen[n] = True
    return False

print(contains_duplicate([1, 2, 3, 1]))