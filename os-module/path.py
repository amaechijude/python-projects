import os
abs_path = os.path.abspath('main.py')
print(f"The absolute path is: {abs_path}")

print(os.path.isabs(abs_path))
print(f"{os.path.getsize(abs_path)} bytes")