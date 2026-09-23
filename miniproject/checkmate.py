def checkmate(board):
    """Print Success if K is attacked, Fail if safe, or nothing if invalid."""
    if not isinstance(board, str):
        return
    rows = board.splitlines()
    size = len(rows)
    if size == 0:
        return
    for row in rows:
        if len(row) != size:
            return
    king_position = None
    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                if king_position is not None:
                    return
                king_position = (row, col)
    if king_position is None:
        return
    king_row, king_col = king_position
    for row in range(size):
        for col in range(size):
            piece = rows[row][col]
            row_distance = king_row - row
            col_distance = king_col - col
            if piece == "P":
                if row_distance == -1 and abs(col_distance) == 1:
                    print("Success")
                    return
            elif piece == "N":
                if (abs(row_distance), abs(col_distance)) in ((1, 2), (2, 1)):
                    print("Success")
                    return
            elif piece in "RBQ":
                straight = row_distance == 0 or col_distance == 0
                diagonal = abs(row_distance) == abs(col_distance)
                if piece == "R" and not straight:
                    continue
                if piece == "B" and not diagonal:
                    continue
                if piece == "Q" and not (straight or diagonal):
                    continue
                row_step = 0
                col_step = 0
                if row_distance > 0:
                    row_step = 1
                elif row_distance < 0:
                    row_step = -1
                if col_distance > 0:
                    col_step = 1
                elif col_distance < 0:
                    col_step = -1
                next_row = row + row_step
                next_col = col + col_step
                blocked = False
                while (next_row, next_col) != (king_row, king_col):
                    if rows[next_row][next_col] in "PBRQNK":
                        blocked = True
                        break
                    next_row += row_step
                    next_col += col_step
                if not blocked:
                    print("Success")
                    return
    print("Fail")
