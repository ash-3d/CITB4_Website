#!/usr/bin/env uv run python
# /// script
# [run]
# dependencies = [
#   "livereload",
# ]
# ///

from livereload import Server, shell

server = Server()

# Watch the main HTML, CSS, and JS files, and the images directory
server.watch('../../index.html', shell('echo "index.html changed"'))
server.watch('../assets/css/style.css', shell('echo "style.css changed"'))
server.watch('../pages/', shell('echo "pages changed"'))
server.watch('../../images/', shell('echo "images changed"'))
server.watch('../../video/', shell('echo "video changed"'))
# server.watch('projects.html', shell('echo "projects.html changed"'))
# server.watch('photography.html', shell('echo "photography.html changed"'))
# server.watch('hobbies.html', shell('echo "hobbies.html changed"'))
# server.watch('images/', shell('echo "images changed"'))
# server.watch('script.js', shell('echo "script.js changed"'))

# Serve the current directory
server.serve(root='../../', port=8000, open_url_delay=0)
