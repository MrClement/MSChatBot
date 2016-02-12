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
			x=raw_input("Mr. Clement plays Dota")
		if x.lower.find("llama") >=0:
			x=raw_input("Did you know that Addison is a llama?")
		if x.lower.find(kuntz) >=:
			x=raw_input)("Brags about how smart Kent students are")
		if x.lower.find(Harrington) >=:
			x=raw_input("headmaster")
		if x.lower.find(football) >=:
			x=raw_input("go Broncos")
		if x.lower.find(soccer) >=:
			x=raw_input)("You are not American enough")



if __name__ == "__main__":
	main()
