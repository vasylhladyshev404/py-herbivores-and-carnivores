class Animal:
    alive = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.hidden = False
        Animal.alive.append(self)

    def die(self) -> None:
        if self.health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return (
            f"{{\n"
            f"  Name: {self.name},\n"
            f"  Health: {self.health},\n"
            f"  Hidden: {self.hidden}\n"
            f"}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Herbivore) -> None:
        if isinstance(other, Herbivore) and not other.hidden:
            other.health -= 50
            other.die()
