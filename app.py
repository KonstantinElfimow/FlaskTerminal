# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

data = None


@app.route('/', methods=['GET'])
def index():
    global data
    error = None
    user = {'username': 'Konstantin'}
    if request.method == 'GET':
        query = request.args.get('command')
        if query and query != '':
            #if query.strip() == 'kill':
            #    return render_template('index.html', title='Home', user=user)

            parsed_query = list(filter(lambda x: x != ' ', query.split()))
            print(parsed_query)
            try:
                process = subprocess.Popen(query, cwd=os.getcwd(), stdout=subprocess.PIPE, text=True)
                data = process.stdout.read().splitlines()
                #print(data)
            except subprocess.CalledProcessError as e:
                error = f"Ошибка команды {e.cmd}!"
            return render_template('index.html', error=error, data=data)
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run(debug=True)
