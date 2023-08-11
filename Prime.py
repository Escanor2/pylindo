import psutil
import time
from pymsgbox import alert
import pygame

def are_programs_running(program_names):
    running_count = 0
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() in program_names:
            running_count += 1

    return running_count

programs_to_check = ["mir4g.exe", "mir4g.exe"]  # Substitua pelos nomes dos programas que você deseja verificar

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

while True:
    num_programs_running = are_programs_running(programs_to_check)

    title = f"Programas rodando: {num_programs_running}/{len(programs_to_check)}"
    message = "Status dos Programas"

    if num_programs_running == len(programs_to_check):
        pass  # Ambos os programas estão abertos, não há ação especial
    else:
        # Reproduz o arquivo de áudio MP3
        pygame.mixer.music.load('wake.mp3')  # Substitua pelo caminho do arquivo MP3
        pygame.mixer.music.play()

        alert("Alerta: Programas não estão rodando!", message)

    alert(title, message)

    time.sleep(600)  # Aguarda 10 minutos (600 segundos) antes de verificar novamente
