# Base state class
class ComputerState:
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current: ', self, ' => switched to new state ', state.name)
            self.__class__ = state
        else:
            print('Current: ', self, ' switching to ', state.name, ' not possible')

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


# Context
class Computer:
    def __init__(self):
        self.state = Off()

    def change(self, state: ComputerState):
        self.state.switch(state)


# === usage ===
c = Computer()
print('computer state: ')
print(c.state.__str__())
c.state.switch(On)
c.state.switch(Suspend)
c.state.switch(Off)
c.state.switch(On)
c.state.switch(Off)
