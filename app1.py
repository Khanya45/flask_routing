from flask import Flask
app = Flask(__name__)
from flask import redirect
from flask import url_for


@app.route('/user/<name>')
def index_page(name):
    if name == "khanya":
        return redirect(url_for('admin_page', name=name))
    else:
        return redirect(url_for('guest_page', name=name))


@app.route('/admin/<name>')
def admin_page(name):
    return 'I am the admin. My name is %s' %name


@app.route('/guest/<name>')
def guest_page(name):
    return 'I am on the guest page. My name is %s' %name


@app.route('/payment/<int:salary>')
def projects_page(salary):
    if salary < 10500.50:
        return redirect('https://www.sahomeloans.com/')
    else:
        return redirect('https://www.fnb.com/')


if __name__ == '__main__':
    app.debug = True
    app.run()
