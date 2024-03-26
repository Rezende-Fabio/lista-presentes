from app.httpResponse.HttpResponse import HttpResonse


class IndexController(HttpResonse):

    def renderIndex(self):
        return self.responseRender("index.html")