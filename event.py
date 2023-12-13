
class Event:
    def __init__(self, eventID, eventLocation, eventType):
        self.__eventID = eventID
        self.setEventLocation(eventLocation)
        self.__eventType = eventType
        
    def getEventID(self):
        return self.__eventID
    
    def setEventLocation(self, newLocation):
        if(newLocation != None):
            for char in newLocation:
                if(char.isnumeric()):
                    raise NameError("No number permitted in newLocation variable")
            self.__evelntLocation = newLocation
        else:
            raise NameError("No Value passed in the newLocation method variable")
        
    def calcEventFee(self):
        eventFee = 12000
        return eventFee + eventFee * 0.135