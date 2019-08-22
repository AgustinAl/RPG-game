import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/pass.html')
        self.response.write(result_template.render())

class PlayPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = the_jinja_env.get_template('templates/main.html')
        self.response.write(result_template.render())


app = webapp2.WSGIApplication([
    ('/', LoginPageHandler),
    ('/play', PlayPageHandler)
], debug = True)
