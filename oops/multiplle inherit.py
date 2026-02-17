#multiple inheritance is 2 parents and one chile class

class parent1:
    pass
class parent2:
    pass
class child(parent1,parent2):
    pass

class father:
    def driving(self):
        print("father has the skills to drive")

class mother:
    def cooking(self):
        print("mother has the skills of cooking")

class child(father,mother):
    def bothskills(self):
        print("child has the skills of both driving and cooking")
        print("child has the skills of gamming")

obj = child()
obj.driving()
obj.cooking()
obj.bothskills()