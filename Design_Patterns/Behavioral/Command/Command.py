class Screen:
    def __init__(self, text=''):
        self.text = text
        self.clipboard = ''

    def cut(self, start=0, end=0):
        self.clipboard = self.text[start:end]
        self.text = self.text[:start] + self.text[end:]

    def paste(self, offset=0):
        self.text = self.text[:offset] + self.clipboard + self.text[offset:]

    def clear_clipboard(self):
        self.clipboard = ''

    def length(self):
        return len(self.text)

    def __str__(self):
        return self.text


class ScreenCommand:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.previous_state = screen.text

    def execute(self): pass

    def undo(self): pass


class CutCommand(ScreenCommand):
    def __init__(self, screen: Screen, start=0, end=0):
        super().__init__(screen)
        self.start = start
        self.end = end

    def execute(self):
        self.screen.cut(start=self.start, end=self.end)

    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state


class PasteCommand(ScreenCommand):
    def __init__(self, screen: Screen, offset=0):
        super().__init__(screen)
        self.offset = offset

    def execute(self):
        self.screen.paste(offset=self.offset)

    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state


class ScreenInvoker:
    def __init__(self):
        self.history = []

    def store_and_execute(self, command: ScreenCommand):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            self.history.pop().undo()


# === Usage ===
invoker = ScreenInvoker()

screen = Screen("Souvent pour s'amuser les hommes d'equipage")
print(screen.__str__())

cut = CutCommand(screen, 7, 12)
invoker.store_and_execute(cut)
print(screen.__str__())

paste = PasteCommand(screen, 16)
invoker.store_and_execute(paste)
print(screen.__str__())

invoker.undo_last()
print(screen.__str__())

invoker.undo_last()
print(screen.__str__())
