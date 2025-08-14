# test_captures.py
# اختبارات منطق الأكل للفيل بدون أي مكتبات خارجية

FILES = "abcdefgh"

def to_rc(sq: str):
    """حوّل مربع زي 'e2' إلى (row, col) حيث row=0 هو الصف 8"""
    c = FILES.index(sq[0])
    r = 8 - int(sq[1])
    return r, c

def is_empty(cell: str) -> bool:
    """تحقق إذا المربع فاضي"""
    return cell in (".", "·", " ")

def path_clear_exclusive(board, src, dst):
    """يتأكد إن كل المربعات بين المصدر والهدف فاضية (لا يشمل الهدف)"""
    sr, sc = src
    dr = dst[0] - sr
    dc = dst[1] - sc
    step_r = (dr > 0) - (dr < 0)
    step_c = (dc > 0) - (dc < 0)
    r, c = sr + step_r, sc + step_c
    while (r, c) != dst:
        if not is_empty(board[r][c]):
            return False
        r += step_r
        c += step_c
    return True

def color_of(ch: str):
    """لون القطعة: أبيض لو حرف كبير، أسود لو صغير"""
    if is_empty(ch):
        return None
    return "white" if ch.isupper() else "black"

def can_bishop_capture(board, src_sq, dst_sq):
    """تحقق إذا الفيل يقدر ياكل قطعة على الوجهة"""
    sr, sc = to_rc(src_sq)
    dr, dc = to_rc(dst_sq)
    # لازم يكونوا على نفس القطر
    if abs(dr - sr) != abs(dc - sc):
        return False
    # المسار قبل الوجهة لازم يكون فاضي
    if not path_clear_exclusive(board, (sr, sc), (dr, dc)):
        return False
    s_piece = board[sr][sc]
    d_piece = board[dr][dc]
    # لازم الوجهة يكون فيها قطعة (اختبار أكل)
    if is_empty(d_piece):
        return False
    # لازم تكون القطعة في الوجهة من لون مختلف
    return color_of(s_piece) != color_of(d_piece)

def empty_board():
    """أنشئ لوح فاضي"""
    return [list("........") for _ in range(8)]

def place(board, sq, ch):
    """ضع قطعة في مربع معين"""
    r, c = to_rc(sq)
    board[r][c] = ch

def run_tests():
    # 1) أكل قانوني
    board = empty_board()
    place(board, "c1", "B")  # فيل أبيض
    place(board, "e3", "q")  # وزير أسود
    assert can_bishop_capture(board, "c1", "e3") is True
    print("✅ Test 1 passed: Bishop can capture enemy on clear path")

    # 2) حاجز قبل الوجهة
    board = empty_board()
    place(board, "c1", "B")
    place(board, "d2", "P")  # بيدق أبيض حاجز
    place(board, "e3", "q")
    assert can_bishop_capture(board, "c1", "e3") is False
    print("✅ Test 2 passed: Bishop blocked by same-color piece before destination")

    # 3) نفس اللون على الوجهة
    board = empty_board()
    place(board, "c1", "B")
    place(board, "e3", "N")  # حصان أبيض
    assert can_bishop_capture(board, "c1", "e3") is False
    print("✅ Test 3 passed: Bishop cannot capture same-color piece")

if __name__ == "__main__":
    run_tests()
