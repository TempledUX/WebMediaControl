from flask import Flask, render_template
import pyautogui
import qrcode
import socket
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pause')
def pause():
    print("Pause")
    pyautogui.press('playpause')
    return 'OK'

@app.route('/forward')
def forward():
    print("Forward")
    pyautogui.press('nexttrack')
    return 'OK'

@app.route('/backward')
def backward():
    print("Backward")
    pyautogui.press('prevtrack')
    return 'OK'

@app.route('/mute')
def mute():
    print("Muted")
    pyautogui.hotkey('volumemute')
    return 'OK'

if __name__ == "__main__":
    #Generate qrcode link
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    local_ip = s.getsockname()[0]
    img = qrcode.make(f'http://{local_ip}:5000')
    plt.figure()
    plt.imshow(img)
    plt.show()
    app.run(host='0.0.0.0')
