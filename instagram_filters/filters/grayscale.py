from ..filter import Filter
from ..decorations.vignette import Vignette


class Grayscale(Filter):
    def apply(self):
        self.execute("convert {filename} -set colorspace Gray -separate -average {filename}")