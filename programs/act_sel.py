#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def act_sel(arr):
    result = []

    while len(arr) > 0:
        min_right_item = arr[0]
        min_right = arr[0][1]

        for i in arr:
            if min_right > i[1]:
                min_right = i[1]
                min_right_item = i.copy()
                
        arr.remove(min_right_item)
        result.append(min_right_item)
        
        new_arr = []
        for i in arr:
            if i[0] > min_right:
                new_arr.append(i)
                
        arr = new_arr.copy()

    return result
        

if __name__ == "__main__":
    arr = [[1, 4], [5, 8], [3, 6], [1, 5],[9, 10]]
    print(f"Изначальный набор отрезков: {arr}")
    print(f"Ответ: {act_sel(arr)}")
    