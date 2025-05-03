from sympy import Matrix, pprint
from functools import reduce
from math import gcd


# Author: Partho Sutra Dhor
# Date: 2/10/25
# Description: Transforming a matrix into Row Echelon Form (REF) and Reduced Row Echelon Form (RREF)

def print_matrix(matrix, step_desc):
    print(f"\n{step_desc}")
    pprint(matrix)


def row_gcd(row):
    return reduce(gcd, row)


def divide_by_gcd(matrix):
    return matrix
    global step
    for i in range(matrix.shape[0]):
        row = matrix.row(i)
        row_gcd_value = row_gcd(row)
        if row_gcd_value != 1 and row_gcd_value != 0:
            for j in range(matrix.shape[1]):
                matrix[i, j] = matrix[i, j] // row_gcd_value
            step = step + 1
            print_matrix(matrix, f"Step-{step}: Dividing by GCD: (Row {i + 1}) → (Row {i + 1}) / {row_gcd_value}")
    return matrix


def row_echelon_form(matrix):
    global step
    rows, cols = matrix.shape
    lead = 0

    for r in range(rows):
        if lead >= cols:
            return matrix

        # Find pivot in the current column
        i = r
        while matrix[i, lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return matrix

        # Swap rows
        if i != r:
            matrix.row_swap(i, r)
            step = step + 1
            print_matrix(matrix, f"Step-{step}: Row Swap: Swap Row {i + 1} with Row {r + 1}")

        # Eliminate below pivot
        for i in range(r + 1, rows):
            matrix = divide_by_gcd(matrix)
            lv = matrix[i, lead]
            pivot = matrix[r, lead]
            s = lv * pivot
            G = gcd(lv, pivot)
            lv = abs(lv // G)
            pivot = abs(pivot // G)
            if lv != 0:
                if s < 0:
                    for j in range(cols):
                        matrix[i, j] = pivot * matrix[i, j] + lv * matrix[r, j]
                    step = step + 1
                    print_matrix(matrix,
                                 f"Step-{step}: Eliminate below: (Row {i + 1}) → {pivot} * (Row {i + 1}) + {lv} * (Row {r + 1})")
                else:
                    for j in range(cols):
                        matrix[i, j] = pivot * matrix[i, j] - lv * matrix[r, j]
                    step = step + 1
                    print_matrix(matrix,
                                 f"Step-{step}: Eliminate below: (Row {i + 1}) → {pivot} * (Row {i + 1}) - {lv} * (Row {r + 1})")

        lead += 1

    return matrix


def reduced_row_echelon_form(matrix):
    global step
    rows, cols = matrix.shape
    lead_positions = []

    # Identify pivot positions
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] != 0:
                lead_positions.append((r, c))
                break

    # Eliminate above pivot
    for r, lead_col in reversed(lead_positions):
        matrix = divide_by_gcd(matrix)
        for i in range(r):
            lv = matrix[i, lead_col]
            pivot = matrix[r, lead_col]
            s = lv * pivot
            G = gcd(lv, pivot)
            lv = abs(lv // G)
            pivot = abs(pivot // G)
            if lv != 0:
                if s < 0:
                    for j in range(cols):
                        matrix[i, j] = pivot * matrix[i, j] + lv * matrix[r, j]
                    step = step + 1
                    print_matrix(matrix,
                                 f"Step-{step}: Eliminate above: (Row {i + 1}) → {pivot} * (Row {i + 1}) + {lv} * (Row {r + 1})")
                else:
                    for j in range(cols):
                        matrix[i, j] = pivot * matrix[i, j] - lv * matrix[r, j]
                    step = step + 1
                    print_matrix(matrix,
                                 f"Step-{step}: Eliminate above: (Row {i + 1}) → {pivot} * (Row {i + 1}) - {lv} * (Row {r + 1})")

    # Normalize pivot
    for r, lead_col in lead_positions:
        pivot = matrix[r, lead_col]
        if pivot != 1:
            for j in range(cols):
                matrix[r, j] = matrix[r, j] / pivot
            step = step + 1
            print_matrix(matrix, f"Step-{step}: Normalize Pivot: (Row {r + 1}) → (Row {r + 1}) / {pivot}")

    return matrix


# Imput Your Augmented Matrix

aug_matrix = Matrix([
    [0, -2, 3, 1],
    [3, 6, -3, -3],
    [6, 6, 3, 5]
])

step = 0
# Row Echelon Form (REF)
print("\n\n------ Solving System ------\n")
print("--- Press ENTER to Iterate ---")
print("---- Press CTRL+C to Exit ----")
print_matrix(aug_matrix, "Original Augmented Matrix")
print("\n")
row_echelon_form(aug_matrix)
print("\n")
print_matrix(aug_matrix, "Row Echelon Form (REF)")

# Reduced Row Echelon Form
print("\n")
reduced_row_echelon_form(aug_matrix)
print("\n")
print_matrix(aug_matrix, "Final Reduced Row Echelon Form (RREF)")
input()
input()