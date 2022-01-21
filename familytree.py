
class Member(object):
    def __init__(self, founder, gender):
       
        self.name = founder
        self.gender = gender
        self.parent = None         
        self.children = []    

    def __str__(self):
        return self.name    

    def add_parent(self, mother):

        self.parent = mother   

    def get_parent(self):

        return self.parent

    def get_chidern(self):
        newlist=[]
        for i in self.children:
            can=True
            for y in newlist:
                if i.name==y.name :
                    can=False
            if can==True:            
                newlist.append(i)
        #print(len(newlist))
        return newlist
    
    def get_parent(self):

        return self.parent 

    def is_parent(self, mother):

        return self.parent == mother  

    def add_child(self, child):

        self.children.append(child)   

    def is_child(self, child):
        return child in self.children
        
    


class Family(object):
    def __init__(self, founder,gender):

        self.names_to_nodes = {}
        self.root = Member(founder,gender)    
        self.names_to_nodes[founder] = self.root   

    def set_children(self, mother, list_of_children):
       
        # convert name to Member node (should check for validity)
        #print(str(self.names_to_nodes)+'fuck')
        mom_node = self.names_to_nodes[mother]  
        # add each child
        for c in list_of_children:           
            self.names_to_nodes[c.name] = c    
            # set child's parent
            c.add_parent(mom_node)        
            # set the parent's child
            mom_node.add_child(c)         
    
    def is_parent(self, mother, kid):
        mom_node = self.names_to_nodes[mother]
        child_node = self.names_to_nodes[kid]
        return child_node.is_parent(mom_node)   

    def is_child(self, kid, mother):
       
        mom_node = self.names_to_nodes[mother]   
        child_node = self.names_to_nodes[kid]
        return mom_node.is_child(child_node)

    def cnt(self, name):
        mother=self.names_to_nodes[name]
        if mother==None:
            return ['0']
        return [str(len(mother.get_chidern()))]
    def ans(self,name):
        anss=[]
        mother=self.names_to_nodes[name]
        while (mother!=None):
            
            parent=mother.get_parent()
            if parent!=None:
                mother=self.names_to_nodes[parent.name]
                anss.append(parent.name)
            else:
                mother=None
        return anss
    def bro(self,name):
        anss=[]
        mother=self.names_to_nodes[name]
        if mother.get_parent() != None:
            for child in mother.get_parent().get_chidern():
                if child.gender=='M' and child.name!=name:
                    anss.append(child.name)

        return anss

    def UNC(self,name):
        anss=[]
        mother=self.names_to_nodes[name]
        if mother.get_parent() != None and mother.get_parent().get_parent():
            father=mother.get_parent().name
            for child in mother.get_parent().get_parent().get_chidern():
                if child.gender=='M' and child.name!=father:
                    anss.append(child.name)

        return anss

    def AUN(self,name):
        anss=[]
        mother=self.names_to_nodes[name]
        if mother.get_parent() != None and mother.get_parent().get_parent():
            father=mother.get_parent().name
            for child in mother.get_parent().get_parent().get_chidern():
                if child.gender=='F' and child.name!=father:
                    anss.append(child.name)

        return anss

    def sis(self,name):
        anss=[]
        mother=self.names_to_nodes[name]
        if mother.get_parent() != None:
            for child in mother.get_parent().get_chidern():
                if child.gender=='F' and child.name!=name:
                    anss.append(child.name)

        return anss

    def dec(self,name):
        anss=[]
        chidern=self.names_to_nodes[name].get_chidern()
        names=[]
        while (chidern!=[]):
            newclidern=[]
            for child in chidern:
                anss.append(child.name)
                #print(child.name)
                newclidern.extend(child.get_chidern())
                #print(len(newclidern))
            chidern=list(set(newclidern))

        return anss
    def search(self,name,types):
        switcher = {
            'ANS': self.ans(name),
            'DEC': self.dec(name),
            'CNT': self.cnt(name),
            'BRO': self.bro(name),
            'SIS': self.sis(name),
            'UNC': self.UNC(name),
            'AUN': self.AUN(name),
        }
        return switcher.get(types, "NuLL")
def normalyze(lines):
    nor=[]
    for x in lines:
        nor.append(x.replace('\n','',1))
    return nor
if __name__ == '__main__':
    with open('input.txt') as f:
        lines = normalyze(f.readlines())
        
        #Test section
        f = None
        for x in lines :
            
            if x.find('*') != -1:
                break
            if f==None:
                f=Family(x.split(':')[0],'M')
            else:
                children=[]
                for y in lines:
                    
                    if x.split(':')[0]==y.split(':')[0]:
                        children.append(Member(y.split(':')[1].split(' ')[0],y[-1]))
                f.set_children(x.split(':')[0],children)
        out=False
        with open('output.txt', 'w') as outFile:
            for x in lines :
                if x.find('*') != -1:
                    out= not out
                if out==True and len(x.split(' '))>1:
                    print(f.search(x.split(' ')[1],x.split(' ')[0]))
                    outFile.write(' '.join(f.search(x.split(' ')[1],x.split(' ')[0])))
                    outFile.write('\n')


        #f.set_children("a", ["b", "c"])

        words = ["zeroth", "first", "second", "third", "fourth", "fifth", "non"]
        print()