import re
capitals = "AminaSamalSymbatBestFriends"
x = re.sub(r'(?<!^)(?=[A-Z])', '_', capitals)
print(x)