import pytest
from ..funcoes_desenvolvidas_pelo_dev import *



@pytest.mark.estoque
def test_prod_disponivel():
    assert verifica_disponibilidade('Produto A') == True 

@pytest.mark.estoque
def test_prod_n_existir():
    assert verifica_disponibilidade('Produto inexistente') == False 

@pytest.mark.estoque
def test_prod_sem_estoque():
    assert verifica_disponibilidade('Produto B') == 'sem estoque' 

@pytest.mark.estoque
def test_prod_preco_errado():
    assert verifica_disponibilidade('Produto B') == False 


@pytest.mark.cep
def test_cep_valido():
    assert consulta_cep('04542012') == "SP"

@pytest.mark.cep
def test_cep_num():
    assert consulta_cep(5) == False

@pytest.mark.cep
def test_cep_grande():
    assert consulta_cep('827482839223') == False

@pytest.mark.cep
def test_cep_pequeno():
    assert consulta_cep(5) == False

@pytest.mark.cep
def test_cep_num():
    assert consulta_cep('04522012') == False
