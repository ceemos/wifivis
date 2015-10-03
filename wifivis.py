import subprocess
from multiprocessing import Process, Queue
from flask import Flask
from function_lib import parse
from function_lib import store
import json
from time import clock, sleep
from decay import decay

'''testgraph = {
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
}  ''' 
    

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
                <script src="http://code.jquery.com/color/jquery.color-2.1.0.min.js"></script>
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
        return json.dumps(update)

    app.run()
    
    
def backend(q):
    
    lasttime = clock()

    dictionary = {}
    p = subprocess.Popen("sudo tcpdump --monitor-mode -i mon0 -e", 
                         shell=True, stdout=subprocess.PIPE)

    while True:
        l = p.stdout.readline()
        if not l:
            return
        packet = parse(str(l))
        print(packet.ptype)
        store(packet, dictionary)
        currenttime = clock()
        print(currenttime-lasttime)
        if (currenttime - lasttime) > 0.003:
            dictionary = decay(dictionary, currenttime-lasttime)
            print("sending update")
            lasttime = currenttime
            graph = {key:value.__dict__ for key,value in dictionary.items()}
            q.put(graph)

if __name__ == '__main__':
    q = Queue(maxsize=1)
    back_p  = Process(target=backend, args=(q,))
    front_p = Process(target=frontend, args=(q,))
    back_p.start()
    front_p.start()
    back_p.join()
    front_p.join()
    #backend(q)

    
