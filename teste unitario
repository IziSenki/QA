import unittest

# Função para testar
def multiplicar(a, b):
    """Multiplica dois números"""
    return a * b

# Classe de testes
class TestesMatematicos(unittest.TestCase):
    def test_multiplicacao(self):
        """Testa vários cenários de multiplicação"""
        self.assertEqual(multiplicar(2, 3), 6)       # Positivos
        self.assertEqual(multiplicar(-1, 5), -5)     # Negativo e positivo
        self.assertEqual(multiplicar(0, 100), 0)     # Zero
        self.assertEqual(multiplicar(-2, -2), 4)     # Dois negativos

# Executa os testes
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
