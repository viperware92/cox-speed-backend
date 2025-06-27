from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

@app.route('/api/speedtest')
def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Mbps
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        return jsonify({
            'download': round(download, 2),
            'upload': round(upload, 2),
            'ping': round(ping, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
