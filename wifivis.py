import subprocess
from multiprocessing import Process, Queue
from flask import Flask
from parse_lib import parse
import json

testgraph = {
    "11:22:33:44:55" : {
        "weight" : 1.0,
        "x" : 0.5,
        "y" : 0.5,
        "edges" : {
            "12:34:56:67:90" : 1.0,
            "aa:bb:cc:dd:ff" : 10.0,
            "aa:11:bb:22:cc" : 2.0,
            "ab:bc:cd:de:ef" : 2.0,
        }
    },
    "12:34:56:67:90" : {
        "weight" : 0.3,
        "x" : 0.1,
        "y" : 0.1,
        "edges" : {
            "aa:bb:cc:dd:ff" : 10.0,
        }
    },
    "aa:bb:cc:dd:ff" : {
        "weight" : 0.3,
        "x" : 0.1,
        "y" : 0.7,
        "edges" : {
        }
    },
    "aa:11:bb:22:cc" : {
        "weight" : 0.5,
        "x" : 0.7,
        "y" : 0.8,
        "edges" : {
        }
    },
    "ab:bc:cd:de:ef": {
        "weight" : 0.1,
        "x" : 0.9,
        "y" : 0.2,
        "edges" : {
        }
    }   
}   
    

def frontend(q):
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        with open("ui.js") as f: js = f.read()
        with open("ui.css") as f: css = f.read()
        
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
                <title>wifivis</title>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
                <style type="text/css">
        ''' +  css + '''       
                </style>
                <script type="text/javascript">
        ''' + js + '''
                </script>
            </head>
            
            <body id="main">
            
            </body>
        </html>
        '''
        
    @app.route('/dynamic')
    def ajax():
        update = q.get()
        return json.dumps(testgraph)

    app.run()
    
    
def backend(q):
    

    def store(packet):
        pass
    p = subprocess.Popen("cat dump", #"sudo tcpdump --monitor-mode -i mon0 -e", 
                         shell=True, stdout=subprocess.PIPE)

    while True:
        l = p.stdout.readline()
        if not l:
            return
        packet = parse(str(l))
        print(packet.ptype)
        store(packet)
        
if __name__ == '__main__':
    q = Queue(maxsize=1)
    back_p  = Process(target=backend, args=(q,))
    front_p = Process(target=frontend, args=(q,))
    back_p.start()
    front_p.start()
    back_p.join()
    front_p.join()

    
