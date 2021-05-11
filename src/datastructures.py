from random import randint

class FamilyStructure:
    def __init__(self, name_last):
        self.name_last = name_last

        self._members = [
            {
                "0_id" : 0,
                "1_name_first" : "Joe",
                "2_name_last" : name_last,
                "3_age" : 60,
                "4_children" : [] 
            }
        ]

    # def random_integer(self):
    #     return randint(0, 99999999)

    def getAllMembers(self):
        return self._members

    def getSingleMember(self, id):
        for member in enumerate(self._members):
            single_member = member[id]
            if single_member == int(id):
                return member
        return None

    def createFamilyMember(self, id, name_first, age, parent_id, parent):
        family_member = {
            "0_id" : id,
            "1_name_first" : name_first,
            "2_name_last" : self.name_last,
            "3_age" : age,
            "4_children" : [],
            "5_parent" : parent
        }

        for index, member in enumerate(self._members):
            if member['0_id'] == int(parent_id):
                self._members[index]['4_children'].append(family_member['1_name_first'])

        self._members.append(family_member)
        return family_member