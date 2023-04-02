from machinetranslation import translator, __init__
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText=translator.english_To_French(textToTranslate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText=translator.french_To_English(textToTranslate)

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
   return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
