#!B:\redstar\venv-redstar\3.6\windows\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'datadog==0.14.0','console_scripts','dog'
__requires__ = 'datadog==0.14.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('datadog==0.14.0', 'console_scripts', 'dog')()
    )
