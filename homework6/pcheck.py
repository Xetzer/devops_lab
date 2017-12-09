'''Simple script to get python info'''
import sys
import subprocess
from platform import python_version
import json
import yaml

json_file = "pyinfo.json"
yaml_file = "pyinfo.yaml"

version = python_version()
virt_env = subprocess.getoutput("pyenv version-name")
executable = sys.executable
pip_location = subprocess.getoutput("which pip")
python_path = sys.exec_prefix
pack_location = next(p for p in sys.path if "site-packages" in p)
pip_freeze = subprocess.getoutput("pip freeze")

print(("Python version: {0}\n"
       "Virtual environment: {1}\n"
       "Executable location: {2}\n"
       "Pip location: {3}\n"
       "PYTHONPATH: {4}\n"
       "Site packages location: {5}\n"
       "Installed packages:\n{6}\n").format(version, virt_env, executable, pip_location,
                                            python_path, pack_location, pip_freeze))
print(("{0} and {1} files will be created.\n").format(json_file, yaml_file))

temp_list = pip_freeze.replace("==", " ").replace("\n", " ").split()
packages = temp_list[0:][::2]
versions = temp_list[1:][::2]
installed = dict(zip(packages, versions))

dictionary = {"Python version": version,
        "Virtual environment": virt_env,
        "Executable location": executable,
        "Pip location": pip_location,
        "PYTHONPATH": python_path,
        "Site packages location": pack_location,
        "Installed packages": {}}
dictionary["Installed packages"] = installed

with open(json_file, "w") as json_out:
    json_out.write(json.dumps(dictionary, indent=4, sort_keys=False))

with open(yaml_file, "w") as yml_out:
    yml_out.write(yaml.dump(dictionary, default_flow_style=False))
