from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    data = [63, 70, 74, 76, 85, 89, 93, 99, 105, 111, 113, 117]
    return render_template(
        template_name_or_list='index.html',
        data=data,
        labels=labels,
    )


@app.route('/more')
def more():
    return render_template('more.html')


if __name__ == '__main__':
 app.run(debug=True)