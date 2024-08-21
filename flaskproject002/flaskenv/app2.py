
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
       
        return f"Name: {name}, Email: {email}"
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
