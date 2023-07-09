from random import randint

DEFAULT_ATTACK: int = 5
DEFAULT_DEFENCE: int = 10
DEFAULT_STAMINA: int = 80


class Character:
    BRIEF_DESC_CHAR_CLASS: str = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK: tuple = (1, 3)
    RANGE_VALUE_DEFENCE: tuple = (1, 5)
    SPECIAL_SKILL: str = 'Удача'
    SPECIAL_BUFF: int = 15

    def __init__(self, name) -> None:
        self.name = name

    def attack(self):
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанесен урон противнику, равный '
                f'{value_attack}.')

    def defence(self):
        value_defence: int = (f'{DEFAULT_DEFENCE}'
                              f' + {randint(*self.RANGE_VALUE_DEFENCE)}')
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}')

    def __str__(self) -> str:
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' дерзкий воин ближнего боя. '
                                  'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK: tuple = (3, 5)
    RANGE_VALUE_DEFENCE: tuple = (5, 10)
    SPECIAL_SKILL: str = 'Выносливость'
    SPECIAL_BUFF: int = DEFAULT_STAMINA + 25


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' находчивый воин дальнего боя. '
                                  'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK: tuple = (5, 10)
    RANGE_VALUE_DEFENCE: tuple = (-2, 2)
    SPECIAL_SKILL: str = 'Атака'
    SPECIAL_BUFF: int = DEFAULT_ATTACK + 40


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS: str = (' могущественный заклинатель. '
                                  'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK: tuple = (-3, -1)
    RANGE_VALUE_DEFENCE: tuple = (2, 5)
    SPECIAL_SKILL: str = 'Защита'
    SPECIAL_BUFF: int = DEFAULT_DEFENCE + 30


def choice_char_class(char_name: str) -> Character:
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = None
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ').lower()
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
            print(char_class)
            approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                                   'или любую другую кнопку, '
                                   'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(char_class: Character) -> None:
    """
    Принимает на вход имя и класс персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        # Замените блок условных операторов на словарь
        # и вынесите его из цикла. Здесь останется одно условие
        # принадлежности введённой команды словарю.
        # В функции print() будет вызываться метод класса,
        # который соответствует введённой команде.
        selected_training = {'attack': char_class.attack,
                             'defence': char_class.defence,
                             'special': char_class.special}
        if cmd in selected_training:
            result = selected_training[cmd]()
            print(result)


def main() -> None:
    """Точка входа.
    При запуске char_name просит ввести имя
    В char_class складется выбранный класс
    """
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    start_training(char_class)


if __name__ == '__main__':
    main()