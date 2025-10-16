import time
import subprocess
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

APP_SCRIPT = "main.py"

def cerrar_instancia_anterior(nombre_script):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        if proc.info['cmdline'] and nombre_script in " ".join(proc.info['cmdline']):
            print(f"🛑 Cerrando instancia PID {proc.pid}")
            proc.terminate()
            proc.wait()
            print("✅ Instancia cerrada")
            return True
    print("ℹ️ No se encontró instancia activa")
    return False

class ReiniciarApp(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"📁 Evento detectado: {event.src_path}")
        if (
            event.src_path.endswith(".py")
            and "__pycache__" not in event.src_path
            and "watcher.py" not in event.src_path
        ):
            print(f"🔄 Cambio válido en: {event.src_path}")
            cerrar_instancia_anterior(APP_SCRIPT)
            print("🚀 Lanzando nueva instancia...")
            subprocess.Popen(["python", APP_SCRIPT])
        else:
            print("⏭ Cambio ignorado")

# 🔄 Lanzamiento inicial controlado
cerrar_instancia_anterior(APP_SCRIPT)
print("🚀 Lanzando instancia inicial...")
subprocess.Popen(["python", APP_SCRIPT])

# 🧭 Activar el observador
observer = Observer()
observer.schedule(ReiniciarApp(), path=".", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
