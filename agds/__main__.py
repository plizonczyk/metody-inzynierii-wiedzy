from .agds_helpers import AGDSHelpers
from .agds import AGDS

data_file = 'agds/data.txt'

agds = AGDS(data_file)
h = AGDSHelpers(agds)

print(h.filter_single_param('leaf-length', 1, 10))

print(h.filter_multi_param([('leaf-length', 4.6, 5.1), ('leaf-width', 3.1, 3.5)]))


