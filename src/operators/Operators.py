from src.internals import Atom, BUILTIN_FUNCTIONS
from src.utils import xnor

# from internals.consts import BUILTIN_FUNCTIONS

# from utils.internals_utils import xnor

WRAPPERS = {
    'list':  ('[', ']'),
    'tuple': ('(', ')'),
    'set':   ('{', '}'), }


# @log_methods
class Operator:
    _operators = {}

    def __init__(self, cls_keyword):
        self.assignment_possible = True
        self.cls_keyword = cls_keyword

        self.atoms = []

    def __init_subclass__(cls, **kwargs):
        cls_keywords = kwargs.get('cls_keywords')
        if cls_keywords:
            for kw in cls_keywords:
                cls._operators[kw] = cls
        """try:
            keywords = kwargs['keywords']

            for kw in keywords:
                cls._operators[kw] = cls
        except KeyError:
            try:
                cls._operators[kwargs['keyword']] = cls
            except KeyError:
                # log_methods get here (Wrapper class)
                breakpoint()"""

    @classmethod
    def by_keyword(cls, cls_keyword):
        """try:
    return cls._operators[cls_keyword](cls_keyword)
except (TypeError, KeyError):
    # __init__ usually doesn't take any argument.
    # StrOperator takes an argument, so try should succeed.
    # DefOperator takes an argument but for a different use. Should end up here.
    return cls._operators[cls_keyword]()"""

        return cls._operators[cls_keyword](cls_keyword)

    #
    # @staticmethod
    # def by_keyword(keyword):
    # 	return Operator._operators[keyword]()

    def _convert(self):
        """
        :rtype: str
        """
        r_side = ''
        wrapper = WRAPPERS[self.cls_keyword]
        for atom in self.atoms:
            r_side += f'{atom.result}, '
        converted = f'{wrapper[0]}{r_side.strip()[:-1]}{wrapper[1]}'
        return converted

    def _handle_single_atom(self):
        """:rtype: str"""
        self._parenthesize_stringify(condition=lambda a: a.is_dotted)

        return f'{self.cls_keyword}({self.atoms[0].result})'

    def _handle_multiple_atoms(self):
        self._parenthesize_stringify()
        return self._convert()

    def _parenthesize_stringify(self, condition=None):
        if isinstance(self.atoms, list):
            for atom in self.atoms:
                self._parenthesize_stringify_single(atom, condition)
        else:
            self._parenthesize_stringify_single(self.atoms[0], condition)

    @staticmethod
    def _parenthesize_stringify_single(atom, condition, dblquote=False):
        # KEEP STATIC AND ATOM AS PARAMETER
        if condition is None:
            condition = lambda a: xnor(a.digit_or_builtins_or_self(),
                                       a.is_dotted)

        atom.parenthesize_builtins()
        if condition(atom):
            atom.stringify_subject(dblquote)
        atom.close_parenthesis(around=atom.subject)

    def handle_atoms(self):
        if len(self.atoms) == 1:
            return self._handle_single_atom()
        else:
            return self._handle_multiple_atoms()

    def __eq__(self, other):
        return other == self.cls_keyword

    @staticmethod
    def _construct_atom_with_builtins(items_raw, i):
        """Add preceding builtins and set subject. Return atom"""
        atom = Atom(builtins=[items_raw[i]])
        j = i + 1
        while items_raw[j] in BUILTIN_FUNCTIONS:
            atom.builtins.append(items_raw[j])
            j += 1
        atom.subject = items_raw[j]
        i = j + 1
        return atom, i

    def construct_atoms(self, items_raw):
        """Set atom.subject, atom.is_dotted, atom.has_builtins, atom._is_digit for each atom. No any string
        manipulation"""
        # atoms = []
        items_len = len(items_raw)
        i = 0
        while i < items_len:
            if items_raw[i] in BUILTIN_FUNCTIONS:
                atom, i = self._construct_atom_with_builtins(items_raw, i)
                self.atoms.append(atom)
                continue

            else:
                self.atoms.append(Atom(subject=items_raw[i]))
                i += 1
                continue


# return atoms


class SetOperator(Operator, cls_keywords=('set',)):
    def __init__(self, cls_keyword):
        super().__init__(cls_keyword)


class TupleOperator(Operator, cls_keywords=('tuple', '()')):
    def __init__(self, cls_keyword):
        super().__init__(cls_keyword)


class ListOperator(Operator, cls_keywords=('list', '[]')):
    def __init__(self, cls_keyword):
        super().__init__(cls_keyword)