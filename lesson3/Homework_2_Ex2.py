from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """Выводит в консоль даты показа фильмов."""
        for i in self.dates:
            iterable = i[0]
            while True:
                if iterable == i[1]:
                    print(iterable)
                    break
                print(iterable)
                iterable += timedelta(days=1)


if __name__ == '__main__':
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 12)),
      (datetime(2020, 12, 30), datetime(2021, 1, 7))
    ])

    for d in m.schedule():
        print(d)
