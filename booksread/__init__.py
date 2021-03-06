"""
	Some description
"""
from bottle import route, run, debug
from booksword import models
from .booksword import predict

def run_server(port_num=8080):
	models.load_models()
	debug(True)

	@route('/<first_word>/<second_word>')
	def index(first_word, second_word):
		return dict(predict(first_word, second_word))
	
	run(host='localhost', port=port_num)

def load():
	print("Hold on Training on Way")
	models.load_models()
	print("training done!!")
	return True