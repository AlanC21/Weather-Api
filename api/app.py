from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"

    querystring = {"text":"fishermans wharf","language":"en"}

    headers = {
	"X-RapidAPI-Key": "cdeaaf4e02mshffcfe442dc1cba2p14985ajsndb3fa3629176",
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

    response = requests.get(url, headers=headers, params=querystring)

    return render_template('index.html', data=response.json())

if __name__ == '__main__':
    app.run(debug=True)