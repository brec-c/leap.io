################################################################################
# Copyright (C) 2012 Leap Motion, Inc. All rights reserved.                    #
# NOTICE: This developer release of Leap Motion, Inc. software is confidential #
# and intended for very limited distribution. Parties using this software must #
# accept the SDK Agreement prior to obtaining this software and related tools. #
# This software is subject to copyright.                                       #
################################################################################

import zmq
import Leap
import sys

class SampleListener(Leap.Listener):

  def onInit(self, controller):

    ctx = zmq.Context()
    self.zmqSocket = ctx.socket(zmq.PUSH)
    self.zmqSocket.bind('tcp://127.0.0.1:3333')

    print "Initialized"

  def onConnect(self, controller):
    print "Connected"

  def onDisconnect(self, controller):
    print "Disconnected"

  def onFrame(self, controller):
    # Get the most recent frame and report some basic information
    frame = controller.frame()

    hands = frame.hands()
    numHands = len(hands)
    print "Frame id: %d, timestamp: %d, hands: %d" % (
          frame.id(), frame.timestamp(), numHands)

    if numHands >= 1:
      # Get the first hand
      hand = hands[0]

      # Check if the hand has any fingers
      fingers = hand.fingers()
      numFingers = len(fingers)
      if numFingers >= 1:
        # Calculate the hand's average finger tip position
        pos = Leap.Vector(0, 0, 0)
        for finger in fingers:
          tip = finger.tip()
          pos.x += tip.position.x
          pos.y += tip.position.y
          pos.z += tip.position.z
        pos = Leap.Vector(pos.x/numFingers, pos.y/numFingers, pos.z/numFingers)
        msg = "Hand has %d fingers with average tip position (%f, %f, %f)" % (
              numFingers, pos.x, pos.y, pos.z)
        print msg

        self.zmqSocket.send_json({
          "message" : msg
        })

      # Check if the hand has a palm
      palmRay = hand.palm()
      if palmRay is not None:
        # Get the palm position and wrist direction
        palm = palmRay.position
        wrist = palmRay.direction
        direction = ""
        if wrist.x > 0:
          direction = "left"
        else:
          direction = "right"
        print "Hand is pointing to the %s with palm position (%f, %f, %f)" % (
              direction, palm.x, palm.y, palm.z)


def main():
  # Create a sample listener and assign it to a controller to receive events
  listener = SampleListener()
  controller = Leap.Controller(listener)

  # Keep this process running until Enter is pressed
  print "Press Enter to quit..."
  sys.stdin.readline()

  # The controller must be disposed of before the listener
  controller = None


if __name__ == "__main__":
  main()
