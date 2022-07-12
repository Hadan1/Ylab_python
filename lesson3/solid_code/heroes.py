from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder


class SuperHero(ABC):
    """Действия героев."""

    @abstractmethod
    def find(self, place):
        ...

    @abstractmethod
    def attack(self):
        ...


class GunMixin:

    def fire_a_gun(self):
        print('PIU PIU')


class LaserMixin:

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class RondHouseKickMixin:

    def roundhouse_kick(self):
        print('Bump')


class UltimateWeaponMixin:

    def ultimate(self):
        if self.can_use_ultimate_attack:
            LaserMixin.incinerate_with_lasers(self)


class HeroNews:
    """Передача новостей о героях в медиа."""
    @staticmethod
    def create_news(hero, place):
        """Передача в медиа."""
        place_name = getattr(place, 'name', 'place')
        print(f'{hero.name} saved the {place_name}!')

    @staticmethod
    def create_newspaper_news(hero, place):
        """Передача в газеты."""
        place_name = getattr(place, 'name', 'place')
        print(f'SUPERHERO TOWN PAPER NEWS {hero.name} saved the {place_name}!')


class Superman(SuperHero, UltimateWeaponMixin, LaserMixin, RondHouseKickMixin):
    """Супермэн."""
    def __init__(self, name='Clark Kent', can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def attack(self):
        return self.roundhouse_kick()

    def find(self, place):
        self.finder.get_antagonist(place)


class ChackNorris(SuperHero, GunMixin, RondHouseKickMixin, ):
    """Чак Норрис."""
    def __init__(self, name='Chuck Norris', can_use_ultimate_attack=False):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def attack(self):
        return self.fire_a_gun()

    def find(self, place):
        self.finder.get_antagonist(place)
