
import os
import pytest
from flask import app
from models import Produto
from database import Session


@pytest.fixture
def client():
    app.config['TESTING'] = True
    os.environ['DATABASE_URL'] = 'postgresql://postgres:Artur@localhost:5432/postgres'
    
    with app.test_client() as client:
        yield client    

def test_cadastrar_produto(client):
    payLoad = {
        "name": "Minecraft",
        "description": "Game de bloco criativo",
        "preco": 400.00
    }
    
    response = client.post("/produtos/cadastrar", json=payLoad)
    data = response.get_json()
    assert data["name"] == "Minecraft"
    