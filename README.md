leap.io
=======

##Description
This is a very simple harness that allows data from the Leap Motion prototype SDK to be sent out to a client via a websocket.  Currently it uses ZeroMQ push/pull, but it should be possible to change to pub/sub for broadcast to more than one client.

##How to run
 1. Install [ZeroMQ](http://www.zeromq.org/) - brew install zmq
 2. Run 'npm install'
 3. Install [python](http://www.python.org/download/)
 4. Install [PIP](http://www.pip-installer.org/en/latest/installing.html) (you may have to setup distribute or easy_install first)
 5. Run 'pip install pyzmq' (https://github.com/zeromq/pyzmq)
 6. Run 'python producer.py' and wave your hand over the Leap motion to get things going (output will hang trying to send the first message)
 7. In separate terminal, run './run.coffee'
 8. Open browser to http://localhost:8080
 9. Enjoy the changing text and debug messages scrolling by in the console

