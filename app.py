import openai
from flask import Flask
from flask import request
from flask import render_template
from config import oai_apikey

app = Flask(__name__)
openai.api_key = oai_apikey


@app.route("/")
def inicio():

    return render_template('index.html')


@app.route("/hello_openai", methods=['POST', 'GET'])
def pregunta_al_doctor():

    error = None

    if request.method == 'POST':

        hello = request.form['hello']

        text = "Generate a hello world message based in {}.".format(
            hello
        )

        respuesta = openai.Completion.create(

            engine="text-davinci-003",

            prompt=text,

            max_tokens=3800

        )

        resp = respuesta["choices"][0]["text"]

        return render_template('response.html', resp=resp)

    else:

        return"Tus Muertos"


if __name__ == "__main__":

    app.run(debug=True)
