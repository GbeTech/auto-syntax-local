# from operators.Operators import Operator
from src.operators.Operators import Operator
from src.utils import xnor


class PrintOperator(Operator, cls_keywords=('print',)):

    def __init__(self, used_keyword):
        super().__init__(used_keyword)
        self.canonical = 'print'
        self.assignment_possible = False
        self.maybe_fstring = lambda x, f: f"print({f}'{x}')"

    def handle_atoms(self):
        multiple_atoms = len(self.atoms) > 1
        if multiple_atoms:
            condition = lambda a: a.is_dotted and a.has_builtins()
        else:
            condition = lambda a: xnor(a.digit_or_builtins_or_self(),
                                       a.is_dotted)

        any_dotted_or_builtins = self.process(try_brackets=multiple_atoms,
                                              condition=condition,
                                              dblquote=multiple_atoms)

        if not multiple_atoms:
            return f'{self.canonical}({self.atoms[0].result})'

        return self.cleanup(any_dotted_or_builtins)

    def cleanup(self, any_dotted_or_builtins):
        r_side = ' '.join(atom.result for atom in self.atoms).strip()
        f = ''
        if any_dotted_or_builtins:
            f = 'f'
        return self.maybe_fstring(r_side, f)

    def process(self, try_brackets, condition, dblquote):
        any_dotted_or_builtins = False
        for atom in self.atoms:
            atom.parenthesize_builtins()
            if condition(atom):
                atom.stringify_subject(dblquote)
            atom.close_parenthesis(around=atom.subject)

            if try_brackets:
                if atom.dotted_or_builtins_or_self():
                    any_dotted_or_builtins = True
                    atom.result = f'{{{atom.result}}}'
        return any_dotted_or_builtins

    """def _convert(self, any_dotted_or_builtins):
        # any_dotted_or_builtins = any(atom.dotted_or_builtins_or_self() for atom in self.atoms)

        r_side = ' '.join(atom.result for atom in self.atoms)

        converted = self.create_line(r_side.strip(), 'f' if any_dotted_or_builtins else '')
        return converted"""