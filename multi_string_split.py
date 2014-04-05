
import ConfigParser

config = '''
[section]
value=foo
other=bar
finally=zap

%include .\foo.ini
'''
class ConfigEmulator(object):

    def __init__(self, ini_str):
        ini_str = ini_str.strip()
        self._lines = ini_str.split('\n')


    def readline(self):
        if self._lines:
            return self._lines.pop(0)
        


fd = ConfigEmulator(config)

parser = ConfigParser.ConfigParser()
parser.readfp(fd)
for item in parser.items('section'):
    print item