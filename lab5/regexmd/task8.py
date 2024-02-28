import re
f = r'[A-Z][a-z]*'
capitals = "AminaMuratbekAskarkyzy"
x = re.findall(f, capitals)
print(x)