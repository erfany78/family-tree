"""
Name the project FamilyTree_Kim.py
"""


class Family_tree():

    def __init__(self):
        self.family_tree = {"siblings": [], "parents": [], "half-siblings": [], "cousins": [], "children": []}

class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree().family_tree

    def add_parents(self, parent_one, parent_two):
        self.family_tree['parents'].append(parent_one)
        self.family_tree['parents'].append(parent_two)

    def add_children(self, child):
        self.family_tree['children'].append(child)

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

        for child in parent_two.family_tree['children']:
            if child not in self.family_tree['siblings'] and self.name is not child.name:
                if child in parent_one.family_tree['children']:
                    self.family_tree['siblings'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-siblings'].append(child)
                    if self not in child.family_tree['half-siblings']:
                        child.family_tree['half-siblings'].append(self)

    def add_cousins(self):
        pass

    def list_relation(self, relation):
        #print(self.family_tree[relation])
        for family_member in self.family_tree[relation]:
            print(family_member.name)

person_list = []

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

    half_p = Person("ewok")
    half = Person("pete")

    a.add_parents(y, z)
    y.add_children(a)
    z.add_children(a)
    a.add_siblings(y, z)

    x.add_parents(y, z)
    y.add_children(x)
    z.add_children(x)
    a.add_siblings(y, z)

    #a.list_relation("siblings")
    #x.list_relation("siblings")

    half.add_parents(half_p, y)
    half_p.add_children(half)
    y.add_children(half)
    half.add_siblings(half_p, y)

    #half.list_relation('half-siblings')
    #half.list_relation('siblings')
    a.list_relation('siblings')



main()
#if __name__ == '__main__':
#    main()
