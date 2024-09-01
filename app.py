from flask import Flask, request, jsonify
from pymodbus.client import ModbusTcpClient

app = Flask(__name__)

client = ModbusTcpClient('192.168.1.1', port=502)

def get_charging_status():
    result = client.read_coils(1, 1)  # Reading the coil controlling charging
    if not result.isError():
        return result.bits[0]  # True if charging, False otherwise
    return None

@app.route('/charging-status', methods=['GET'])
def charging_status():
    status = get_charging_status()
    if status is not None:
        return jsonify({'charging': status})
    else:
        return jsonify({'error': 'Could not retrieve status'}), 500

if __name__ == '__main__':
    app.run(debug=True)
