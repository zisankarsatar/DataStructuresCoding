contact_list = {'zisan' : {'tel_no' : '+31xxxxxxxxx',
                            'mail': 'z@kc.com',
                            'addres': 'zaandam'},
                'fatma' : {'tel_no' : '+90xxxxxxxxx',
                            'mail': 'f@k.com',
                            'addres': 'kmaras'},
                'defne' : {'tel_no' : '+32xxxxxxxxx',
                            'mail': 'd@v.com',
                            'addres': 'brussels'},
                'drev' : {'tel_no' : '+1505xxxxxxxxx',
                            'mail': 'd@k.com',
                            'addres': 'Albuquerque'},
                'maria' : {'tel_no' : '+331xxxxxxxxx',
                            'mail': 'm@k.com',
                            'addres': 'Normandiya'}}

class contactBook():
    def __init__(self):
        #self.contact_list = open("data.txt", "r", encoding="utf-8").read()    
        ...
        
    def get_all_list(self):
        if contact_list is not None:
            return contact_list
        else:
            return 'There is saved'
        
    def search(self):
        name = input(f"pls put name: ")
        if name in contact_list:
            return contact_list[name]
        else:
            return 'No such person exists'
        
    def create_new_contact(self):
        name = input(f"pls put name: ")
        tel_no = input(f"pls put telephone number: ")
        mail = input(f"pls put mail: ")
        addres = input(f"pls put addres: ")
        
        contact_list[name] = {'tel_no': tel_no, 'mail':mail, 'addres':addres}
        
        return contact_list[name]
    
    def delete_contact(self, name):
        sure = input(f"are you sure(y/n): ")
        if sure == 'y' and name in contact_list:
            del contact_list[name]
            return contact_list
        else:
            return 'ok'
        
    def update_contact(self):
        name = input(f"pls put name which you want to change: ")
        tel_no = input(f"pls put new telephone number: ")
        mail = input(f"pls put new mail: ")
        addres = input(f"pls put new addres: ")
        
        contact_list[name] = {'tel_no': tel_no, 'mail':mail, 'addres':addres}
        
        return contact_list


c = contactBook()
#print(c.create_new_contact())
#print(c.delete_contact('zisan'))
print(c.update_contact())