#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def max_independent_set(tree):
    if tree == {}:
        return []
    
    leaves = []
    branches = set()

    def traverse(t, path):
        for node, child in t.items():
            current_path = path + [node]
            if child == {}:
                if len(current_path) != 1:
                    branches.add(tuple(current_path[:-1]))
                else:
                    branches.add((current_path[-1],))

                leaves.append(node)

            traverse(child, current_path)

    traverse(tree, [])
    list_br = list(branches)
    temp_list_branch = []
    sorted_branches = sorted(list_br, key=len)

    for branch in sorted_branches:
        temp_branch = []
        
        for i in range(len(branch)):
            if not branch[i] in temp_list_branch:
                temp_branch.append(branch[i])

        parent = tree
        if len(temp_branch) != 1:
            for node in temp_branch[:-1]:
                temp = parent
                parent = parent[node]
        else:
            temp = tree

        for key, value in parent[temp_branch[-1]].copy().items():
            if value == {}:
                del parent[temp_branch[-1]][key]
            elif len(temp_branch) != 1:
                temp[node][key] = value
            else:
                temp[key] = value
                
        del parent[temp_branch[-1]]
        temp_list_branch.append(temp_branch[-1])
        
    list_leave = (max_independent_set(tree))
    leaves.extend(list_leave)

    return leaves


if __name__ == '__main__':
    tree = {1: {2:{4: {},5: {},6: {}},3:{7: {},8: {},9: {}}}}
    print(max_independent_set(tree))
    
    tree = {1: {2: {3: {4: {5: {6: {7: {8: {9: {10: {}}}}}}}}}}}
    print(max_independent_set(tree))