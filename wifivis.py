import subprocess
from multiprocessing import Process, Queue
from flask import Flask
from function_lib import parse
from function_lib import store
import json
from time import clock, sleep


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
        return json.dumps(update)

    app.run()
    
    
def backend(q):
    
    lastpack = clock()

    dictionary = {}
    p = subprocess.Popen("cat dump", #"sudo tcpdump --monitor-mode -i mon0 -e", 
                         shell=True, stdout=subprocess.PIPE)

    while True:
        l = p.stdout.readline()
        sleep(0.1)
        if not l:
            return
        packet = parse(str(l))
        print(packet.oui_SA)
        print(packet.oui_DA)
        print(packet.name_sender)
        store(packet, dictionary)
        currenttime = clock()
        print(currenttime-lastpack)
        if (currenttime - lastpack) > 0.001:
            print("sending update")
            lastpack = currenttime
            store(packet,dictionary)
            graph = {key:value.__dict__ for key,value in dictionary.items()}
            q.put(graph)

if __name__ == '__main__':
   q = Queue(maxsize=10)
   back_p  = Process(target=backend, args=(q,))
   front_p = Process(target=frontend, args=(q,))
   back_p.start()
   front_p.start()
   back_p.join()
   front_p.join()
   backend(q)

    
