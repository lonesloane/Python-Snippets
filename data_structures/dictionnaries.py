__author__ = 'stephane'


class DicoTest(object):
    def __init__(self):
        pass

    @staticmethod
    def define_dictionary():
        print('**********************')
        print("Define dictionary:")
        print('**********************\n')
        d = {"server": "pilgrim", "database": "master"}
        print(d)
        print("server: " + d["server"])
        print("database: " + d["database"])
        dic = dict(firstname='stephane', lastname='Varin', surname='LoneSloane')
        print(dic)
        dico = {}
        dico['favoriteband'] = "Nirvana"
        dico['favoritegame'] = "Assasin's Creed"
        dico['favoritesport'] = "Rugby"
        print(dico)
        keys = ['Baudelaire', 'Hugo', 'Zola', 'Rabelais']
        values = ['Fleurs du Mal', 'Travailleurs de la mer', 'Germinal', 'Pantagruel']
        zipdic = dict(zip(keys, values))
        print(zipdic)

    @staticmethod
    def modify_dictionary():
        print('\n**********************')
        print("Modify dictionary:")
        print('**********************\n')
        d = {"server": "pilgrim", "database": "master"}
        print(d)
        print("change database")
        d["database"] = "pubs"
        print(d)
        print("add user")
        d["user"] = "stephane"
        print(d)
        d.update([("OS", "Linux"),("Admin", "Yraghael")])
        print(d)

    @staticmethod
    def mixed_datatypes():
        print('\n**********************')
        print("Mixed data types:")
        print('**********************\n')
        print("keys and values can be of mixed data types")
        dd = {"key1": "elem1", "key2": "elem2"}
        d = {"server": "pilgrim", "database": "master", "max_nb_items": 1000, 0: "zero", "anotherArray": dd}
        print(d)

    @staticmethod
    def delete_item():
        print('\n**********************')
        print("Delete item:")
        print('**********************\n')
        d = {"server": "pilgrim", "database": "master", "user": "stephane"}
        print(d)
        print("delete user")
        del d["user"]
        print(d)


    @staticmethod
    def values():
        print('\n**********************')
        print("Values:")
        print('**********************\n')
        d = {"server": "pilgrim", "database": "master", "user": "stephane"}
        vals = d.values()
        print("values of dictionary:", vals)

    @staticmethod
    def get_value():
        print('\n**********************')
        print("Get value:")
        print('**********************\n')
        d = {"server": "pilgrim", "database": "master", "user": "stephane"}
        value = d.get("database")
        print("value of database:", value)

    @staticmethod
    def get_items():
        print('\n**********************')
        print("Get items:")
        print('**********************\n')
        d = {0: "a", 1: "b", 2: "c"}
        t = d.items()
        print(t)
        dd = dict(t)
        print(dd)

    @staticmethod
    def zippit():
        print('\n**********************')
        print("Use zip to create dict:")
        print('**********************\n')
        d = dict(zip(['a', 'b', 'c'], range(3)))
        print(d)

    @staticmethod
    def fill_with_comprehension():
        print('\n**********************')
        print("Use list comprehension to create dict:")
        print('**********************\n')
        d = dict([(str(x)+'^2:', x**2) for x in range(10)])
        print(d)


def main():
    dicotest = DicoTest()
    dicotest.define_dictionary()
    dicotest.modify_dictionary()
    dicotest.mixed_datatypes()
    dicotest.delete_item()
    dicotest.values()
    dicotest.get_value()
    dicotest.get_items()
    dicotest.zippit()
    dicotest.fill_with_comprehension()

if __name__ == '__main__':
    main()