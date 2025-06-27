from flask import Flask, jsonify
import speedtest
import os

app = Flask(__name__)

@app.route('/api/speedtest')
def speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # Convert to Mbps
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        return jsonify({
            'download': round(download, 2),
            'upload': round(upload, 2),
            'ping': round(ping, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
