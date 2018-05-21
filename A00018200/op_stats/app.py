from flask import Flask
import sys
sys.path.append('/home/so-exam3/A00018200')
from op_stats.stats import Stats 
import json

app=Flask(__name__)

@app.route('/v1/stats/cpu')
def get_cpu():
    cpu=Stats.get_cpu()
    return json.dumps({'cpu_percent' : cpu})

@app.route('/v1/stats/memory')
def get_memory():
    memory=Stats.get_memory()
    return json.dumps({'memory_percent': memory})

@app.route('/v1/stats/disk')
def get_disk():
    disk=Stats.get_disk()
    return json.dumps({'disk_percent' : disk})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)

