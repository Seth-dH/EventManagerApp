import event
import specialEvent
import json

class ProductManagerApp:
    def __init__(self):
        self._events = []
        self.loadData()
        
        self.run()
        
    def run(self):
        print("Event Manager - [Seth deHaan]")
        
        while True:
            print('What woud you like to do:')
            print('1.\tcreate new event')
            print('2.\tcreate new special event')
            print('3.\tcalculate fees for all events')
            print('4.\tsave and exit')
            print()
            userCh = 0
            while(True):
                print('Enter the number of the option you would like to choose')
                try:
                    userCh = int(input())
                    if(userCh > 0 and userCh < 5):
                        break
                    else:
                        raise ValueError
                except:
                    print("Invalid answer, Please try again")    
                    print()
            
            if(userCh == 1):
                self.createNewEvent()
            if(userCh == 2):
                self.createNewSpecialEvent()
            if(userCh == 3):
                self.calculateFeesForAllEvents()
            if(userCh == 4):
                self.saveData()
                break
    
    def createNewEvent(self):
        print('What is the event ID')
        eventId = input()
                        
        print('What is the event type')
        eventType = input()
        
        while True:
            try:
                print("What is the event location")
                location = input()
                newEvent = event.Event(eventId, location, eventType)
                break
            except:
                print("Invalid entry, please try again")
                print("Make sure the location is not empty, and there are no numbers in the location")
                
        self._events.append(newEvent)
        print('event created!')
        
    def createNewSpecialEvent(self):
        print('What is the event ID')
        eventId = input()
                        
        print('What is the event type')
        eventType = input()
        
        print("What is the special event type")
        specEventType = input()
        
        while True:
            try:
                print("What is the event location")
                location = input()
                self._events.append(specialEvent.SpecialEvent(eventId, location, eventType, specEventType))
                break
            except:
                print("Invalid entry, please try again")
                print("Make sure the location is not empty, and there are no numbers in the location")
                
        print('event created!')
    
    def calculateFeesForAllEvents(self):
        totalFees = 0
        for event in self._events:
            totalFees += event.calcEventFee()
            
        print(f"The Total fees of all events is: ${totalFees}")
        
    def saveData(self):
        readableEvents = []
        for _event in self._events:
            if(type(_event) == event.Event):
                readableEvents.append([_event.getEventID(), _event.getEventLocation(), _event.getEventType()])
            elif(type(_event) == specialEvent.SpecialEvent):
                readableEvents.append([_event.getEventID(), _event.getEventLocation(), _event.getEventType(), _event.getSpecialEventType()])
        with open ('events.json', 'w') as eventFile:
            json.dump(readableEvents, eventFile, indent=2)
    
    def loadData(self):
        with open('events.json', 'r') as eventFile:
            eventValues = json.load(eventFile)
            
        for _event in eventValues:
            if(len(_event) == 3):
                self._events.append(event.Event(_event[0], _event[1], _event[2]))
            elif(len(_event) == 4):
                self._events.append(specialEvent.SpecialEvent(_event[0], _event[1], _event[2], _event[3]))
                
    
projectManagerApp = ProductManagerApp()