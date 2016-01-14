#!/usr/bin/python
import os
from CGIHTTPServer import CGIHTTPRequestHandler
import BaseHTTPServer

web_dir = '/home/stephane/Playground/OECD/search/test-ui/dist/org.oecd.exalead.testframework~webclient~0.1/web'
port = 8888

os.chdir(web_dir)
srv_addr = ("", port)
srv_obj = BaseHTTPServer.HTTPServer(srv_addr, CGIHTTPRequestHandler)
srv_obj.serve_forever()
