class Musician:
    def __init__(self,name):
        self.name=name
        


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self) -> str:
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"
    

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self) -> str:
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"
    

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
    
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"
    

class Band:
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)

    def __str__(self):
        return f"Hey we are {self.name} band"
    
    def __repr__(self):
        return f"Hey we are {self.name} band"

    def play_solos(self):
        arr=[]
        for i in self.members:
            arr.append(i.play_solo())
            
        return arr

    def get_members(self):
        return self.members
    
    @classmethod
    def to_list (cls):
        return cls.instances

arr_musician=[Guitarist("yazeed"),Bassist("mohammed"),Drummer("abood"),Guitarist("zaid")]
print(arr_musician)