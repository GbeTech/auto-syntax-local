from . import PrintOperator


class StrOperator(PrintOperator, cls_keywords=('str', "'", '"', "''", '""')):
    def __init__(self, used_keyword):
        super().__init__(used_keyword)
        self.assignment_possible = True
        if '"' in self.used_keyword:
            self.create_line = lambda x, f: f'{f}"{x}"'
        else:
            self.create_line = lambda x, f: f"{f}'{x}'"

    # don't remove, doesn't handle single atom differently than multiple
    def handle_atoms(self):
        return self._handle_multiple_atoms()