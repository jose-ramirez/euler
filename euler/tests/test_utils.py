from euler.utils import Utils

def test_to_matrix():
    u = Utils()
    u.to_matrix('./test_matrix.in')

def test_to_matrix_2():
    u = Utils()
    u.to_matrix('./test_matrix_2.in', separator=',')

def test_log_factorial():
    u = Utils()
    actual = u.log_factorial(5)
    assert(actual > 0)

def test_log_nPr():
    u = Utils()
    actual = u.log_nPr(5, 4)
    assert(actual > 0)
