# RemoteVNA-html-Python
Example of remote connectivity to Keysight's VNA instrument. the front end will be running on the web browser using localhost::5000 after running the python (app.py) code.
The placement of the file should be 
|- {folder}
  |- app.py
  |- templates
    |- index.html

Steps to run:
1. user will need to run the app.py using command prompt "python app.py"
2. go to web browser and type in "localhost:5000" OR "127.0.0.1:5000"
3. Key in the instrument remote hislip VISA address
4. type in SCPI command and send to instrument

link to walkthru video 
