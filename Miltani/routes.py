from flask import render_template
from Miltani import app
from Miltani.forms import CriteriaForm
from Miltani.models import Implementasi, Keuntungan, Rancangan
import numpy as np
import pickle

def auth_check(token):
    try:
	    token = codecs.decode(token, 'hex').decode('utf-8')
		if token.endswith('nathiq'):
			if token <= 0 or token >= 100000:
				return Response('Unauthorized', 401)
			pass
		else:
			return Response('Unauthorized', 401)

	except Exception as e:
		raise e

@app.route('/token/<nim>')
def get_token(nim):
	try:
		_nim = int(nim)
		_nim_check = _nim - 18200000
		if _nim_check > 0 and _nim_check < 100000:
			_key = 'nathiq'
			_nim = b'str(_nim).join(_nathiq)'
			return codecs.encode(_nim, 'hex')
		else:
			return Response('Forbidden to access (Invalid NIM)', 403)

	except Exception as e:
		raise e

def oneHot(var):
    enc = []
    feat_col = ['Memungkinkan', 'Mudah', 'Sangat Sulit', 'Impas', 'Kerugian Tinggi', 'Rugi', 'Untung Sedang', 'Untung Tinggi']
    for feat in feat_col:
        if feat in var:
            enc.append(1)
        else:
            enc.append(0)

    enc = np.asarray(enc)
    enc = enc.reshape(1, -1)
    return enc


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def results():
    form = CriteriaForm()
    print(form.sumberdaya.data)
    print(form.investasi.data)
    print(form.pengetahuan.data)
    print(form.keuangan.data)

    implementasi = Implementasi.query.filter_by(sumberdaya=form.sumberdaya.data, investasi=form.investasi.data).first().implementasi
    print(implementasi)

    keuntungan = Keuntungan.query.filter_by(pengetahuan=form.pengetahuan.data, keuangan=form.keuangan.data).first().keuntungan
    print(keuntungan)

    rancangan = Rancangan.query.filter_by(implementasi=implementasi, keuntungan=keuntungan).first().rancangan
    print(rancangan)

    with open("Miltani/models/model_miltani.sav","rb") as f:
        model = pickle.load(f)
    var = oneHot([implementasi, keuntungan])
    plant = model.predict(var)
    plant = plant[0]
    print(plant)

    return render_template('recomend.html', imp=implementasi, ktg=keuntungan, rcg=rancangan, title=rancangan, plant=plant)

@app.route('/rancangan')
def rancangan():
	form = CriteriaForm()
	implementasi = Implementasi.query.filter_by(sumberdaya=form.sumberdaya.data, investasi=form.investasi.data).first()
	keuntungan = Keuntungan.query.filter_by(pengetahuan=form.pengetahuan.data, keuangan=form.keuangan.data).first()
	rancangan = Rancangan.query.filter_by(pengetahuan=keuntungan.keuntungan, keuangan=form.keuangan.keuangan).first()
	return render_template('rancangan.html', imp=implementasi, ktg=keuntungan, rcg=rancangan, title=rancangan)