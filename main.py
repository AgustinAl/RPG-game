import webapp2
import jinja2
import os
from model import *
#from handler import *

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

room_dict = {
    "start": Room("#write des", ["kitchen" , "HG"], NoMonster()),
    "kitchen": Room("#write des", ["start"], Goblin()),
    "HG": Room("#write des", ["start" , "Lib","Treasure"], Hobgoblin()),
    "Lib": Room("#write des", ["HG"], NoMonster()),
    "Treasure": Room("#write des", ["HG","FB"], NoMonster()),
    "FB": Room("#write des", ["Treasure"], GoblinKing()),
}

current_room_key = "start"

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/pass.html')
        self.response.write(result_template.render())

class PlayPageHandler(webapp2.RequestHandler):
    def get(self):

        var_dict = {
            "Des_for_template": room_dict[current_room_key].description
        }
        result_template = the_jinja_env.get_template('templates/main.html')
        self.response.write(result_template.render(var_dict))


app = webapp2.WSGIApplication([
    ('/', LoginPageHandler),
    ('/game', PlayPageHandler)
], debug = True)
