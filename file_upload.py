import cherrypy 
import shutil


class UploadHandler(object):

    def __call__(self, *args, **kwargs):
        fout = file('read.zip', mode='w+b')
        with fout:
            fout.write(cherrypy.request.rfile.read())

        return 'Success!!!'

dispatcher = cherrypy.dispatch.RoutesDispatcher()
dispatcher.connect(name='root', route='/', controller=UploadHandler())
config = {
          '/': {'request.dispatch': dispatcher}}

cherrypy.tree.mount(root=None, config=config)
cherrypy.quickstart(None, config=config)

# application/octet-stream
