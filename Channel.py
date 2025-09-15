class Channel:
    def __init__(self):self.subscribers = []
    def subscribe(self, user):self.subscribers.append(user)
    def upload(self, video):
        for subscriber in self.subscribers:
            subscriber.notify(video)
class User:
    def notify(self, video):
        print("New video",video)

yt = Channel()
u1,u2 = User(), User()
yt.subscribe(u1);yt.subscribe(u2)
yt.upload("Python Basics")