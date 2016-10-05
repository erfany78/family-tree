"""
Name the project FamilyTree_Kim.py
"""

person_list = []
class Family_tree():

    def __init__(self):
        self.family_tree = {"sibling": [], "parent": [], "half-sibling": [], "cousin": [], "children": [], 'spouse': [], "ancestor": []}

class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree().family_tree
        person_list.append(self)

    def add_parents(self, parent_one, parent_two):
        self.family_tree['parent'].append(parent_one)
        if parent_one not in parent_two.family_tree['spouse']:
            parent_two.family_tree['spouse'].append(parent_one)
        self.family_tree['parent'].append(parent_two)
        if parent_two not in parent_one.family_tree['spouse']:
            parent_one.family_tree['spouse'].append(parent_two)

        parent_one.add_children(self)
        parent_two.add_children(self)

        self.add_siblings(parent_one, parent_two)
        self.add_cousins(parent_one, parent_two)

        # Adds the parents as ancestors of the Person as defined in specs
        self.family_tree['ancestor'].append(parent_one)
        self.family_tree['ancestor'].extend(parent_one.family_tree['ancestor'])
        self.family_tree['ancestor'].append(parent_two)
        self.family_tree['ancestor'].extend(parent_two.family_tree['ancestor'])

    def add_children(self, child):
        self.family_tree['children'].append(child)

    def add_spouse(self, spouse):
        if spouse not in self.family_tree['spouse']:
            self.family_tree['spouse'].append(spouse)
        if self not in spouse.family_tree['spouse']:
            spouse.family_tree['spouse'].append(self)

    def add_siblings(self, parent_one, parent_two):
        for child in parent_one.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_two.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-sibling'].append(child)
                    if self not in child.family_tree['half-sibling']:
                        child.family_tree['half-sibling'].append(self)

                # Adds the siblings to the cousin list as 0th cousins as defined in specs
                if self not in child.family_tree['cousin']:
                    child.family_tree['cousin'].append(self)
                if child not in self.family_tree['cousin']:
                    self.family_tree['cousin'].append(child)

        for child in parent_two.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_one.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-sibling'].append(child)
                    if self not in child.family_tree['half-sibling']:
                        child.family_tree['half-sibling'].append(self)

                # Adds the siblings to the cousin list as 0th cousins as defined in specs
                if self not in child.family_tree['cousin']:
                    child.family_tree['cousin'].append(self)
                if child not in self.family_tree['cousin']:
                    self.family_tree['cousin'].append(child)

    def add_cousins(self, parent_one, parent_two):
        for cousin in parent_one.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
                if self not in cousin.family_tree['cousin']:
                    cousin.family_tree['cousin'].append(self)

        for cousin in parent_two.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
                if self not in cousin.family_tree['cousin']:
                    cousin.family_tree['cousin'].append(self)

        for sibling in parent_one.family_tree['sibling']:
            if sibling not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(sibling)
                if self not in sibling.family_tree['cousin']:
                    sibling.family_tree['cousin'].append(self)

        for halfsib in parent_one.family_tree['half-sibling']:
            if halfsib not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(halfsib)
                if self not in halfsib.family_tree['cousin']:
                    halfsib.family_tree['cousin'].append(self)

        for sibling in parent_two.family_tree['sibling']:
            if sibling not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(sibling)
                if self not in sibling.family_tree['cousin']:
                    sibling.family_tree['cousin'].append(self)

        for halfsib in parent_two.family_tree['half-sibling']:
            if halfsib not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(halfsib)
                if self not in halfsib.family_tree['cousin']:
                    halfsib.family_tree['cousin'].append(self)

    # Deprecated. Use the Operations class function list_relation(person_name, relation)
    def list_relation(self, relation):
        for family_member in self.family_tree[relation]:
            print(family_member.name)

class Operations():

    def list_relation(self, person_name, relation):
        for person in person_list:
            if person_name == person.name:
                for family_member in person.family_tree[relation]:
                    print(family_member.name)

    def is_relation(self, person_name_one, person_name_two, relation):
        #  Checks to see if person_one has RELATION with person_two
        #  All the above attributes are strings
        #  Returns true or false
        for person in person_list:
            if person_name_one == person.name:
                for person_2 in person_list:
                    if person_name_two == person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("true")
                            return
                        else:
                            print("false")
                            return
        print("false")

    def closest_relation(self, person_one, person_two):
        if person_two in person_one.family_tree["spouse"]:
            print("spouse")
            return
        if person_two in person_one.family_tree["sibling"]:
            print("sibling")
            return
        if person_two in person_one.family_tree["half-sibling"]:
            print("half-sibling")
            return
        if person_two in person_one.family_tree["parent"]:
            print("parent")
            return
        if person_two in person_one.family_tree["ancestor"]:
            print("ancestor")
            return
        if person_two in person_one.family_tree["cousin"]:
            print("cousin")
            return
        else:
            print("Unrelated")


def check_exists(person_name):
    if person_name in person_list:
        pass
    else:
        return Person(person_name)

def retrieve_person(person_name):
    for person in person_list:
        if person.name == person_name:
            return person
    return Person(person_name)

def fileRead():
    op = Operations()
    #filename = input()
    # open file and read all text
    f = open("family.txt", mode='r')
    text = f.read()
    # tokenize words with " " delimiter
    text = text.split("\n")

    for line in text:
        commands = line.split(" ")
        if commands[0] is "E":
            if len(commands) is 4:
                #print(commands)
                person_one = retrieve_person(commands[1])
                person_two = retrieve_person(commands[2])
                person_three = retrieve_person(commands[3])
                person_three.add_parents(person_one, person_two)

            if len(commands) is 3:
                person_one = retrieve_person(commands[1])
                person_two = retrieve_person(commands[2])
                person_one.add_spouse(person_two)

        if commands[0] is "W":
            person_one = retrieve_person(commands[2])
            relation = commands[1]
            op.list_relation(person_one.name, relation)

        if commands[0] is "R":
            person_one = retrieve_person(commands[1])
            person_two = retrieve_person(commands[2])
            op.closest_relation(person_one, person_two)

        if commands[0] is "X":
            person_one = retrieve_person(commands[1])
            relation = commands[2]
            person_two = retrieve_person(commands[3])
            op.is_relation(person_one.name, person_two.name, relation)


def main():
    fileRead()
    


main()
#if __name__ == '__main__':
#    main()
