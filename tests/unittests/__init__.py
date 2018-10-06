from src.internals import Expression

tri_quote = '"""'


def get_expression(clp, used_keyword=None):
    is_indented = '    ' in clp or '    ' in clp
    line = Expression(clp, is_indented, used_keyword)

    if line.l_side:
        return line.l_side + ' = ' + line.r_side
    return line.r_side