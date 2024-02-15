
class Animal:

    def __init__(self, s, n):
        self.state = s
        self.size = n
        self.__happiness = 1.0
        self.__hunger = 1.0
        self.__tiredness = 1.0
    
    def SetHappiness(self, NewHappiness):
        self.__happiness = NewHappiness
        
    
    def GetHappiness(self):
        return self.__happiness
    
    def SetHunger(self, NewHunger):
        self.__hunger = NewHunger
        
    
    def GetHunger(self):
        return self.__hunger
    
    def SetTiredness(self, NewTiredness):
        self.__tiredness = NewTiredness
        
    
    def GetTiredness(self):
        return self.__tiredness
    
    def feed(self):
        """Feed the animal"""
        self.size += 1
        print(self.state, "fed")
      
    def getState(self):
        """Get the state of the animal"""
        return self.state
    
    def getSize(self):
        """Get the size of the animal"""
        return self.size
    
    
class Fish(Animal):
    
    def __init__(self, s, n):
        Animal.__init__(self, s, n)
        self.maxSize = 0
        self.__happiness = 5.0
        self.__hunger = 1.0
        self.__tiredness = 1.0
    
    def setMaxSize(self, m):
        """Set maximum size of fish"""
        self.maxSize = m
        
    def feed(self): #overriding the Animal.feed()
        """Feed the fish"""
        self.size += 2
        print(self.state, "fed")
        if self.size >= self.maxSize:
            self.state = "BIG FISH"
        
class Duck(Animal):
    
    def __init__(self, s, n):
        Animal.__init__(self, s, n)
        
    def feed(self): #overriding the Animal.feed()
        """Feed the duck"""
        Animal.feed(self)
        if self.size == 3:
            self.state = "BIG DUCK"



    
thisFish = Fish("little fish", 0)
thisFish.setMaxSize(3)
thisDuck = Duck("little duck", 0)
for count in range(3):
    thisDuck.feed()
    print(thisDuck.getState())
    thisFish.feed()
    print(thisFish.getState())


