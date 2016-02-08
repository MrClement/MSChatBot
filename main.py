import object
import subject
import verb
def main():
	inputs = []
	initial = raw_input("Hi I am ACRONYM \n")
	while(True):
		s = subject.getRandomWord()
		v = verb.getRandomWord()
		o = object.getRandomWord()
		x = raw_input("ACRONYM: " + s + " " + v + " " +o + "\nResponse> ")
		inputs.append(x)
		if(x=="nobody loves you"):
			return('nobody loves you either')

if __name__ == "__main__":
	main()
