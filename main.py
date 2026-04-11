import requests
import time

# CONFIG
URL = "https://www.ticketmaster.com.br/event/venda-geral-bts-world-tour-arirang-31-10"
TOKEN = "8613821943:AAH3am77c9X_Er6bKf0UioUApZ_2bXzAFx8"
CHAT_ID = "1805770693"

def enviar_mensagem(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    
    # TESTE
enviar_mensagem("TESTE FUNCIONANDO 🚀")
    

ultimo_alerta = 0

while True:
    try:
        print("🔎 Verificando ingressos...")

        response = requests.get(URL)
        texto = response.text.lower()

        if "buy" in texto or "comprar" in texto or "tickets" in texto:
            agora = time.time()

            if agora - ultimo_alerta > 300:
                print("🔥 INGRESSO DISPONÍVEL!")
                enviar_mensagem("🔥 INGRESSO DISPONÍVEL! CORRE!")
                ultimo_alerta = agora

        else:
            print("❌ Ainda não disponível...")

        time.sleep(60)

    except Exception as e:
        print("Erro:", e)
        time.sleep(60)

