import glob
from pathlib import Path
from . import client
import sys
import logging
import importlib
from pathlib import Path

path = "userbot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        pathq = Path(a.name)
        plugin_name = pathq.stem
        load_plugins(plugin_name.replace(".py", ""))

def load_plugins(plugin_name):
    path = Path(f"userbot/modules/{plugin_name}.py")
    name = "userbot.modules.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["userbot.modules." + plugin_name] = load
    print("Successfully loaded all plugins ...")

print("Started..!")

if __name__ == "__main__":
    bot.run_until_disconnected()
