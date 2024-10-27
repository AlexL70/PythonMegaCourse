class User:
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year

    def get_name(self) -> str:
        return self.name.capitalize()

    def age(self, current_year: int) -> int:
        return current_year - self.birth_year


user = User("alice", 1999)
print(f"User {user.get_name()} is {user.age(2023)} years old")
