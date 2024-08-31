import time
import subprocess

print("Starting PBB...")
time.sleep(1)
print("Verifying files...")
time.sleep(3)
print("Checking for systems...")
time.sleep(0.7)
print("Found a system! Booting up...")
time.sleep(0.3)
subprocess.run(["python", "main.py"])