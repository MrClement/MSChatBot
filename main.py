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
		if x.lower.find(kuntz) >=0:
			x=raw_input("Brags about how smart Kent students are")
		if x.lower.find(Harrington) >=0:
			x=raw_input("headmaster")
		if x.lower.find(football) >=0:
			x=raw_input("go Broncos")
		if x.lower.find(soccer) >=0:
			x=raw_input("You are not American enough")
		if x.lower.find(jackson) >=0:
			x=raw_input("Knows French")
		if x.lower.find(newman) >=:0
			x=raw_input("Stares at walls")
		if x.lower.find(baseball) >=0:
			x=raw_input("Hood baseball is where you get mugged by a man with a bat")
		if x.lower.find(wrestling) >=0:
			x=raw_input("John Cena did 911")
		if x.lower.find(hockey) >=0:
			x=raw_input("Sam Choi")
		if x.lower.find(addison) >=0:
			x=raw_input("Is a llama")
		if x.lower.find(hat) >=0:
			x=raw_input("ripped a hole in space time to get baby hands")
		if x.lower.find(goat) >=0:
			x=raw_input("will be converted to llama")
		if x.lower.find(meme) >=0:
			x=raw_input("llamas with hats rule the universe")
		if x.lower.find(Peru) >=0:
			x=raw_input("land of the llamas")
		if x.lower.find(mexico) >=0:
			x=raw_input("those people are llamas")



if __name__ == "__main__":
	main()
