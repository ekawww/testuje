from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

sekretarki = {
    'DAWN BRITTAIN': {'imiona': ["aderinto", "lewis", "grogan", "vijayanand", "jones", "smith", "venkatesh", "DAWN", "BRITTAIN"], 'miejsce': (5, 6)},
    'JAYNE THOMPSON': {'imiona': ["jameison", "verma", "parmer", "james", "orme", "conroy", "wright", "jung", "JAYNE", "THOMPSON"], 'miejsce': (7, 6)},
    'VICKI SHORT RB ': {'imiona': ["budgen", "turton", "del", "galdo", "whitwell", "grace", "dugdale", "peacey", "sinha", "kattan", "VICKI", "SHORT","hussain", "barr", "BELL", "RACHEL"], 'miejsce': (1, 6)},
    'LYNN HARRISON': {'imiona': ["sagar", "toogood", "smith", "halstead", "LYNN", "HARRISON"], 'miejsce': (7, 5)},
    'ELAINE INGHAM': {'imiona': ["wall", "campbell", "riyat", "sood", "ELAINE", "INGHAM"], 'miejsce': (3, 6)},
    'KEZIAH O TOOLE': {'imiona': ["kelly", "rawes", "shetty", "tay", "tulwa", "holton", "KEZIAH", "TOOLE"], 'miejsce': (2, 6)},
    'CARDIOLOGY': {'imiona': ["sapsford", "schlosshan", "malkin"], 'miejsce': (1, 5)},
    'JANINE CULLEY': {'imiona': ["kayes", "khan", "turner", "JANINE", "CULLEY"], 'miejsce': (4, 6)},
    'ALEX APPLEYARD': {'imiona': ["russell", "serela","ALEX", "APPLEYARD"], 'miejsce': (7, 5)},
    'AMY STOTT': {'imiona': ["kimuli", "stables", "hackney", "monkhouse", "AMY", "STOTT"], 'miejsce': (5, 6)},
    'RACHEL BELL': {'imiona': ["hussain", "barr", "BELL", "RACHEL"], 'miejsce': (5, 6)},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.json.get('name')
    for secretary, data in sekretarki.items():
        if any(name.lower() in i.lower() for i in data['imiona']):
            return jsonify(secretary=secretary, location=data['miejsce'], names=data['imiona'])
    return jsonify(secretary="OUTPATIENTS", location=(1, 4), names=[])

if __name__ == '__main__':
    app.run(debug=True)
