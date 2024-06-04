from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, start_http_server
import http.server

METRICS_PORT = 8001
APP_PORT = 8000
class HandleRequests(http.server.BaseHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        self.send_header("context-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Document</title></head><body style='color: #333; margin-top: 30px;'><center><h1> Hello this is Arafat and this is my Prometheus Server!!</h1></center></body></html>", "utf-8"))
        self.wfile.close()
if __name__ == "__main__":
        start_http_server(METRICS_PORT)
        server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
        server.serve_forever()