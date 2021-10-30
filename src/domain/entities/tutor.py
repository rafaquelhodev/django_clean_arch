class Tutor:
    def __init__(self, id: str, name: str, email: str) -> None:
        self.id: str = id
        self.__name: str = name
        self.__email: str = email
        self.__validate_owner()

    def __validate_owner(self) -> None:
        if self.__name == "":
            raise Exception("An owner must have a name")

        return

    def get_email(self):
        return self.__email
