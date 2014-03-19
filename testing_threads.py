import threading
import time

class ThreadedOutput(threading.Thread):

    def __init__(self, count):
        self._count = count
        super(ThreadedOutput, self).__init__()


    def run(self):
        
        with file('tmp{seq}.txt'.format(seq=self._count), 'w') as fout:
            seq = [str(i) for i in range(1000000)]
            output = '\n'.join(seq)
            fout.write(output)
        time.sleep(1)
        print '\nThread: ' + str(self._count)



def run_threading_test():
    print 'Starting threaded output....'
    for i in range(10):
        to = ThreadedOutput(i)
        to.start()
    print '\nAll threads triggered....'


if __name__=='__main__':
    run_threading_test()