import psutil
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
  cpu_percent=psutil.cpu_percent()
  mem_percent=psutil.virtual_memory().percent
  cpu_metric = cpu_percent
  mem_metric = mem_percent
  Message=None
  if cpu_percent>80 or mem_percent>80:
    Message="High CPU or Memory Utilization detected. Please scale up"
  return render_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent,cpu_metric=cpu_metric,mem_metric=mem_metric,message=Message)
if __name__ =='__main__':
  app.run(debug=True, host='0.0.0.0')