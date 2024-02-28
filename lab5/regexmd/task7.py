import re

name = 'AminaMuratbek'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)
