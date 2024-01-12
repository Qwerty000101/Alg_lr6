#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def act_sel_upgrade(arr):
    arr.sort(key=lambda item: item[1])
    result = []
    result.append(arr[0])

    for i in arr:
        if i[0] > result[-1][1]:
            result.append(i)
            
    return result
        

if __name__ == "__main__":
    arr = [[1, 4], [5, 8], [3, 6], [1, 5],[9, 10]]
    print(f"Изначальный набор отрезков: {arr}")
    print(f"Ответ: {act_sel_upgrade(arr)}")
    