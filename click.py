import time
import pyautogui

# Aguarde alguns segundos antes de iniciar os cliques automáticos
time.sleep(5)

# Número de cliques automáticos
num_clicks = 10

for _ in range(num_clicks):
    pyautogui.click()  # Simula um clique do mouse
    time.sleep(1)  # Aguarda 1 segundo antes do próximo clique
