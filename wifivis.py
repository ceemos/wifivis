from __future__ import print_function
import subprocess
from multiprocessing import Process, Queue
from flask import Flask


def frontend(q):
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        with open("ui.js") as f: js = f.read()
        with open("ui.css") as f: css = f.read()
        
        return '''
        <html>
            <head>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
                <style "type=text/css">
        ''' +  css + '''       
                </style>
                <script type="text/javascript">
        ''' + js + '''
                </script>
            </head>
            
            <body>
            
            </body>
        </html>
        '''
    
    
    app.run()
    
    
def backend(q):

    def parse(line):
        print(line)


    def store(packet):
        pass
# 
    p = subprocess.Popen("cat dump", #"sudo tcpdump --monitor-mode -i mon0 -e", 
                         shell=True, stdout=subprocess.PIPE)

    while True:
        l = p.stdout.readline()
        if not l:
            return
        packet = parse(l)
        store(packet)
        
if __name__ == '__main__':
    q = Queue()
    back_p  = Process(target=backend, args=(q,))
    front_p = Process(target=frontend, args=(q,))
    back_p.start()
    front_p.start()
    back_p.join()
    front_p.join()

    
