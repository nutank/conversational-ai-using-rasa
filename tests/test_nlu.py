from rasa_nlu.model import Metadata, Interpreter
import json

def pprint(o):
 # small helper to make dict dumps a bit prettier
	print(json.dumps(o, indent=2))

interpreter = Interpreter.load('./models/current/nlu')
pprint(interpreter.parse(u"My day is HORRIBLE"))


# from rasa_nlu.evaluate import run_evaluation
# run_evaluation("data/nlu.md", "./models/current/nlu")