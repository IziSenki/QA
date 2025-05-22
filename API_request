pip install requests
import requests

# Teste básico de API
def testar_api():
    url = "https://jsonplaceholder.typicode.com/users/1"  # API de teste gratuita
    
    try:
        # 1. Faz a requisição
        resposta = requests.get(url)
        
        # 2. Verifica o status (200 = sucesso)
        if resposta.status_code != 200:
            return f"❌ Falha - Status code: {resposta.status_code}"
        
        # 3. Verifica os dados retornados
        dados = resposta.json()
        if "name" not in dados:
            return "❌ Falha - Chave 'name' não encontrada"
            
        # 4. Se tudo ok
        return f"✅ Sucesso - Usuário: {dados['name']}"
    
    except Exception as e:
        return f"❌ Erro: {str(e)}"

# Executa e mostra o resultado
print(testar_api())
