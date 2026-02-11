def checkmate(board):
    if not board:
        return

    rows = board.split("\n")
    size = len(rows)

    # ตรวจว่าเป็นสี่เหลี่ยม
    for row in rows:
        if len(row) != size:
            print("Error")
            return

    # หา King
    king_pos = None
    king_count = 0

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        print("Error")
        return

    king_r, king_c = king_pos

    # เดินดูทุกช่องแล้วหาว่าเป็นตัวอะไร
    for r in range(size):
        for c in range(size):
            piece = rows[r][c]

            # Pawn
            if piece == "P":
                moves = [
                    (r-1, c-1), #บนซ้าย
                    (r-1, c+1), #บนขวา
                    (r+1, c-1), #ล่างซ้าย
                    (r+1, c+1)  #ล่างขวา
                ]
                for nr, nc in moves:
                    if 0 <= nr < size and 0 <= nc < size:
                        if rows[nr][nc] == "K":
                            print("Success")
                            return

            # Rook
            if piece == "R" or piece == "Q":
                directions = [(-1,0),(1,0),(0,-1),(0,1)] #บน ล่าง ซ้าย ขวา
                for dr, dc in directions:
                    nr, nc = r, c
                    while True:
                        nr += dr
                        nc += dc
                        if not (0 <= nr < size and 0 <= nc < size):
                            break
                        if rows[nr][nc] == "K":
                            print("Success")
                            return
                        if rows[nr][nc] != ".":
                            break

            # Bishop
            if piece == "B" or piece == "Q":
                directions = [(-1,-1),(-1,1),(1,-1),(1,1)] #มุมทั้ง 4
                for dr, dc in directions:
                    nr, nc = r, c
                    while True:
                        nr += dr
                        nc += dc
                        if not (0 <= nr < size and 0 <= nc < size):
                            break
                        if rows[nr][nc] == "K":
                            print("Success")
                            return
                        if rows[nr][nc] != ".":
                            break

    print("Fail")
