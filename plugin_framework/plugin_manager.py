import os
import json
class PluginManager:
    def __init__(self):
        self._plugins = list()
    
    def install(self, path):
        # path.replace(os.path.sep, ".")
        from plugins.first_plugin.plugin import FirstPlugin
        with open("./plugins/first_plugin/spec.json", "r") as fp:
            specification = json.load(fp)
            fp = FirstPlugin(specification)
            fp.enabled = False
            self._plugins.append(fp)
            self.enable(fp.symbolic_name)
    
    def uninstall(self, symoblic_name):
        return False

    def enable(self, symoblic_name):
        for plugin in self._plugins:
            if (plugin.symbolic_name == symoblic_name) and (plugin.enabled is False):
                plugin.enabled = True
                plugin.activate()
                return True
        return False

    def disable(self, symoblic_name):
        for plugin in self._plugins:
            if plugin.symbolic_name == symoblic_name and plugin.enabled is True:
                plugin.enabled = False
                return True
        return False