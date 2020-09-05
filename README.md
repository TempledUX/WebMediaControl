# WebMediaControl
Web interface for sending media control events to the server.

Simple Web UI for sending media callbacks to the server. The python script uses flask for setting up a local web server to which other devices in the local network can connect and receive the UI data using a web browser. The script first generates a QR Code with the server machine private IP so a smartphone can read it and open a connection in the web browser, after that the flask local server is setted up. 

The web UI uses ajax for sending the media callbacks, the server receives the call and executes code based in pyautogui which simulates the media control pulsation (mediaforward, mediabackward, mediamute).
