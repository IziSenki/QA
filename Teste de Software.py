Teste de Software é o processo de verificar se um sistema funciona conforme o esperado. Existem diferentes tipos de testes, cada um com um propósito específico no ciclo de desenvolvimento de software:

Teste Unitário - Valida funções isoladas

Teste de Integração - Verifica se componentes interagem corretamente

Teste de Sistema - Avalia o sistema completo

Teste de Aceitação - Confirma se atende às necessidades do usuário

Teste de Regressão - Garante que mudanças não causem novos erros

Todos são essenciais para garantir a qualidade e confiabilidade do software.

Exemplos Práticos em Python
1. Teste Unitário
Valida uma função isolada (módulo, classe ou método).
def multiplicar(a, b):
    return a * b

def test_multiplicar():
    assert multiplicar(2, 3) == 6       # Caso positivo
    assert multiplicar(-1, 5) == -5     # Caso com número negativo
    assert multiplicar(0, 10) == 0      # Caso com zero
    print("✅ Teste Unitário passou!")

test_multiplicar()

2. Teste de Integração
Verifica a interação entre componentes.

def autenticar(usuario, senha):
    return usuario == "user" and senha == "pass"

def acessar_painel(usuario, senha):
    if autenticar(usuario, senha):
        return "Painel acessado"
    return "Acesso negado"

def test_acessar_painel():
    assert acessar_painel("user", "pass") == "Painel acessado"     # Credenciais corretas
    assert acessar_painel("user", "errado") == "Acesso negado"      # Senha incorreta
    print("✅ Teste de Integração passou!")

test_acessar_painel()

3. Teste de Sistema
Avalia o sistema como um todo.

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def total_livros(self):
        return len(self.livros)

def test_biblioteca():
    biblio = Biblioteca()
    biblio.adicionar_livro("Livro A")
    biblio.adicionar_livro("Livro B")
    assert biblio.total_livros() == 2
    print("✅ Teste de Sistema passou!")

test_biblioteca()

4. Teste de Aceitação
Confirma se o sistema atende aos requisitos do usuário.

def test_aceitacao():
    resultado = acessar_painel("user", "pass")
    assert resultado == "Painel acessado"
    print("✅ Teste de Aceitação passou!")

test_aceitacao()


5. Teste de Regressão
Garante que alterações não quebrem funcionalidades existentes.


def test_regressao():
    assert multiplicar(4, 5) == 20  # Verifica se a função ainda funciona após mudanças
    print("✅ Teste de Regressão passou!")

test_regressao()


