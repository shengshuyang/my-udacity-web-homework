import webapp2
import handler as hd


class ToDoHandler(hd.Handler):

    def get(self):
        nav = self.render_str("nav_off.html")
        self.render("todo_list.html",
                    items=self.request.get_all("food"),
                    navigation=nav)

app = webapp2.WSGIApplication([
    ('/todo_list', ToDoHandler)
], debug=True)
