
import subprocess

subprocess.call(["git", "init", "-b", "main"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "Initial commit"])
