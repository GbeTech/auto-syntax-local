from . import PrintOperator


class StrOperator(PrintOperator, keywords=('str', "'", '"', "''", '""')):
    def __init__(self, op_keyword):
        super().__init__(op_keyword)
        self.assignment_possible = True
        if '"' in self.op_keyword:
            self.create_line = lambda x, f: f'{f}"{x}"'
        else:
            self.create_line = lambda x, f: f"{f}'{x}'"

    # don't remove, doesn't handle single atom differently than multiple
    def handle_atoms(self):
        return self._handle_multiple_atoms()