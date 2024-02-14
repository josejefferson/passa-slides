# Define o título da janela
try:
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW('Passa Slides')
except:
    pass

from pynput.keyboard import Key, Controller
from bottle import route, run, response, static_file, HTTPError
from texts import print_texts

PORT = 14859
keyboard = Controller()

# Rotas estáticas (página da web)
@route('/')
def serve_index():
    return static_file('index.html', root='./static')

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./static')

# Slide anterior
@route('/control/prev')
def prev():
    keyboard.tap(Key.left)
    response.status = 204

# Próximo slide
@route('/control/next')
def next():
    keyboard.tap(Key.right)
    response.status = 204

# Primeiro slide
@route('/control/first')
def prev():
    keyboard.tap(Key.home)
    response.status = 204

# Último slide
@route('/control/last')
def next():
    keyboard.tap(Key.end)
    response.status = 204

# Ir para slide
@route('/control/goto/<slide>')
def goto(slide):
    if not slide.isnumeric():
        raise HTTPError(status=400, body='Invalid integer')
    
    slide = int(slide)

    if slide <= 0:
        raise HTTPError(status=400, body='Slide must be greater than 0')

    for key in str(slide):
        keyboard.tap(key)
    keyboard.tap(Key.enter)

    response.status = 204

print_texts()
run(host='0.0.0.0', port=PORT, quiet=True)
