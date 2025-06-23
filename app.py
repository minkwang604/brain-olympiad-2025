from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

def read_data():
    data = []
    file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_score', methods=['POST'])
def get_score():
    name = request.form['name']
    birthdate = request.form['birthdate']

    for row in read_data():
        if row['name'] == name and row['birthdate'] == birthdate:
            award = row['award'] if row['award'] != '없음' else None
            return jsonify({
                'category': row['category'],
                'score': row['score'],
                'award': award
            })
    return jsonify({'score': '없음'})


if __name__ == '__main__':
    app.run(debug=True)
