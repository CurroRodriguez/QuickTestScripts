import cherrypy
import json



def handle_error(status, message, traceback, version):
    tb = [line for line in traceback.split('\n')]
    response = {
            'status': status,
            'message': message,
            'traceback': tb,
            'version': version
        }
    return json.dumps(response)
    




class ExceptionTestingHandler(object):

    @cherrypy.expose
    def index(self):
        #return 'running....'

        raise cherrypy.HTTPError(404, message='foo')





config = {'error_page.default': handle_error}
cherrypy.config.update(config)
cherrypy.quickstart(ExceptionTestingHandler())