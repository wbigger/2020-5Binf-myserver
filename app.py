# La seguente istruzione importa la classe "Flask" dalla libreria "flask"
# Notare che possiamo usare la libreria flask perché l'abbiamo già installata con pip3
from flask import Flask

from amorosi import pagina as paginaAmorosi
from gismondi import pagina as paginaGismondi
from ciocci import pagina as paginaCiocci
from moracchioli import pagina as paginaMoracchioli
from stella import pagina as paginaStella
from soriani import pagina as paginaSoriani

# Istanzio l'oggetto della classe Flask
# L'argomento è una qualsiasi stringa identificativa, nel nostro caso "marconi"
# Notare che non dobbiamo dichiarare il tipo, perché viene "inferito" dal compilatore
app = Flask("marconi")

# Le istruzioni che cominciano con @ si chiamano "annotazioni"
# Ci dicono qualcosa su quello che segue
# In particolare l'annotazione @app.route ci dice che la funzione che segue
# deve rispondere ad una particolare rotta, in questo caso "/" che è la rotta di default
@app.route('/')
# Definiamo una funzione con la parola chiave "def"
# Anche in questo caso il tipo di ritorno della funzione viene inferito
def hello():
	return '<h1>ciao sono il prof. Claudio Capobianco</h1>'

@app.route('/amorosi')
def amorosi():
    return paginaAmorosi

@app.route('/ciocci')
def ciocci():
    return paginaCiocci

@app.route('/gismondi')
def gismondi():
    return paginaGismondi

@app.route('/stella')
def stella():
    return paginaStella

@app.route('/moracchioli')
def moracchioli():
    return paginaMoracchioli

@app.route('/soriani')
def soriani():
    return paginaSoriani
# Notare che le righe in python non richiedono il ; alla fine
# Il contenuto delle funzioni deve essere indentato, perché non si usano le parentesi graffe
