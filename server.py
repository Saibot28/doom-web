from http.server import HTTPServer, SimpleHTTPRequestHandler
import mimetypes

# Make sure .zip files have the correct MIME type
mimetypes.add_type('application/zip', '.zip')

# Set the host and port
host = 'localhost'
port = 8080

# Create the HTTP server
server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"Serving HTTP on {host} port {port} (http://{host}:{port}/) ...")

# Start serving
server.serve_forever()
