from src.operators import Operator
from src.utils import xnor


class DictOperator(Operator, cls_keywords=('dict', '{}')):
    def __init__(self, used_keyword):
        super().__init__(used_keyword)
        self.canonical = 'dict'
        self.last_atom_subject = ' '  # KEEP THE SPACE

    def handle_atoms(self):
        """last_atom_subject = ''
        if len(atoms) % 2 != 0:
            last_atom_subject = atoms[-1].subject
            atoms = atoms[:-1]"""
        atoms_len = len(self.atoms)
        is_single_atom = atoms_len == 1
        if not is_single_atom and atoms_len % 2 != 0:
            self.last_atom_subject += self.atoms[-1].subject
            self.atoms = self.atoms[:-1]

        if is_single_atom:
            condition = lambda a: a.is_dotted
        else:
            condition = lambda a: xnor(a.digit_or_builtins_or_self(),
                                       a.is_dotted)
        for atom in self.atoms:
            atom.parenthesize_builtins()
            if condition(atom):
                dblquote = False
                atom.stringify_subject(dblquote)
            atom.close_parenthesis(around=atom.subject)

        if is_single_atom:
            return f'{self.canonical}({self.atoms[0].result})'
        return self._convert()

    def _convert(self):
        r_side = ''

        extend_with = lambda target, ex: f'{target}{ex} '
        for idx, atom in enumerate(self.atoms):
            r_side += extend_with(target=atom.result,
                                  ex=':' if idx % 2 == 0 else ',')

        converted = extend_with(target=f'{{{r_side.strip()[:-1]}}}', ex=self.last_atom_subject)

        return converted.strip()