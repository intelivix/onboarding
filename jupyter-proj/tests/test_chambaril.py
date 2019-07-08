import pytest
from utils import Chambaril


class TestChambaril():

    def test_chambaril_preco(self):
        chamba = Chambaril()
        assert chamba.preco == 10.00
        
    def test_chambaril_ingredientes(self):
        chamba = Chambaril()
        assert isinstance(chamba.ingredientes, list)
        assert 'paio' in chamba.ingredientes
        assert 'pirao' in chamba.ingredientes
        assert 'pimenta' not in chamba.ingredientes

    def test_chambaril_temperatura(self):
        chamba = Chambaril()
        assert chamba.temperatura > 25
        chamba.temperatura = 10
        assert chamba.is_cold
        chamba.temperatura = 100
        assert chamba.is_hot

    def test_chambaril_ingrediente_removido(self):
        chamba = Chambaril()
        assert not chamba.faltou_ingredientes
        ingrediente_removido = chamba.ingredientes.pop(0)
        assert chamba.faltou_ingredientes

    def test_chambaril_pimenta(self):
        chamba = Chambaril()
        assert not chamba.apimentado
        chamba.marcelo_colocou_pimenta()
        assert chamba.apimentado

