
pip install selenium

# Configuração rápida do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura o navegador (Chrome em modo headless)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Roda sem abrir janela
driver = webdriver.Chrome(options=options)

# Teste 1: Acessar site e verificar título
driver.get("https://www.python.org")
print("✅ Página carregada" if "Python" in driver.title else "❌ Falha no carregamento")

# Teste 2: Busca no site
campo_busca = driver.find_element(By.ID, "id-search-field")
campo_busca.send_keys("selenium")
campo_busca.submit()
time.sleep(2)  # Aguarda resultados

# Verifica resultados
resultados = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
print(f"🔍 {len(resultados)} resultados encontrados")

# Fecha o navegador
driver.quit()
