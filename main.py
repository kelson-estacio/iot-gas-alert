import multiprocessing
import time
import subprocess
import sys

def run_device():
    # Executa o script do dispositivo
    subprocess.run([sys.executable, "device/device_main.py"])

def run_backend():
    # Executa o script do backend
    subprocess.run([sys.executable, "backend/backend_main.py"])

def run_dashboard():
    # Executa o script do dashboard
    subprocess.run([sys.executable, "dashboard/dashboard_app.py"])

if __name__ == "__main__":
    # Iniciar backend e dashboard em processos separados
    device_process = multiprocessing.Process(target=run_device)
    backend_process = multiprocessing.Process(target=run_backend)
    dashboard_process = multiprocessing.Process(target=run_dashboard)

    device_process.start()
    backend_process.start()
    dashboard_process.start()

    print("Todos os componentes iniciados. Pressione Ctrl+C para encerrar.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando todos os processos...")
        device_process.terminate()
        backend_process.terminate()
        dashboard_process.terminate()
        print("Projeto encerrado.")
