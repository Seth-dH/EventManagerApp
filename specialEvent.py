import event

class specialEvent(event.Event):
    def __init__(self, eventID, eventLocation, eventType, specialEventType):
        super().__init__(eventID, eventLocation, eventType)
        self.__specialEventType = specialEventType
        
    def calcEventFee(self):
        vipEventFee = 15000000
        return vipEventFee + vipEventFee * 0.135