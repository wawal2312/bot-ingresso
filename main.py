from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import webbrowser
import os

# ===== CONFIG =====
URL = "https://www.ticketmaster.com.br/event/venda-geral-bts-world-tour-arirang-31-10"

TOKEN = "8613821943:AAH3am77c9X_Er6bKf0UioUApZ_2bXzAFx8"
CHAT_ID = "1805770693"

# ==================

def enviar_mensagem(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def tocar_alarme():
    for _ in range(3):
        os.system("start https://www.youtube.com/watch?v=QH2-TGUlwu4")
        time.sleep(2)

def iniciar_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    time.sleep(10)
    return driver

driver = iniciar_driver()
ultimo_alerta = 0

while True:
    try:
        print("🔎 Verificando ingressos...")

        botoes = driver.find_elements(By.XPATH, "//button")

        for botao in botoes:
            texto = botao.text.lower()

            if "buy" in texto or "comprar" in texto or "tickets" in texto:
                agora = time.time()

                if agora - ultimo_alerta > 120:
                    print("🔥🔥🔥 INGRESSO DISPONÍVEL 🔥🔥🔥")

                    enviar_mensagem("🔥 INGRESSO DISPONÍVEL! CORRE AGORA!!!")

                    # abre várias abas
                    for _ in range(3):
                        webbrowser.open(URL)

                    tocar_alarme()

                    ultimo_alerta = agora

        print("❌ Ainda não disponível...")
        time.sleep(30)
        driver.refresh()

    except Exception as e:
        print("⚠️ Erro:", e)
        print("♻️ Reiniciando navegador...")

        try:
            driver.quit()
        except:
            pass

        time.sleep(5)
        driver = iniciar_driver()
