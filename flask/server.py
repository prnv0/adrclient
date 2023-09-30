from flask import Flask, request, jsonify
from flask_cors import CORS
import fitz 

app = Flask(__name__)

# Configure CORS to allow requests from your React app's origin
CORS(app)

@app.route('/concatenate', methods=['POST'])
def concatenate_strings():
    data = request.get_json()
    name = data.get('string1', '')
    prescription = data.get('string2', '')
    doc = fitz.open("Records\\"+name+".pdf")
    all_text = ""
    for page in doc:
        all_text += page.get_text() + chr(12)
    print(all_text.splitlines())
    splittext=all_text.splitlines()
    s=splittext.index("Additional Notes")
    prompt=splittext[4]+"|"+splittext[5]+"|"+splittext[23]+"|"+splittext[24]+"|"
    for i in range(s+3, len(splittext)-3):
        prompt+=splittext[i]+" "+prescription
    print(prompt)
    return jsonify({'result': prompt})

if __name__ == '__main__':
    app.run(debug=True)
