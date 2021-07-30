from abc import  abstractmethod, abstractstaticmethod, abstractclassmethod


    

class Musician:
    members = []
    def __init__(self, name):
        self.name=name
        Musician.members.append(self.name)
    @abstractmethod # Abstraction
    def __str__(self):
        pass
    @abstractmethod # Abstraction
    def __repr__(self):
        pass
    @abstractstaticmethod # Abstraction
    def get_instrument(self):
        pass
    @abstractclassmethod # Abstraction
    def play_solo(self):
        pass

class Band(Musician):
    instances=[]
    def __init__(self, name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
             
    def play_solos(self):
        each_member=[]
        for x in self.members:
            each_member.append(x.play_solo())
        return each_member
    def __str__(self):
        
        return f" i am {self.name} and welcome to you "

    def __repr__(self):

        return f"Name = {self.name}"
    @classmethod
    def to_list(class_method):
        
        return class_method.instances

        


    
    
    
class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return "bom bom buh bom"
    
    

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return "rattle boom crash"




