import cherrypy
import json
import sys
import traceback


class WrappedException(cherrypy.HTTPError):

    def get_error_page(self, *args, **kwargs):
        return 'foo'.encode('utf-8')






def global_error_handler():
    e_type, e_value, e_tb = sys.exc_info()
    record = {
        "code": 500,
        "type": str(e_type),
        "value": str(e_value)
    }
    cherrypy.response.status = 500
    body = json.dumps(record, encoding='utf-8')
    cherrypy.response.body = body
    




class ExceptionTestingHandler(object):

    @cherrypy.expose
    def index(self):
        #return 'running....'

        raise KeyError('key')







config = {'request.error_response': global_error_handler}
cherrypy.config.update(config)
cherrypy.quickstart(ExceptionTestingHandler())