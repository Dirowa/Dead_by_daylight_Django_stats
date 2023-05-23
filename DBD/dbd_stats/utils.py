import matplotlib.pyplot as plt
import base64
from io import  BytesIO
from datetime import datetime


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf8')
    buffer.close()
    return graph
class CreateData():
    def __init__(self, query):
        self.data = query
        self.data = self.correct_data()
        self.how_many_games = self.get_games_per_time()

    def correct_data(self):
        new_data = {}
        for i in (self.data):
            i =  (dict(i))
            new_data[i["pub_date"]] = i
        return new_data

    def get_games_per_time(self):
        dates = []
        for i in self.data.keys():
            i = (i.split("T"))[0]
            dates.append(i)
        return dates
    def get_plot_histogram(self):
        plt.switch_backend("AGG")

        days = list((self.how_many_games).keys())


        plt.figure(figsize=(10,5))
        plt.title("games a day")
        plt.hist(self.how_many_games)
        graph = get_graph()
        return graph