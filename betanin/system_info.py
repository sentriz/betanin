# standard library
import platform

# betanin
from betanin import version


SYSTEM_INFO = {
    "platform": platform.platform(),
    "python_version": platform.python_version(),
    "betanin_version": version.__version__,
}
