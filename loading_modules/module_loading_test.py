import imp
import os.path
import sys


def load_script(filename):
    path, module_name, ext = _extract_script_components(filename)
    sys.path.append(path)
    return _load_module(module_name)
    


def _extract_script_components(filename):
    path = os.path.dirname(filename)
    base_name = os.path.basename(filename)
    module_name, ext = os.path.splitext(base_name)
    return path, module_name, ext


def _load_module(module_name):
    file, pathname, description = imp.find_module(module_name)
    module = imp.load_module(module_name, file, pathname, description)
    file.close()
    return module



print 'Starting proces....'
script_to_load = 'lib_module.py'
full_path_to_script = os.path.abspath(script_to_load)
print 'Loading ' + full_path_to_script + '....'
test = load_script(full_path_to_script)
test.echo()