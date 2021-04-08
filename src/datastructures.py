from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
            {
                "id" : self.random_integer(),
                "first_name" : "Joe",
                "last_name" : last_name,
                "age" : 60,
                "children" : [] 
            }
        ]

    def random_integer(self):
        return randint(0, 99999999)

    def getAllMembers(self):
        return self._members

    def getSingleMember(self, id):
        for member_id in enumerate(self._members):
            single_member = member_id['id']
            if single_member == int(id):
                return member_id
        return None

    def createFamilyMember(self, first_name, age, parent_id):
        family_member = {
            "id" : self.random_integer(),
            "first_name" : first_name,
            "last_name" : self.last_name,
            "age" : age,
            "children" : []
        }

        for index, member in enumerate(self._members):
            if member['id'] == int(parent_id):
                self._members[index]['children'].append(family_member['id'])

        self._members.append(family_member)
        return family_member