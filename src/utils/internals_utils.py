from contextlib import contextmanager
import types


def _is_builtin_const(target):
	return target in ['None', 'True', 'False']


def delete_many(src, *args):
	for arg in args:
		src = src.replace(arg, '')
	return src


def get_singular(clp):
	clp = delete_many(clp, "'", 'self.', '*')
	if len(clp) >= 2 and clp.endswith('s'):
		return clp[:-1]
	elif clp.startswith('i'):
		return 'item'
	else:
		return clp[0]


@contextmanager
def ignore(*exceptions):
	try:
		yield
	except exceptions:
		pass


def stringify(target, dblquote=False):
	surround = '"' if dblquote else "'"
	return surround_with(surround=surround, to_surround=target)


def stringify_if_not_builtin_const_or_digit(target):
	if not target.isdigit() and not _is_builtin_const(target):
		return stringify(target)
	else:
		return target


def surround_with(surround, to_surround):
	return f'{surround}{to_surround}{surround}'


def xnor(a, b):
	return not a ^ b


def class_decorator(cls):
	"""Prints class method name on method call"""

	class Wrapper:
		@staticmethod
		def log_func(func, *args, **kwargs):
			print(f'logging {func.__qualname__}')

			return lambda *args, **kwargs: func(*args, **kwargs)

		def __init__(self, *args, **kwargs):
			self.wrapped = cls(*args, **kwargs)
			for k, v in cls.__dict__.items():
				if type(v).__name__ == 'function':
					v = self.log_func(v)

		def __getattr__(self, name):
			# cls_name = self.wrapped.__class__.__name__
			# try:
			# 	cls_name = self.wrapped.__class__.__name__
			# except KeyError:
			# 	print(self.wrapped)
			attr = getattr(self.wrapped, name)
			is_method = type(attr) == types.MethodType
			# print(f'is {cls_name} of types.MethodType: {is_method}')
			if is_method:
				return self.log_func(attr)
			else:
				return attr

	return Wrapper
