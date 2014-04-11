

add_settings = None
app = None


class Application(object):


    def __init__(self):
        global app;
        global add_settings
        if app: return
        app = self
        add_settings = self.add_settings 


    def add_settings(self, settings):
        print 'Adding settings: ' + str(settings) + ' to ' + str(self)