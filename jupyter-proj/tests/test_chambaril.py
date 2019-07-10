import pytest
from utils import Chambaril


class TestChambaril():

    def setup_method(self, method):
        self.chamba = Chambaril()

    def teardown_method(self, method):
        self.chamba = None

    def test_chambaril_preco(self):
        assert self.chamba.preco == 10.00
        
    def test_chambaril_ingredientes(self):
        assert isinstance(self.chamba.ingredientes, list)
        assert 'paio' in self.chamba.ingredientes
        assert 'pirao' in self.chamba.ingredientes
        assert 'pimenta' not in self.chamba.ingredientes

    def test_chambaril_temperatura(self):
        assert self.chamba.temperatura > 25
        self.chamba.temperatura = 10
        assert self.chamba.is_cold
        self.chamba.temperatura = 100
        assert self.chamba.is_hot

    def test_chambaril_ingrediente_removido(self):
        assert not self.chamba.faltou_ingredientes
        ingrediente_removido = self.chamba.ingredientes.pop(0)
        assert self.chamba.faltou_ingredientes

    def test_chambaril_pimenta(self):
        assert not self.chamba.apimentado
        self.chamba.marcelo_colocou_pimenta()
        assert self.chamba.apimentado


class TestChambarilove():

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print('setup class')

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print('teardown class')

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    print('setup module')

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print('teardown module')