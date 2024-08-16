from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Database connection details
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

@app.route('/')
def student_form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    grade = request.form['grade']
    email = request.form['email']

    cursor = db.cursor()
    sql = "INSERT INTO students (name, grade, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, grade, email))
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
