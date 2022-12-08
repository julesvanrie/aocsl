import os, sys, timeit
from aochelper import get_data

def solve(lines=None):
    # with open("input.txt") as fo:
    #     lines = fo.readlines()
    text = lines if lines else get_data(sys.argv)
    lines = text.split('\n')
    trees = [[tree for tree in row] for row in lines]
    h = len(trees)
    w = len(trees[0])
    visibilities = [[True for tree in range(w)] for row in range(h)]
    scenics = [[0 for tree in range(w)] for row in range(h)]

    for r, row in enumerate(trees[1:-1], start=1):
        for c, tree in enumerate(row[1:-1], start=1):
            left = right = up = down = 0
            col = [row[c] for row in trees]

            # For part 1
            if max(row[:c]) >= tree \
                and max(row[c+1:]) >= tree \
                and max(col[:r]) >= tree \
                and max(col[r+1:]) >= tree:
                    visibilities[r][c] = False

            # For part 2
            for i in range(c-1, -1, -1):
                left += 1
                if row[i] >= tree:
                    break
            for i in range(c+1, w, 1):
                right += 1
                if row[i] >= tree:
                    break
            col = [row[c] for row in trees]
            for i in range(r-1, -1, -1):
                up += 1
                if col[i] >= tree:
                    break
            for i in range(r+1, h, 1):
                down += 1
                if col[i] >= tree:
                    break

            scenics[r][c] = left * right * up * down

    result1 = sum(sum(v) for v in visibilities)
    result2 = max(max(v) for v in scenics)

    print("The result is for part 1 is:", result1)
    print("The result is for part 2 is:", result2)

    return result1, result2

def time():
    with open(os.devnull, 'w') as out:
        sys.stdout = out
        number = 20
        timing = timeit.timeit(solve, number=number) / number
        sys.stdout = sys.__stdout__
    print(f"This took {timing:.6f} seconds")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1][:4] == "time":
        del sys.argv[1]
        time()
    else:
        solve()
