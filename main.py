import object
import subject
import verb
def main():
	inputs = []
	initial = raw_input("Hi I am ACRONYM")
	while(True):
		subject = subject.getRandomWord()
		verb = verb.getRandomWord()
		object = object.getRandomWord
		x = raw_input(subject, verb, object)
		inputs.append(x)
		if(x=="nobody loves you"):
			return('nobody loves you either')
