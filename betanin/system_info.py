# standard library
import platform

# betanin
from betanin import paths


VERSION = ""
with open(paths.VERSION_PATH, "r") as version_file:
    VERSION = f"v{version_file.read()}"


SYSTEM_INFO = {
    "platform": platform.platform(),
    "python_version": platform.python_version(),
    "betanin_version": VERSION,
}
