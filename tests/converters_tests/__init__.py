from internals.expression import Expression


def get_expression(clp, keyword=None):
	is_indented = '\t' in clp or '    ' in clp
	line = Expression(clp, is_indented, keyword)
	result = line.finalize()
	return result
