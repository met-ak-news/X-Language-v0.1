from xlang.parser import parse_program

def test_basic():
    src = '''
U fetch reddit /r/test count=10
U summarize method=short
'''
    prog = parse_program(src)
    assert len(prog) == 2
    assert prog[0][0] == 'fetch'
    assert 'reddit' in prog[0][1]
