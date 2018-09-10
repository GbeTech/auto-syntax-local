# from operators.Operators import Operator
from src.operators.Operators import Operator
from src.utils import xnor


class PrintOperator(Operator, cls_keywords=('print',)):

    def __init__(self, used_keyword):
        self.create_line = lambda x, f: f"print({f}'{x}')"
        super().__init__(used_keyword)
        self.canonical = 'print'
        self.assignment_possible = False

    def handle_atoms(self):
        is_single_atom = len(self.atoms) == 1

        if is_single_atom:
            condition = lambda a: xnor(a.digit_or_builtins_or_self(),
                                       a.is_dotted)
            dblquote = False
        else:
            condition = lambda a: a.is_dotted and a.has_builtins(),
            dblquote = True

        if is_single_atom:
            self.parenthesize_stringify_atoms(condition)
            return f'{self.canonical}({self.atoms[0].result})'

        for atom in self.atoms:
            self._parenthesize_stringify_single(atom,
                                                condition=lambda a: a.is_dotted and a.has_builtins(),
                                                dblquote=dblquote
                                                )

            if atom.dotted_or_builtins_or_self():
                atom.result = f'{{{atom.result}}}'

        return self._convert()

    """def _handle_single_atom(self):
        self.parenthesize_stringify_atoms()

        return f'{self.canonical}({self.atoms[0].result})'

    def _handle_multiple_atoms(self):
        for atom in self.atoms:
            self._parenthesize_stringify_single(atom,
                                                condition=lambda a: a.is_dotted and a.has_builtins(),
                                                dblquote=True
                                                )

            if atom.dotted_or_builtins_or_self():
                atom.result = f'{{{atom.result}}}'

        return self._convert()"""

    def _convert(self):
        any_dotted_or_builtins = any(atom.dotted_or_builtins_or_self() for atom in self.atoms)

        r_side = ' '.join(atom.result for atom in self.atoms)

        converted = self.create_line(r_side.strip(), 'f' if any_dotted_or_builtins else '')
        return converted