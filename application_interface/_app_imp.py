


class Application(object):


    def __init__(self):
        self._settings = []


    def add_settings(self, settings):
        setting = 'Adding settings: ' + str(settings) + ' to ' + str(self)
        print setting
        self._settings.append(setting)


    def show_settings(self):
        print 'Showing all settings:'
        for setting in self._settings:
            print setting