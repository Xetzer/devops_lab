'''Simple script to get python info'''
import sys
import subprocess
import json
import yaml

jfile = "pyinfo.json"
yfile = "pyinfo.yaml"

python_ver = subprocess.getoutput("python -V")
virt_env = subprocess.getoutput("pyenv version-name")
exec_loc = sys.executable
pip_loc = subprocess.getoutput("which pip")
#pyth_path = sys.exec_prefix
pyth_path = subprocess.getoutput("echo $VIRTUAL_ENV")
site_pack = next(p for p in sys.path if "site-packages" in p)
inst_pack = subprocess.getoutput("pip freeze")

print(("Python version: {0}\nVirtual environment: {1}\nExecutable location: {2}\nPip location: {3}\nPYTHONPATH: {4}\nSite packages location: {5}\nInstalled packages:\n{6}\n").format(python_ver, virt_env, exec_loc, pip_loc, pyth_path, site_pack, inst_pack))
print(jfile + " and " + yfile + " files will be created.")

freeze = inst_pack.replace('==', ' ').replace('\n', ' ').split()
pckgs = freeze[0:][::2]
vers = freeze[1:][::2]
inst = dict(zip(pckgs, vers))

ddic = {'Python version': python_ver,
        'Virtual environment': virt_env,
        'Executable location': exec_loc,
        'Pip location': pip_loc,
        'PYTHONPATH': pyth_path,
        'Site packages location': site_pack,
        'Installed packages': {}}
ddic['Installed packages'] = inst

with open(jfile, 'w') as gi:
    gi.write(json.dumps(ddic, indent=4, sort_keys=False))

with open(yfile, 'w') as joe:
    joe.write(yaml.dump(ddic, default_flow_style=False))
