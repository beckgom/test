#!/usr/bin/python
#-*- coding: utf-8 -*-
import os, time, socket, glob, sys
from daemon import Daemon

class MyDaemon(Daemon):
  def run(self):
    while True:
      job()
      time.sleep(1*60*60) ## check in every minute
    


def job():
  pass

def main():
  daemon = MyDaemon('/tmp/daemon-example.pid')
  if len(sys.argv) == 2:
    if 'start' == sys.argv[1]:
      daemon.start()
      print 'daemon is running'
    elif 'stop' == sys.argv[1]:
      daemon.stop()
      print 'daemon is killed'
    elif 'restart' == sys.argv[1]:
      daemon.restart()
      print 'daemon is restarted'
    else:
      print 'unknown command'
      sys.exit(2)
    sys.exit(0)
  else:
    print 'usage: %s start/stop/restart' % sys.argv[0]
    sys.exit(2)

if __name__ == '__main__':
  main()
