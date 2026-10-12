class Hostel:
    def __init__(self):
        self.list_person=[]

    def Add_person(self, name, age, id):
        for person in self.list_person:
            if  person['id']==id:
                print("the person is already exist")
            else:
                person={
                    'name':name,
                     'id':id,
                     'age':age}
                self.list_person.append(person)
                print("the person is add successfully")   
    def remove_             