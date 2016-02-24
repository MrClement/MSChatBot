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
		if x.lower().find("clement") >=0:
			x=raw_input("Mr. Clement plays Dota" + "\nResponse>")
		if x.lower().find("llama") >=0:
			x=raw_input("Did you know that Addison is a llama?" + "\nResponse>")
		if x.lower().find("kuntz") >=0:
			x=raw_input("Brags about how smart Kent students are" + "\nResponse>")
		if x.lower().find("Harrington") >=0:
			x=raw_input("headmaster" + "\nResponse>")
		if x.lower().find("football") >=0:
			x=raw_input("go Broncos" + "\nResponse")
		if x.lower().find("soccer") >=0:
			x=raw_input("You are not American enough" + "\nResponse>")
		if x.lower().find("jackson") >=0:
			x=raw_input("Knows French" + "\nResponse>")
		if x.lower().find("newman") >=0:
			x=raw_input("Stares at walls" + "\nResponse>")
		if x.lower().find("baseball") >=0:
			x=raw_input("Hood baseball is where you get mugged by a man with a bat" + "\nResponse>")
		if x.lower().find("wrestling") >=0:
			x=raw_input("John Cena did 911" + "\nResponse>")
		if x.lower().find("hockey") >=0:
			x=raw_input("Sam Choi" + "\nResponse>")
		if x.lower().find("addison") >=0:
			x=raw_input("Is a llama" + "\nResponse>")
		if x.lower().find("hat") >=0:
			x=raw_input("ripped a hole in space time to get baby hands" + "\nResponse>")
		if x.lower().find("goat") >=0:
			x=raw_input("will be converted to llama" + "\nResponse>")
		if x.lower().find("meme") >=0:
			x=raw_input("llamas with hats rule the universe" + "\nResponse>")
		if x.lower().find("peru") >=0:
			x=raw_input("land of the llamas" + "\nResponse>")
		if x.lower().find("mexico") >=0:
			x=raw_input("those people are llamas" + "\nResponse>")



if __name__ == "__main__":
	main()
