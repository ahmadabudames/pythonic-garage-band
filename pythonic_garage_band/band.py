
class Band:
    def __init__(self,name,members=[]):
        self.name = name
        self.members = members
   
    def __str__(self):
        str = f"Band Name : {self.name}\nMembers names : "
        for player in self.members :
            str = str + '\n' + player.name
        return str

    def __repr__(self):
        return f"Name : {self.name}"

    def to_list(self):
        return self.members





