from flask import Flask, jsonify

app = Flask(name)

@app.route('/status')
def status():
    return jsonify({"status": "Logistics API Running"})

if name == 'main':
    app.run(debug=True)
