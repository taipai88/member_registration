from flask import Flask, render_template, request, url_for
import sqlite3, os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# 建立資料表
def init_db():
    conn = sqlite3.connect('members.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS members (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 member_id TEXT NOT NULL,
                 name TEXT NOT NULL,
                 dob TEXT,
                 address TEXT,
                 photo_path TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        member_id = request.form['member_id']
        name = request.form['name']
        dob = request.form['dob']
        address = request.form['address']
        photo = request.files['photo']

        filename = None
        if photo and photo.filename:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn = sqlite3.connect('members.db')
        c = conn.cursor()
        c.execute("INSERT INTO members (member_id, name, dob, address, photo_path) VALUES (?, ?, ?, ?, ?)",
                  (member_id, name, dob, address, filename))
        conn.commit()
        conn.close()
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_id = request.form['search_id'].strip()
    conn = sqlite3.connect('members.db')
    c = conn.cursor()

    if search_id == "":
        c.execute("SELECT member_id, name, dob, address, photo_path FROM members")
        results = c.fetchall()
        result = None
    else:
        c.execute("SELECT member_id, name, dob, address, photo_path FROM members WHERE member_id = ?", (search_id,))
        result = c.fetchone()
        results = None

    conn.close()
    return render_template('index.html', result=result, results=results, search_id=search_id)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
