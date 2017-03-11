def sort(lst): 
    if len(lst)==1:
        return lst
    else:
        left, right = lst[:len(lst)//2], lst[len(lst)//2:]
        return merge(sort(left), sort(right))

def merge(left, right):
    merged = []
    i = 0
    j = 0
    for k in range(2*len(right)):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
            if i == len(left):
                merged = merged + right[j:]
                break
        else:
            merged.append(right[j])
            j += 1
            if j == len(right):
                merged = merged + left[i:]
                break
    return merged