"""
Name the project FamilyTree_Kim.py
"""

person_list = []
class Family_tree():

    def __init__(self):
        self.family_tree = {"siblings": [], "parents": [], "half-siblings": [], "cousins": [], "children": [], 'spouses': [], "ancestors": []}

class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree().family_tree
        person_list.append(self)

    def add_parents(self, parent_one, parent_two):
        self.family_tree['parents'].append(parent_one)
        if parent_one not in parent_two.family_tree['spouses']:
            parent_two.family_tree['spouses'].append(parent_one)
        self.family_tree['parents'].append(parent_two)
        if parent_two not in parent_one.family_tree['spouses']:
            parent_one.family_tree['spouses'].append(parent_two)

        parent_one.add_children(self)
        parent_two.add_children(self)

        self.add_siblings(parent_one, parent_two)

        # Adds the parents as ancestors of the Person as defined in specs
        self.family_tree['ancestors'].append(parent_one)
        self.family_tree['ancestors'].extend(parent_one.family_tree['ancestors'])
        self.family_tree['ancestors'].append(parent_two)
        self.family_tree['ancestors'].extend(parent_two.family_tree['ancestors'])

    def add_children(self, child):
        self.family_tree['children'].append(child)

    def add_spouse(self, spouse):
        if spouse not in self.family_tree['spouses']:
            self.family_tree['spouses'].append(spouse)
        if self not in spouse.family_tree['spouses']:
            spouse.family_tree['spouses'].append(self)

    def add_siblings(self, parent_one, parent_two):
        for child in parent_one.family_tree['children']:
            if child not in self.family_tree['siblings'] and self.name is not child.name:
                if child in parent_two.family_tree['children']:
                    self.family_tree['siblings'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-siblings'].append(child)
                    if self not in child.family_tree['half-siblings']:
                        child.family_tree['half-siblings'].append(self)

                # Adds the siblings to the cousin list as 0th cousins as defined in specs
                if self not in child.family_tree['cousins']:
                    child.family_tree['cousins'].append(self)
                if child not in self.family_tree['cousins']:
                    self.family_tree['cousins'].append(child)

        for child in parent_two.family_tree['children']:
            if child not in self.family_tree['siblings'] and self.name is not child.name:
                if child in parent_one.family_tree['children']:
                    self.family_tree['siblings'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-siblings'].append(child)
                    if self not in child.family_tree['half-siblings']:
                        child.family_tree['half-siblings'].append(self)

                # Adds the siblings to the cousin list as 0th cousins as defined in specs
                if self not in child.family_tree['cousins']:
                    child.family_tree['cousins'].append(self)
                if child not in self.family_tree['cousins']:
                    self.family_tree['cousins'].append(child)

    def add_cousins(self, parent_one, parent_two):
        for cousin in parent_one.family_tree['cousins']:
            if cousin not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(cousin)
                if self not in cousin.family_tree['cousins']:
                    cousin.family_tree['cousins'].append(self)

        for cousin in parent_two.family_tree['cousins']:
            if cousin not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(cousin)
                if self not in cousin.family_tree['cousins']:
                    cousin.family_tree['cousins'].append(self)

        for sibling in parent_one.family_tree['siblings']:
            if sibling not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(sibling)
                if self not in sibling.family_tree['cousins']:
                    sibling.family_tree['cousins'].append(self)

        for halfsib in parent_one.family_tree['half-siblings']:
            if halfsib not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(halfsib)
                if self not in halfsib.family_tree['cousins']:
                    halfsib.family_tree['cousins'].append(self)

        for sibling in parent_two.family_tree['siblings']:
            if sibling not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(sibling)
                if self not in sibling.family_tree['cousins']:
                    sibling.family_tree['cousins'].append(self)

        for halfsib in parent_two.family_tree['half-siblings']:
            if halfsib not in self.family_tree['cousins']:
                self.family_tree['cousins'].append(halfsib)
                if self not in halfsib.family_tree['cousins']:
                    halfsib.family_tree['cousins'].append(self)

    # Deprecated. Use the Operations class function list_relation(person_name, relation)
    def list_relation(self, relation):
        for family_member in self.family_tree[relation]:
            print(family_member.name)

class Operations():

    def list_relation(self, person_name, relation):
        for person in person_list:
            if person_name is person.name:
                for family_member in person.family_tree[relation]:
                    print(family_member.name)

    def is_relation(self, person_name_one, person_name_two, relation):
        #  Checks to see if person_one has RELATION with person_two
        #  All the above attributes are strings
        #  Returns true or false
        for person in person_list:
            if person_name_one is person.name:
                for person_2 in person_list:
                    if person_name_two is person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("true")
                            return
                        else:
                            print("false")
                            return
        print("false")

def check_exists(person_name):
    if person_name in person_list:
        pass
    else:
        return Person(person_name)

def fileRead():
    filename = input()
    # open file and read all text
    f = open(filename, mode='r')
    text = f.read()
    # tokenize words with " " delimiter
    words = text.split()
    # print words
    for word in words:
        print(word)

def main():

    #fileRead()
    a = Person("Rob")
    x = Person("Thomas")
    y = Person("Mary")
    z = Person("Jeff")

    a.add_parents(x, y)

    z.add_parents(x, y)

    mother = Person("sara")
    grand = Person("Pete")

    grand.add_parents(z, mother)
    ops = Operations()
    ops.list_relation("Thomas", "spouses")
    ops.is_relation("Thomas", "Mary", "spouses")
    grand.list_relation("cousins")



main()
#if __name__ == '__main__':
#    main()
