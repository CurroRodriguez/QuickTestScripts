import cherrypy
import json



def handle_error(status, message, traceback, version):

    response = {
            'status': status,
            'message': message,
            'traceback': traceback,
            'version': version
        }
    return json.dumps(response)
    




class ExceptionTestingHandler(object):

    _cp_config = {'request.error_response': handle_error}

    @cherrypy.expose
    def index(self):
        #return 'running....'

        raise cherrypy.HTTPError(404, message='foo')





config = {'error_page.default': handle_error}
cherrypy.config.update(config)
cherrypy.quickstart(ExceptionTestingHandler())