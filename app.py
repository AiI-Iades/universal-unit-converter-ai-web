from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    value = data.get('value')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')

    result = subprocess.run([
        'universal-unit-converter-ai',
        '--value', str(value),
        '--from-unit', from_unit,
        '--to-unit', to_unit
    ], capture_output=True, text=True)

    return jsonify({
        'result': result.stdout.strip(),
        'error': result.stderr.strip()
    })

if __name__ == '__main__':
    app.run(debug=True)