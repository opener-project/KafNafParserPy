import os
import sys

from distutils.core import setup

# Get all the directories for the package that lazy way. This way we don't have
# to also manually update that list.
this_folder  = os.path.dirname(os.path.realpath(__file__))
lib_name     = 'KafNafParserPy'
lib_dir      = os.path.join(this_folder, lib_name)
directories  = [lib_name]
python_files = []

for name in os.listdir(lib_dir):
    full_path = os.path.join(lib_name, name)

    # Gather all the directories.
    if os.path.isdir(full_path):
        directories.append('%s.%s' % (lib_name, name))

    # Gather all the Python files.
    else:
        path, ext = os.path.splitext(full_path)
        basename = os.path.basename(path)

        if ext == '.py':
            python_files.append('%s.%s' % (lib_name, basename))

setup(
    name         = lib_name,
    version      = '1.5',
    description  = 'Parser between KAF and NAF',
    author       = 'Ruben Izquierdo',
    url          = 'https://github.com/cltl/KafNafParserPy',
    author_email = 'r.izquierdobevia@vu.nl',
    packages     = directories,
    py_modules   = python_files
)
