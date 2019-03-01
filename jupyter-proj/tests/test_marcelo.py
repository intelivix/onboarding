import pytest
from utils import marcelo


class TestMarcelo():

    def test_marcelo(self):
        assert marcelo(0) == 'marcelo'
        assert marcelo('hahaha') == 'marcelo'

    def test_marcelo_nao_e_feio(self):
        assert marcelo(0, False) == 'marcelo bonito'
        assert marcelo(False, False) == 'marcelo bonito'

    def test_marcelo_deu_bronca(self):
        with pytest.raises(Exception):
            assert marcelo(0, None) == 'marcelo'
