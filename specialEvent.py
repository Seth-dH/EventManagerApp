import event

class SpecialEvent(event.Event):
    def __init__(self, eventID, eventLocation, eventType, specialEventType):
        super().__init__(eventID, eventLocation, eventType)
        self._specialEventType = specialEventType
        
    def getSpecialEventType(self):
        return self._specialEventType
        
    def calcEventFee(self):
        vipEventFee = 15000000
        return vipEventFee + vipEventFee * 0.135