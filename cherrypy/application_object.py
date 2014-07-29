import cherrypy
import routes


class Handler(object):

    def __call__(self, *argv, **kwargs):
        output = {
            'global_config': app.global_config,
            'app_config': app.app_config,
            'request_config': app.request_config
        }
        return str(output)




class CherryPyApplication(object):

    def __init__(self, global_config, app_config):
        dispatcher = self._setup_routes()
        self._config = app_config
        root_config = self._config['/']
        root_config['request.dispatch'] = dispatcher
        cherrypy.config.update(global_config)
        


    def start(self):
        self._app = cherrypy.tree.mount(None, config=self._config)
        cherrypy.quickstart(self._app)


    @property
    def configuration(self):
        if not cherrypy.request.config:
            return cherrypy.config
        return cherrypy.request.config

    @property
    def global_config(self):
        return cherrypy.config


    @property
    def app_config(self):
        return self._app.config


    @property
    def request_config(self):
        return cherrypy.request.config



    def _setup_routes(self):
        dispatcher = cherrypy.dispatch.RoutesDispatcher()
        handler = Handler()
        dispatcher.connect('root', '/',   Handler())
        dispatcher.connect('root', '/s1', Handler())
        dispatcher.connect('root', '/s2', Handler())
        dispatcher.connect('root', '/s3', Handler())
        return dispatcher



global_configuration = {
                        'global_option': 'global_option'
                        }



configuration = {
    '/':  {
        'handler': 'root',
        'root_option': 'at root'
    },
    '/s1':{
        'handler': 'S1',
        's1_option': 'at s1'
    },
    '/s2':{
        'handler': 'S2',
        's2_option': 'at s2'
    },
    '/s3':{
        'handler': 'S3',
        's3_option': 'at s3'
    },
}
app = CherryPyApplication(global_configuration, configuration)



if __name__=='__main__':
    app.start()