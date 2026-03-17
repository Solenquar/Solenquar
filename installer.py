
import subprocess
import tempfile
import urllib.request
import urllib.error
import sys

url = "https://yourstoragespace.ca/YCFn9BMaxiTGrcnNoqA6gEfNRppwsaPE/release_installer.txt"

try:
    with urllib.request.urlopen(url) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        text = response.read().decode(charset, errors="replace")
except urllib.error.URLError as e:
    print(f"Failed to download {url}: {e}")
    sys.exit(1)

try:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as f:
        f.write(text)
        filename = f.name
except OSError as e:
    print(f"Failed to write temp file: {e}")
    sys.exit(1)

subprocess.Popen(["notepad.exe", filename])
