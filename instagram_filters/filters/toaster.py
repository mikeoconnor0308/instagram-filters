from ..filter import Filter
from ..decorations.vignette import Vignette
from ..decorations.border import Border


class Toaster(Vignette, Border):
    def apply(self):
        self.colortone('#330000', 50, 0)
        self.execute("convert {filename} -modulate 150,80,100 -gamma 1.2 -contrast -contrast {filename}")
        self.vignette('none', 'LavenderBlush3')
        self.vignette('#ff9966', 'none')
        self.border('white')
