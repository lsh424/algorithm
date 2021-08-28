def solution(places):
    places = list(map(lambda place: list(map(lambda x: list(x), place)), places))

    dsnb = [(0,1), (1,0), (-1,0), (0,-1),(0,2),(2,0),(-2,0),(0,-2)]
    diagonal = [(-1,-1), (-1,1), (1,-1), (1,1)]

    def isSocialDistancing(place):
        for row in range(len(place)):
            for col in range(len(place[0])):
                if place[row][col] == "P":
                    for dr, dc in dsnb:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]) and place[nr][nc] == "P":
                            if abs(dr) == 1 or abs(dc) == 1:
                                return 0

                            if dr == 2:
                                if place[nr-1][nc] != "X":
                                    return 0
                            elif dr == -2:
                                if place[nr+1][nc] != "X":
                                    return 0
                            elif dc == 2:
                                if place[nr][nc-1] != "X":
                                    return 0
                            elif dc == -2:
                                if place[nr][nc+1] != "X":
                                    return 0

                    for dr, dc in diagonal:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]):
                            if place[nr][nc] == "P":
                                if dr == -1 and dc == -1:
                                    if place[nr+1][nc] != 'X' or place[nr][nc+1] != 'X':
                                        return 0
                                elif dr == -1 and dc == 1:
                                    if place[nr+1][nc] != 'X' or place[nr][nc-1] != 'X':
                                        return 0
                                elif dr == 1 and dc == -1:
                                    if place[nr-1][nc] != 'X' or place[nr][nc+1] != 'X':
                                        return 0
                                elif dr == 1 and dc == 1:
                                    if place[nr-1][nc] != 'X' or place[nr][nc-1] != 'X':
                                        return 0
        return 1

    answer = list(map(lambda place: isSocialDistancing(place), places))
    return answer