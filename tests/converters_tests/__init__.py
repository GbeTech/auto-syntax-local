from expression import Expression


def get_expression(clp, keyword=None):
	line = Expression(clp, keyword)
	result = line.finalize()
	return result
