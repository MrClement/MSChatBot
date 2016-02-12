import object
import subject
import verb
def main():
	inputs = []
	print "Hi I am ACRONYM"
	name = raw_input("ACRONYM: What is your name? \n")
	while(True):
		s = subject.getRandomWord()
		v = verb.getRandomWord()
		o = object.getRandomWord()
		x = raw_input("ACRONYM: Hey, "+ name + ", I heard that " + s + " " + v + " " +o + "\nResponse> ")
		inputs.append(x)
		if(x=="nobody loves you"):
			return('nobody loves you either')
		if x.lower.find("clement") >=0 :
			print "Mr. Clement plays Dota"
		if x.lower.find("llama") >=0:
			print "Did you know that Addison is a llama?"
		if x.lower.find(kuntz) >=:
			print "Brags about how smart Kent students are"
		if x.lower.find(Harrington) >=:
			print "headmaster"
		if x.lower.find(football) >=:
			print "go Broncos"
		if x.lower.find(soccer) >=:
			"You are not American enough"



if __name__ == "__main__":
	main()
