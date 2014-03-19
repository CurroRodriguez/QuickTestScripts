'''
Testing:

In order to test this script, run it through the debugger or by invoking
python file_upload.py. With the local server running, you can use curl.exe
to post a file (expecting a ZIP file) with the following command line::

    curl.exe -X POST -H "Content-Type: application/octet-stream" --data-binary "@large_test.zip" http://localhost:8080

Notice the file name is surrounded by quotes and prefixed with an '@' sign.
'''
import cherrypy 
import shutil


class UploadHandler(object):

    def __call__(self, *args, **kwargs):
        with file('result.zip', mode='w+b') as fout:
            #body = cherrypy.request.rfile
            body = cherrypy.request.body
            if body:
                fout.write(body.read())


        return 'Success!!!'

dispatcher = cherrypy.dispatch.RoutesDispatcher()
dispatcher.connect(name='root', route='/', controller=UploadHandler())
config = {
          '/': {'request.dispatch': dispatcher}}

cherrypy.tree.mount(root=None, config=config)
cherrypy.quickstart(None, config=config)

# application/octet-stream
