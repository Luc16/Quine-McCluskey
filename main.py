import datetime
import Quine_McCluskey as qm

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    #qm_test = qm.quine_mccluskey(2, [[0, 1], [1, 1]])

    return render_template('initial_page.html')


@app.route('/results', methods=['POST', 'GET'])
def root1():
    if request.method == 'POST':
        result = request.form
        nvar = int(result['nvar'])
        table_ones = result['truth_table']
        table_output = result['table_output']
        handle = qm.handle_input(nvar, table_ones, table_output)
        qm_test = qm.num_to_letter(nvar, qm.quine_mccluskey(nvar, handle))
        return render_template("results.html", qm=qm_test)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)