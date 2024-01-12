#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def knapsack(items, weight):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    result = []

    for item in items:
        if item[1] <= weight:
            weight -= item[1]
            result.append(item)

        else:
            coefficient = item[0]/item[1]
            result.append([coefficient * weight, weight])
            weight = 0
            break
            
    return result


if __name__ == "__main__":
    items = [[14, 2], [20, 4], [18, 3], [30, 5]]
    weight = 12
    print(f"Изначальный массив:{items}")
    print(f"Результат: {knapsack(items, weight)}")