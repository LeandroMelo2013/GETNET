import requests
import jsonschema
from jsonschema import validate

BASE_URL = "https://reqres.in/api/"

def test_create_user():
    # Dados do usuário a serem criados
    user_data = {
        "name": "Leandro Melo",
        "job": "QA Engineer",
        "id": "001"
    }

    # Requisição POST para criar um usuário
    response = requests.post(f"{BASE_URL}users", json=user_data)
    
    # Validação do Status Code
    assert response.status_code == 201, f"Erro no Status Code: {response.status_code}"
    
    # Validação dos Campos Obrigatórios na Resposta
    response_data = response.json()
    assert "id" in response_data, "Campo 'id' não encontrado na resposta"
    assert "createdAt" in response_data, "Campo 'createdAt' não encontrado na resposta"

    # Conversão da propriedade 'id' para um número
    if 'id' in response_data:
        response_data['id'] = int(response_data['id'])
        
    # Validação do Contrato (Schema) da Resposta
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "createdAt": {"type": "string"}
            # Adicione outras propriedades conforme necessário
        },
        "required": ["id", "createdAt"]
    }
    
    try:
        validate(response_data, user_schema)
        print("Teste bem-sucedido! Contrato validado.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Erro na validação do contrato: {e}")

if __name__ == "__main__":
    test_create_user()