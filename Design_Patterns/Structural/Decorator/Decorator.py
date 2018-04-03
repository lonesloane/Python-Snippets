class IWindow:
    def build(self): pass


class AbstractWindowDecorator(IWindow):
    """
    Maintain a reference to a Window object and
    define an interface that conform's to IWindow
    """

    def __init__(self, window):
        self._window = window

    def build(self): pass


class Window(IWindow):

    def build(self):
        print('Building window')


class BorderDecorator(AbstractWindowDecorator):

    def add_border(self):
        print('Adding border')

    def build(self):
        self.add_border()
        self._window.build()


class VerticalSBDecorator(AbstractWindowDecorator):

    def add_vertical_scrollbar(self):
        print('Adding vertical scrollbar')

    def build(self):
        self.add_vertical_scrollbar()
        self._window.build()


class HorizontalSBDecorator(AbstractWindowDecorator):

    def add_horizontal_scrollbar(self):
        print('Adding horizontal scrollbar')

    def build(self):
        self.add_horizontal_scrollbar()
        self._window.build()


# === Usage ===


w = Window()
w.build()

wb = BorderDecorator(w)
wb.build()

wbv = VerticalSBDecorator(wb)
wbv.build()

full_window = HorizontalSBDecorator(wbv)
full_window.build()