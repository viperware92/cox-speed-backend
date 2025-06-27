from flask import Flask, jsonify, send_from_directory
import speedtest
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/speedtest')
def speedtest_api():
    s = speedtest.Speedtest()
    s.get_best_server()
    download_speed = round(s.download() / 1_000_000, 2)
    upload_speed = round(s.upload() / 1_000_000, 2)
    ping = round(s.results.ping, 2)
    return jsonify({
        "download": download_speed,
        "upload": upload_speed,
        "ping": ping
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
