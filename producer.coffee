#!/usr/bin/env NODE_PATH=./ ./node_modules/coffee-script/bin/coffee

config = require 'config'

zmq = require 'zmq'
sock = zmq.socket 'push'

sock.bindSync config.zmqUrl
console.log "Producer bound to 0MQ"

setInterval (->
	console.log 'sending...'
	sock.send "testing: #{new Date}"
), 5
