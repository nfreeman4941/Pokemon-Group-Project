#Nina Freeman, Lydia McPhee, Rebeca Mousser, Mason Stewart
#Pokemon Battle

class Pokemon:
    def __init__(self,name,elemental_type,hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    def get_info(self):
        return f'{self.name.title()} - Type: {self.elemental_type} - Hit Points: {self.hit_points}'
    
    def heal(self):
        self.hit_points += 15

        return f'{self.name.title()} has been healed to {self.hit_points}'