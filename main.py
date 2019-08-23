import webapp2
import jinja2
import os
from model import *
#from handler import *

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

room11 = "You feel a sense of dread when you first enter. {{ Name of User }}, you must kill all the enemies inside. If not the village will not survive the next attack. You also noticed the smell of feces around this room and the amount of skeletons there are in this room is a great amount. Good lord there is a bunch of skeletons here! This is not the first time someone has tried to clean out this infestation."
room12 = "It's a kitchen, but not a very clean one. Dirty dishes and pans everywhere, rats roaming around like it's nobody's business, and worst of all, cooked chicken right next to raw chicken in the fridge. Whoever runs this kitchen must've dropped out of culinary school. And soon you find out unsurprisingly it's run by a goblin. {{Name of User}} please get rid of this abomination of a chef!"
room13 = "You go through a giant wooden door. The room you have entered is big, can't even see the ceiling. Everywhere you turn the walls and pillars are covered in dry blood stains. Guess you found out why there are so many skeletons in the first room, huh {{ Name of User}}? But you aren't alone, you start to hear the growling of a goblin. But this one sounds ...angrier? Uh oh! It's a hobgoblin! And it's wearing armor! {{Name of User}} would you kindly eliminate this foe?"
room14 = "You go through a metal door, and find yourself in a library. Rows and rows of books on shelves are in this room. Save for a couple of cobwebs, it's actually pretty clean compared to the rest of this dungeon. How strange, goblins are pretty dumb and can't read. So why would they keep a library? No time to think however, because a goblin has been hiding behind a shelf and ambushes you. It's a shame you can't speak goblinese {{Name of User}}, otherwise you could've asked him. Well {{Name of User}}, you know what to do. Eliminate him."
room15 = "You're almost there to the end of the dungeon. And wouldn't you know it, you come across the treasure room. There are chests filled with gold coins everywhere. Gold everywhere you look, Hooray! You grab a huge handful of gold eagerly, and upon closer inspection you're happiness starts to fade. They're pennies, just covered in gold paint. Well {{Name of user}}, at least you can pay for the bus ride home. It's not all bad though because you come across the legendary Stick of Truth! The most powerful weapon of all time. And yes it's made of gold {{Name of User}}, the legends said it is. With more courage and slightly richer, you press onward. Or you go back for some reason."
room16 = "You entered the final room {{Name of User}}. The throne room. A long regal hallway with a throne made out of stone. And who is smugly sitting there on the throne. None other than the Goblin King himself. This is going to be a tough one {{Name of User}}. Not many have seen or even fought a Goblin King , and for good reason too. Armed with your stick, you face him head on!"

img1=""
img2=""
img3=""
img4=""
img5=""
img6=""

room_dict = {
    "start": Room( room11, ["kitchen" , "HG"], NoMonster(),img1),
    "kitchen": Room(room12, ["start"], Goblin(),img2),
    "HG": Room(room13, ["start" , "Lib","Treasure"], Hobgoblin(),img3),
    "Lib": Room(room14, ["HG"], Goblin(),img4),
    "Treasure": Room(room15, ["HG","FB"], NoMonster(),img5),
    "FB": Room(room16, ["Treasure"], GoblinKing(),img6),
}

#current_room_key = "start"


class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/pass.html')
        self.response.write(result_template.render())

class PlayPageHandler(webapp2.RequestHandler):
    def post(self):
        current_room_key = self.request.get("roomchoice")
        if current_room_key == "":
            current_room_key = "start"

        var_dict = {
            "Cur_for_dict": room_dict[current_room_key]
        }

        result_template = the_jinja_env.get_template('templates/main.html')
        self.response.write(result_template.render(var_dict))


app = webapp2.WSGIApplication([
    ('/', LoginPageHandler),
    ('/game', PlayPageHandler)
], debug = True)
