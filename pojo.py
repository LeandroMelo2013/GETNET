import requests
import sys
from user import User
print(sys.path)

def create_user(api_url, user_data):
    response = requests.post(api_url + "/users", json=user_data.to_dict())
    return response

# CREATE com POJO
if __name__ == "__main__":
    base_url = "https://reqres.in/api"
    new_user_data = User(id=101, name="Joao", job="PO")

    response = create_user(base_url, new_user_data)

    if response.status_code == 201:
        print("Usuário criado com sucesso!")
    else:
        print(f"Falha ao criar usuário. Código de status: {response.status_code}")
        print(response.json())