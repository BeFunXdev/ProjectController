class Observer:
    subscribes = []

    @classmethod
    def event(cls, data: any):
        for action in cls.subscribes:
            action(data)

    @classmethod
    def subscribe(cls, function: any):
        cls.subscribes.append(function)


class Consumer:

    def __init__(self, observer: Observer):
        observer.subscribe(self.action)

    def action(self, data: any):
        pass
