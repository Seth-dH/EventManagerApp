import event

class specialEvent(event.Event):
    def __init__(self, eventID, eventLocation, eventType, specialEventType):
        super().__init__(eventID, eventLocation, eventType)
        self.__specialEventType = specialEventType
        
    def calcEventFee(self, eventBaseCost, specialEventFee):
        eventFee = eventBaseCost + specialEventFee
        return eventFee + eventFee * 0.135