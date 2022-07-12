from typing import Union
from heroes import Superman, SuperHero, HeroNews, ChackNorris
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero,
                   place: Union[Tokyo, Kostroma],
                   news: HeroNews,
                   type_of_news: Union['Media', 'Newspaper']):
    hero.find(place)
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    else:
        hero.attack()
    if type_of_news == 'Media':
        news.create_news(hero, place)
    if type_of_news == 'Newspaper':
        news.create_newspaper_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), HeroNews(), 'Newspaper')
    print('-' * 20)
    save_the_place(ChackNorris(), Tokyo(), HeroNews(), 'Media')
    print('-' * 20)
    save_the_place(Superman(), Tokyo(), HeroNews(), 'Newspaper')


