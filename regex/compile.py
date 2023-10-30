import re
import text

a = re.compile(r"dis(agree|allow|array|connected)")
b = a.search(text.dis)

print(b.group())
print(c)