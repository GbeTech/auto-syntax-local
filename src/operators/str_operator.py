from . import PrintOperator


class StrOperator(PrintOperator, cls_keywords=('str', "'", '"', "''", '""')):
    def __init__(self, cls_keyword):
        super().__init__(cls_keyword)
        self.assignment_possible = True
        if '"' in self.cls_keyword:
            self.create_line = lambda x, f: f'{f}"{x}"'
        else:
            self.create_line = lambda x, f: f"{f}'{x}'"

    # don't remove, doesn't handle single atom differently than multiple
    def handle_atoms(self):
        return self._handle_multiple_atoms()