#!/usr/bin/python

# Equivalent of "tail -f" as a webpage using websocket
# Usage: webtail.py PORT FILENAME
# Tested with tornado 2.1

# Thanks to Thomas Pelletier for it's great introduction to tornado+websocket
# http://thomas.pelletier.im/2010/08/websocket-tornado-redis/

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import sys
import os
import json
import time

PORT = int(sys.argv[1])
TEMPLATE = open('template.html').read()

class PingHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket open")

    def on_message(self, message):
        print("received %s" % message)
        msg = json.loads(message)
        msg['server_tx'] = int(time.time()*1000)
        self.write_message(json.dumps(msg))
        
    def on_close(self):
        print "WebSocket close"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(TEMPLATE % (self.request.host))


application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/ping/', PingHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': './static'}),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)

    io_loop = tornado.ioloop.IOLoop.instance()
    try:
        io_loop.start()
    except SystemExit, KeyboardInterrupt:
        io_loop.stop()
        tailed_file.close()
