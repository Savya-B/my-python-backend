from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

if __name__ == '__main__':
    app.run()
    
from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/server-health")
def server_health():
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent
    status = 100 - max(cpu, ram)
    return {
        "name": "Render Backend Server",
        "status": status,
        "cpu": cpu,
        "ram": ram
    }
