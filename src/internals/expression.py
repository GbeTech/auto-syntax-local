from src.utils import ignore
# from src.utils.internals_utils import log_methods

from src.operators import Operator


# noinspection PyUnresolvedReferences,PyAttributeOutsideInit
# @log_methods
class Expression:

    def __init__(self, clp, is_indented, used_keyword=None):
        self.operator: Operator
        self.l_side = None
        self.r_side = None
        self.items_raw = []
        self.set_equation_sides(clp)
        self.set_operator_and_items(used_keyword)
        with ignore(AttributeError):
            # Class and Def ops. have `set_is_within_class`
            self.operator.set_is_within_class(is_indented)

        if self.l_side:
            if not self.operator.assignment_possible:
                return
        self.operator.construct_atoms(self.items_raw)
        self.r_side = self.operator.handle_atoms()

    def set_equation_sides(self, clp):
        """Set l_side if '=' in `clp`, anyway set r_side"""
        if '=' in clp:
            self.l_side, _, self.r_side = map(lambda x: x.strip(),
                                              clp.partition('='))
            return
        self.r_side = clp

    def set_operator_and_items(self, used_keyword):
        # is_indented = self._remove_indentations()
        if used_keyword:
            breakpoint()
            items = self.r_side.split()
        else:
            used_keyword, *items = self.r_side.split()
        self.operator = Operator.by_keyword(used_keyword)
        self.items_raw = items

    # with ignore(AttributeError):
    # 	self.operator.set_is_within_class(is_indented)

    def _remove_indentations(self):
        unchanged = self.r_side[:]
        while self.r_side.startswith('\t'):
            self.r_side = self.r_side[1:]
        else:
            while self.r_side.startswith('    '):
                self.r_side = self.r_side[4:]
        return unchanged != self.r_side

    def finalize(self):
        if self.l_side:
            return self.l_side + ' = ' + self.r_side
        return self.r_side

    def __str__(self):
        """atoms_results = ', '.join(self.atoms)
        op_type = str(type(self.operator))
        dot_idx = op_type.rindex('.') + 1
        end_idx = op_type.rindex("'")
        return f'Operator:{op_type[dot_idx:end_idx]}, Atoms Results:{atoms_results}, l_side:{self.l_side},
        r_side:{self.r_side}'"""
        return f'Operator:{op_type[dot_idx:end_idx]}'