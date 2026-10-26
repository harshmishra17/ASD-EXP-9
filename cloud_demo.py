import os
import platform


print("ASD Experiment 9")
print("Student: Harsh Mishra")
print("GitHub: harshmishra17")
print("-" * 45)

print("Operating system:", platform.system())
print("OS release:", platform.release())
print("Architecture:", platform.machine())
print("Python version:", platform.python_version())
print("Working directory:", os.getcwd())

in_codespaces = os.environ.get("CODESPACES") == "true"

print("Running in GitHub Codespaces:", in_codespaces)

if in_codespaces:
    print("Cloud environment verification: SUCCESS")
else:
    print("Codespaces environment variable not detected")