from src.utils import xnor
from . import PrintOperator


class StrOperator(PrintOperator, cls_keywords=('str', "'", '"', "''", '""')):

    def __init__(self, used_keyword):
        super().__init__(used_keyword)
        self.assignment_possible = True
        self.canonical = 'str'

        if '"' in self.used_keyword:
            self.maybe_fstring = lambda x, f: f'{f}"{x}"'
        else:
            self.maybe_fstring = lambda x, f: f"{f}'{x}'"

    def handle_atoms(self):
        is_single_atom = len(self.atoms) == 1
        if is_single_atom:
            condition = lambda a: a.is_dotted
        else:
            condition = lambda a: a.has_self

        any_dotted_or_builtins = self.process(try_brackets=True,
                                              condition=condition,
                                              dblquote=False)

        r_side = ' '.join(atom.result for atom in self.atoms).strip()

        f = ''
        if any_dotted_or_builtins:
            f = 'f'

        return self.maybe_fstring(r_side, f)