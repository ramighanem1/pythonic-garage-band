from abc import ABC, abstractmethod

class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f'Musician instance. Name = {self.name}'
    
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self ,name) :
        super().__init__(name)

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'guitar'
    
    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    def __init__(self ,name) :
        super().__init__(name)

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    def __init__(self ,name) :
        super().__init__(name)

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'drums'
    
    def play_solo(self):
        return 'rattle boom crash'
    
class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f'Name = {self.name}'

    def __repr__(self):
        return f'Band instance. Name = {self.name}'

    def play_solos(self):
        result = []
        for member in self.members:
            result.append(member.play_solo())
        return result

    @classmethod
    def to_list(cls):
        return cls.instances

