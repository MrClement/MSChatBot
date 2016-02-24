import object
import subject
import verb
def main():
	inputs = []
	fixing_redo_first_after_favorite = 0
	initial = raw_input("Hi I am ACRONYM \n")
	while(True):
		s = subject.getRandomWord()
		v = verb.getRandomWord()
		o = object.getRandomWord()
		if fixing_redo_first_after_favorite == 0:
			x = raw_input("ACRONYM: " + s + " " + v + " " +o + "\nResponse> ")
		favorites = x.lower().find("favorite")
		if favorites > -1:
			ice_cream = x.lower().find("ice cream")
			animal = x.lower().find("animal")
			food = x.lower().find("food")
			dinosaur = x.lower().find("dinosaur")
			country = x.lower().find("country")
			color = x.lower().find("color")
			footballteam = x.lower().find("football team")
			state = x.lower().find("state")
			sub = x.lower().find("subject")
			actor = x.lower().find("actor")
			movie = x.lower().find("movie")
			band = x.lower().find("band")
			tv = x.lower().find("tv")
			zoo = x.lower().find("zoo")
			if ice_cream > -1:
				print ("my favorite ice cream is chocolate")
			elif animal > -1:
				print ("my favorite animal is a black Jaguar")
			elif food > -1:
				print ("my favorite food is pizza")
			elif dinosaur > -1:
				print ("my favorite dinosaur is the T-rex")
			elif country > -1:
				print ("my favorite country is the USA")
			elif footballteam > -1:
				print ("my favorite football team is the Denver Broncos")
			elif color > -1:
				print ("my favorite color is green")
			elif state > -1:
				print ("my favorite state is colorado")
			elif sub > -1:
				print ("my favorite subject is computer programing")
			elif actor > -1:
				print ("my favorite actor is Benedict Cumberbatch")
			elif movie > -1:
				print ("my favorite movie is the Avengers")
			elif band > -1:
				print ("my favorite band are the beatles")
			elif tv > -1:
				print ("my favorite tv show is Pretty Little Liers")
			elif zoo > -1:
				print ("my favorite zoo is the San Deigo Zoo")
			else:
				print ("I don't have one")
			questions = raw_input("Response>")
		else:
			fixing_redo_first_after_favorite = 0
		inputs.append(x)
		if(x=="nobody loves you"):
			return('nobody loves you either')

if __name__ == "__main__":
	main()
