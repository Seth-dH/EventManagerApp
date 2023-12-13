
class Event:
    def __init__(self, eventID, eventLocation, eventType):
        self._eventID = eventID
        self.setEventLocation(eventLocation)
        self._eventType = eventType
        
    def getEventID(self):
        return self.__eventID
    
    def setEventLocation(self, newLocation):
        if(newLocation != None):
            for char in newLocation:
                if(char.isnumeric()):
                    raise NameError("No number permitted in newLocation variable")
            self._evelntLocation = newLocation
        
    def calcEventFee(self):
        eventFee = 12000000
        return eventFee + eventFee * 0.135