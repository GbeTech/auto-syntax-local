from src.operators.Operators import Operator
from src.utils import get_singular


class ForOperator(Operator, cls_keywords=('for',)):
    def __init__(self, used_keyword):
        super().__init__(used_keyword)
        self.assignment_possible = False

    def _convert(self):
        if not self.atoms[0].subject.isdigit():
            singular = get_singular(self.atoms[0].subject)
            if 'enumerate' in self.atoms[0].builtins:
                converted = f'for i, {singular} in {self.atoms[0].result.replace("*","")}:\n    '
            else:
                converted = f'for {singular} in {self.atoms[0].result.replace("*","")}:\n    '
        else:
            converted = f'for i in range({self.atoms[0].result}):\n    '
        return converted

    def handle_atoms(self):
        self.atoms[0].parenthesize_builtins()
        if self.atoms[0].is_dotted:
            self.atoms[0].stringify_subject()
        self.atoms[0].close_parenthesis(around=self.atoms[0].subject)
        return self._convert()

    # def _handle_single_atom(self):
    #     self.atoms[0].parenthesize_builtins()
    #     if self.atoms[0].is_dotted:
    #         self.atoms[0].stringify_subject()
    #     self.atoms[0].close_parenthesis(around=self.atoms[0].subject)
    #     return self._convert()