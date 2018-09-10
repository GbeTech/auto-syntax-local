# from operators.Operators import Operator
from src.operators.Operators import Operator


class PrintOperator(Operator, cls_keywords=('print',)):

    def __init__(self, cls_keyword):
        self.create_line = lambda x, f: f"print({f}'{x}')"
        super().__init__(cls_keyword)
        self.assignment_possible = False

    def _handle_single_atom(self):
        self._parenthesize_stringify()

        return f'{self.cls_keyword}({self.atoms[0].result})'

    def _handle_multiple_atoms(self):
        for atom in self.atoms:
            self._parenthesize_stringify_single(atom,
                                                condition=lambda a: a.is_dotted and a.has_builtins(),
                                                dblquote=True
                                                )

            if atom.dotted_or_builtins_or_self():
                atom.result = f'{{{atom.result}}}'

        return self._convert()

    def _convert(self):
        any_dotted_or_builtins = any(atom.dotted_or_builtins_or_self() for atom in self.atoms)

        r_side = ' '.join(atom.result for atom in self.atoms)

        converted = self.create_line(r_side.strip(), 'f' if any_dotted_or_builtins else '')
        return converted