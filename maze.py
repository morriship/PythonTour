from collections import namedtuple, deque


Direction = namedtuple('Direction', 'x y')


class Dir:
    left = Direction(0, -1)
    right = Direction(0, 1)
    top = Direction(-1, 0)
    bottom = Direction(1, 0)


dirs = [Dir.left, Dir.right, Dir.top, Dir.bottom]


# 0 0 0
# 2 1 0
# 0 3 0
def find_exit(n, m, maze):
    # initialize
    # find positions of rat and exit
    rat_x, rat_y = -1, -1
    exit_x, exit_y = -1, -1
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                rat_y, rat_x = i, j
            if maze[i][j] == 3:
                exit_y, exit_y = i, j

    # start BFS algorithm
    que = deque()
    # init queue with the poisition of rat, and 0 distance
    # que((x-axis, y-axis, distance from rat))
    que.append((rat_x, rat_y, 0))

    while len(que):
        cnt_x, cnt_y, distance = que.pop()
        # dirs: top, left, right, bottom
        for direction in dirs:
            next_x = cnt_x + direction.x
            next_y = cnt_y + direction.y
            if next_x < 0 or next_y < 0 or next_x >= m or next_y >= n:
                continue

            target_cell = maze[next_y][next_x]
            if target_cell == 3:
                return distance + 1
            if target_cell == 0:
                maze[next_y][next_x] = 1
                que.append((next_x, next_y, distance + 1))
    return -1


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    maze = [list(map(int, input().split())) for i in range(n)]
    print(find_exit(n, m, maze))
