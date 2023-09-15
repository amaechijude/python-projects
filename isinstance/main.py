items = ["Name", "Age", 23, 45.54, 67, 32.21]
for item in items:
    if isinstance(item, int):
        print(item, type(item))

for item in items:
    if isinstance(item, float):
        print(item, type(item))

for item in items:
    if isinstance(item, str):
        print(item, type(item))
