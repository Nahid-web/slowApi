def app(environ, start_response):
    print(environ)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello, Nahid Amin and Nafia!"]
