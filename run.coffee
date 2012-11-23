#!/usr/bin/env NODE_PATH=./ ./node_modules/coffee-script/bin/coffee

app    = require('express')()
server = require('http').createServer(app)
io     = require('socket.io').listen(server)
zmq    = require 'zmq'
config = require 'config'

server.listen 8080

app.get '/', (req, res) -> res.sendfile "#{__dirname}/index.html"
console.log 'Webserver up and running at http://localhost:8080'

sock = zmq.socket 'pull'
sock.connect config.zmqUrl or 'tcp://127.0.0.1:3333'
console.log "listening to 0MQ"

numConnections = 0

io.sockets.on 'connection', (socket) ->
	numConnections++

	socket.on 'disconnect', -> numConnections--


sock.on 'message', (msg) ->
	console.log "0MQ msg: #{msg}"
	console.log typeof msg

	if numConnections > 0
		io.sockets.emit 'leap-frame', String(msg)
	else
		console.log 'not writing to websocket b/c no one listening'
