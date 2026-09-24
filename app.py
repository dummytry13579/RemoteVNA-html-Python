from flask import Flask, render_template, request, jsonify
import pyvisa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_scpi', methods=['POST'])
def send_scpi():
    data = request.json
    resource_str = data.get('address', '').strip()
    command = data.get('command', '').strip()

    if not resource_str or not command:
        return jsonify({'status': 'error', 'response': 'VISA Resource Address and Command are required.'}), 400

    try:
        rm = pyvisa.ResourceManager()
        # Open connection with a 5-second timeout
        with rm.open_resource(resource_str, timeout=5000) as instrument:
            # Query if command ends with '?', else write
            if command.endswith('?'):
                response = instrument.query(command)
            else:
                instrument.write(command)
                response = "Command sent successfully."

            return jsonify({'status': 'success', 'response': response.strip()})

    except Exception as e:
        return jsonify({'status': 'error', 'response': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)