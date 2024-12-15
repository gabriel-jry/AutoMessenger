# Importar bibliotecas
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from pyperclip import copy
from time import sleep

def iniciar_navegador():
    """Inicializa o navegador e abre o WhatsApp Web."""
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://web.whatsapp.com/')
    return navegador

def aguardar_login(navegador, timeout=300):
    """Aguarda o login no WhatsApp Web."""
    try:
        WebDriverWait(navegador, timeout).until(
            EC.presence_of_element_located((By.ID, 'side'))
        )
    except:
        print("Login não detectado. Encerrando...")
        navegador.quit()
        exit()

def buscar_contato(navegador, contato):
    """Busca por um contato no WhatsApp Web."""
    try:
        busca = navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
        busca.clear()
        busca.send_keys(contato)
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'matched-text'))
        )
        busca.send_keys(Keys.ENTER)
    except:
        print(f"Contato '{contato}' não encontrado.")
        navegador.quit()
        exit()

def enviar_mensagem(navegador, mensagem):
    """Envia uma mensagem para o contato selecionado."""
    try:
        campo_mensagem = navegador.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
        )
        copy(mensagem)
        campo_mensagem.send_keys(Keys.CONTROL + 'v')
        campo_mensagem.send_keys(Keys.ENTER)
    except:
        print("Erro ao enviar a mensagem.")
        navegador.quit()
        exit()

def main():
    """Executa o bot para envio de mensagens no WhatsApp Web."""
    contatos = [
        'Contato 1', 'Contato 2', 'Contato 3', 
        'Contato 4', 'Contato 5', 'Contato 6', 'Contato 7'
    ]
    mensagem = "Olá! 👋 Esta é uma mensagem automatizada enviada pelo AutoMessenger. Espero que você esteja bem!"

    navegador = iniciar_navegador()
    aguardar_login(navegador)

    for contato in contatos:
        buscar_contato(navegador, contato)
        enviar_mensagem(navegador, mensagem)
        sleep(1.5)

    print("Mensagens enviadas com sucesso!")
    navegador.quit()

if __name__ == "__main__":
    main()
