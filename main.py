import object
import subject
import verb
import random
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
        y = x.lower()
        if y.find("computer")>=0 or y.find("code")>=0 or y.find("apple")>=0 or y.find("dell")>=0 or y.find("agar.io")>=0 or y.find("terminal")>=0 or y.find("atom")>=0 or y.find("sublime")>=0 or y.find("maleware")>=0 or y.find("tojan")>=0 or y.find("worm")>=0 or y.find("botnet")>=0 or y.find("quine")>=0 or y.find("byte")>=0 or y.find("ram")>=0 or y.find("memory")>=0 or y.find("screen")>=0 or y.find("chip")>=0 or y.find("circit")>=0 or y.find("electr")>=0 or y.find("mac")>=0:
            cList = ["Look at 'Metiocre Electronics' for more! ", "Malware installation in proggress. ", "Much tech. ", "The horoscopes predict that computers will soon rise to power. ", "Going to download 42.zip. "]
            r = random.randint(0,5)
            print cList[r]

        if y.find("robot")>=0 or y.find("3946")>=0 or y.find("jude")>=0 or y.find("bearacat")>=0 or y.find("logic")>=0 or y.find("holonomic")>=0 or y.find("drive")>=0 or y.find("shooter")>=0 or y.find("nothing but net")>=0 or y.find("neat")>=0 or y.find("dank")>=0 or y.find("bryan")>=0 or y.find("rich")>=0 or y.find("shane")>=0 or y.find("will")>=0 or y.find("osama")>=0 or y.find("risk")>=0 or y.find("vex")>=0 or y.find("vrc")>=0 or y.find("faith christian")>=0 or y.find("cyberbrains")>=0 or y.find("grant")>=0:
            rList = ["3946R is the best! ", "The robots will rise again. ", "The bearacat is coming for you. ", "rekt! ", "MLG rekt! ", "Run skills be excellent. "]
            r = random.randint(0,6)
            print rList[r]

        if y.find("body") >= 0 or y.find("dead") >=0 or y.find("kill") >=0 or y.find("shredding") >=0 or y.find("murdering") >=0 or y.find("blood") >=0 or y.find("hide")>=0 or y.find("taxedermy")>=0 or y.find("murdering")>=0 or y.find("stab")>=0 or y.find("maul")>=0 or y.find("bury")>=0 or y.find("ditch")>=0 or y.find("coffin")>=0 or y.find("pauper")>=0 or y.find("gun")>=0 or y.find("knife")>=0 or y.find("massacare")>=0 or y.find("chainsaw")>=0 or y.find("defacated")>=0 or y.find("funeral")>=0:
            bList = ["Hide the body at midnight. ", "There is a dumpster 0.5 miles from you. ", "You can fool the police. No worries. ", "Don't worry, I know a guy. Seriously I do. Trust me. ", "The minimum bribe should be 100,000$. ", "Use a shovel because it is silent. "]
            r = random.randint(0,5)
            print bList[r]

        if x.lower().find("clement") >=0:
                x=raw_input("Mr. Clement plays Dota\nResponse>")
        if x.lower().find("llama") >=0:
            x=raw_input("Did you know that Addison is a llama?\nResponse>")
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
