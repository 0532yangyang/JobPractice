# -*- coding: utf-8 -*-


def find_in_matrix(mat, number):
    assert len(mat) > 0 and len(mat[0]) > 0
    n_row = len(mat)
    n_col = len(mat[0])
    i = 0
    j = n_col-1
    while i < n_row and j >= 0:
        if mat[i][j] == number:
            return i, j
        elif mat[i][j] > number:
            j -= 1
        else:
            i += 1
    return None, None




if __name__ == '__main__':
    sample = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15],
    ]
    query = 11

    print find_in_matrix(sample, query)