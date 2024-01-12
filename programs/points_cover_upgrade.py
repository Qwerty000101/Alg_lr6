#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def points_cover_upgrade(arr):
    result = []
    arr.sort()
    i = 0

    while i < len(arr):
        x_left = arr[i]
        x_right = x_left + 1
        result.append([x_left, x_right])
        i += 1

        while i < len(arr) and arr[i] <= x_right:
            i += 1

    return result


if __name__ == "__main__":
    arr = [0.1, 1, 2, 3, 4, 5, 6, 7, 9, 11.1, 90]
    result = points_cover_upgrade(arr)
    print(f"Массив на входе: {arr}")
    print("Результат:")
    print(*result, sep="\n")