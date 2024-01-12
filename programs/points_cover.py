#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def points_cover(arr):
    result = []
    new_arr = arr.copy()

    while len(new_arr) != 0:
        x_left = min(new_arr)
        x_right = x_left + 1
        result.append([x_left, x_right])

        for i in arr:
            if i in new_arr and i >= x_left and i <= x_right:
                new_arr.remove(i)
                
    return result


if __name__ == "__main__":
    arr = [0.1, 1, 2, 3, 4, 5, 6, 7, 9, 11.1, 90]
    result = points_cover(arr)
    print(f"Массив на входе: {arr}")
    print("Результат:")
    print(*result, sep="\n")