from UserDict import UserDict


class Useless:
    pass


class FileInfo(UserDict):
    classAttribute = "class attribute, owned by class, not by instance"
    "store file metadata"
    def __init__(self, filename=None):
        """Closest thing to a constructor"""
        UserDict.__init__(self)
        self.name = filename  # instance attribute

    @staticmethod
    def __private_method(self):
        """private methods start with __ """
        pass


class Boat(object):
    def __init__(self, name, loa):
        self.name= name
        self.loa= loa


class CatBoat(Boat):
    def __init__(self, sailarea, * args):
        Boat.__init__(* args)
        self.main_area= sailarea


class Sloop(CatBoat):
    def __init__(self, jib_area, * args):
        CatBoat.__init__(* args)
        self.jib_area= jib_area


def main():
    fileinfo = FileInfo()


if __name__ == '__main__':
    main()