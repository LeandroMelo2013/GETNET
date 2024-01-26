import requests
from user import User

def test_create_user():
    base_url = "https://reqres.in/api"
    endpoint = "/users"

    new_user_data = User(id=101, name="Joao", job="PO")

    response = requests.post(base_url + endpoint, json=new_user_data.to_dict())

    assert response.status_code == 201, f"Falha ao criar usuário. Código de status: {response.status_code}"
    
    # Verifique campos obrigatórios
    user_info = response.json()
    assert user_info["name"] == new_user_data.name, f"Campo 'name' incorreto. Esperado: {new_user_data.name}, Obtido: {user_info['name']}"
    assert user_info["job"] == new_user_data.job, f"Campo 'job' incorreto. Esperado: {new_user_data.job}, Obtido: {user_info['job']}"

    print("Usuário criado com sucesso!")

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
