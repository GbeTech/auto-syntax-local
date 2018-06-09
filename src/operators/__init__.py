# autosyntax\src\operators\__init__.py
from .Operators import Operator
from .def_operator import DefOperator
from .class_operator import ClassOperator
from .dict_operator import DictOperator
from .for_operator import ForOperator
from .listcomp_operator import ListCompOperator
from .print_operator import PrintOperator
from .str_operator import StrOperator

# IS used in class_operator
# from src.internals import (Atom, Indentation,
#                            TypedAtom, atom_factory,
#                            BUILTIN_FUNCTIONS, BUILTIN_TYPES, MAGIC_FUNCTIONS)
# from src.utils import ignore, surround_with, get_singular, xnor
