class BaseAction:
    POSSIBLE_GAME_RESULTS = {
        'Rock': {'Scissors': True, 'Paper': False},
        'Paper': {'Scissors': False, 'Rock': True},
        'Scissors': {'Paper': True, 'Rock': False},
    }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.POSSIBLE_GAME_RESULTS[self.name][other.name]

    def __hash__(self):
        return hash(self.name)


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
