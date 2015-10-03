from __future__ import print_function
import subprocess
from multiprocessing import Process, Queue
from flask import Flask
from parse_lib import parse

def frontend(q):
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return 'Hello World!'
    
    app.run()
    
    
def backend(q):



    def store(packet):
        pass
# 
    p = subprocess.Popen("cat dump ", 
                         shell=True, stdout=subprocess.PIPE)

    while True:
        l = p.stdout.readline()
        if not l:
            return
        packet = parse(str(l))
        print(packet.ptype)
        store(packet)
        
if __name__ == '__main__':
    q = Queue()
    back_p  = Process(target=backend, args=(q,))
    front_p = Process(target=frontend, args=(q,))
    back_p.start()
    front_p.start()
    back_p.join()

    
