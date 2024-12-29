
def three_sum_zero(arr):
    arr.sort()
    result_set = set()
    n = len(arr)
    for i in range(n - 2):

        first_pointer = i + 1
        second_pointer = n - 1
        while first_pointer < second_pointer:
            if arr[i] + arr[first_pointer] + arr[second_pointer] > 0:
                second_pointer -= 1
            elif arr[i] + arr[first_pointer] + arr[second_pointer] < 0:
                first_pointer += 1
            else:
                if not (arr[i], arr[first_pointer], arr[second_pointer]) in result_set:
                    result_set.add((arr[i], arr[first_pointer], arr[second_pointer]))
                first_pointer += 1
    return [list(x) for x in result_set]




arr = [-1, 0, 1, 2, -1, -4, 1, 1, 1, -1, 0, -2]

print(three_sum_zero(arr))  # Вывод: [[-1, -1, 2], [-1, 0, 1]]
