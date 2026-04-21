import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            b"""
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hola Mundo DevOps</title>
    <style>
      body {
        margin: 0;
        min-height: 100vh;
        display: grid;
        place-items: center;
        font-family: Arial, sans-serif;
        background: #f4f7fb;
        color: #1f2937;
      }
      main {
        text-align: center;
        padding: 32px;
      }
      h1 {
        font-size: clamp(2rem, 6vw, 4rem);
        margin: 0 0 12px;
      }
      p {
        font-size: 1.2rem;
        margin: 0;
      }
    </style>
  </head>
  <body>
    <main>
      <h1>Hola Mundo</h1>
      <p>Aplicacion web ejecutandose desde Docker.</p>
    </main>
  </body>
</html>
"""
        )


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), HelloHandler)
    print(f"Servidor iniciado en http://0.0.0.0:{port}")
    server.serve_forever()
