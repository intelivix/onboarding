import pytest
from utils import Preparo

class TestPreparo():
    def setup_method(self):
        self.preparo = Preparo()
        self.preparo.do_a_chambaril()

    def test_avaliar(self):
        assert self.preparo.avaliar() == 'o prato está bom'

    def test_bom(self):
        assert self.preparo.good == True

    def test_slow_cook_oven(self):
        assert self.preparo.slow_cook_oven == True
