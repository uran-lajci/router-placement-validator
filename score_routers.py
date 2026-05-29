from argparse import ArgumentParser


def is_covered(grid: list[list[str]], H: int, W: int, router_row: int, router_col: int, row: int, col: int) -> bool:
    if (row < 0) or (row >= H) or (col < 0) or (col >= W):
        return False

    if grid[row][col] in ('#', '-'):
        return False

    min_row, max_row = min(router_row, row), max(router_row, row)
    min_col, max_col = min(router_col, col), max(router_col, col)
    for w in range(min_row, max_row + 1):
        for v in range(min_col, max_col + 1):
            if grid[w][v] == '#':
                return False

    return True


def compute_score(input_src: str, submission_src: str) -> int:
    with open(input_src) as f:
        content = f.read().splitlines()

    H, W, R = (int(x) for x in content[0].split())
    Pb, Pr, B = (int(x) for x in content[1].split())

    grid = [list(content[3 + r]) for r in range(H)]

    with open(submission_src) as f:
        sub = f.read().splitlines()

    line = 0
    N = int(sub[line])
    line += 1
    line += N

    M = int(sub[line])
    line += 1

    covered = [[False] * W for _ in range(H)]
    for _ in range(M):
        router_row, router_col = (int(x) for x in sub[line].split())
        line += 1

        for row in range(router_row - R, router_row + R + 1):
            for col in range(router_col - R, router_col + R + 1):
                if is_covered(grid, H, W, router_row, router_col, row, col):
                    covered[row][col] = True

    t = sum(cell for cells in covered for cell in cells)
    return 1000 * t + (B - (N * Pb + M * Pr))


def main(input_path: str, submission_path: str) -> None:
    score = compute_score(input_path, submission_path)
    print(f'Score: {score}')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input_path', type=str, required=True)
    parser.add_argument('-s', '--submission_path', type=str, required=True)

    args = parser.parse_args()
    main(args.input_path, args.submission_path)

