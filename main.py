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
		favorites = x.lower().find("favorite")
		if favorite > -1:
			ice_cream = x.lower().find("ice cream")
			if ice_cream > -1:
				print ("my favorite ice cream is chocolate")
			animal = x.lower().find("animal")
			if animal > -1:
				print ("my favorite animal is a black Jaguar")
			food = x.lower().find("food")
			if food > -1:
				print ("my favorite food is pizza")
			dinosaur = x.lower().find("dinosaur")
			if dinosaur > -1:
				print ("my favorite dinosaur is the T-rex")
			country = x.lower().find("country")
			if countr > -1:
				print ("my favorite country is the USA")
			footballteam = x.lower().find("football team")
			if footballteam > -1:
				print ("my favorite football team is the Denver Broncos")
			color = x.lower().find("color")
			if color > -1:
				print ("my favorite color is green")
			state = x.lower().find("state")
			if state > -1:
				print ("my favorite state is colorado")
			subject = x.lower().find("subject)
			if subject > -1:
				print ("my favorite subject is computer programing")
			actor = x.lower().find("actor")
			if actor > -1:
				print ("my favorite actor is Benedict Cumberbatch")
			movie = x.lower().find("movie")
			if movir > -1:
				print ("my favorite movie is the Avengers")
			band = x.lower().find("band")
			if band > -1:
				print ("my favorite band are the beatles")
			tv = x.lower().find("tv")
			if tv > -1:
				print ("my favorite tv show is Pretty Little Liers")
			zoo = x.lower().find("zoo")
			if zoo > -1:
				print ("my favorite zoo is the San Deigo Zoo")
		inputs.append(x)
		if(x=="nobody loves you"):
			return('nobody loves you either')

if __name__ == "__main__":
	main()
