import receive, random, socket, ssl, datetime, encrypt, os
def deal_with_client(connstream):

   data = connstream.read()
   imageData =  "%4d%02d%02d%02d%02d0" %(datetime.datetime.now().year,  datetime.datetime.now().month,  datetime.datetime.now().day,  datetime.datetime.now().hour,  datetime.datetime.now().minute)
   imageName =  "%4d%02d%02d%02d%02d%02d%s0.jpg" %(datetime.datetime.now().year,  datetime.datetime.now().month,  datetime.datetime.now().day,  datetime.datetime.now().hour,  datetime.datetime.now().minute, datetime.datetime.now().second, random.choice('abcdefghijklmnopqrstuvwxyz'))
   location = '/images/'+ imageName
   location2 = '/websites/secure/www/'+ imageName
   # null data means the client is finished with us
   f = open(location2, 'wb')
   print "WOOOHOOO BITS BITS BITS"
   
   while data:
      # print bytearray(data)
      f.write(data)
      data = connstream.read()

   f.write(data)
   f.close()
   encrypt.encode(location2, location)
   receive.receive(imageData, imageName)
   os.remove(location2)
   connstream.close()

def do_something(connstream, date):
    return False

if __name__ == '__main__':
    bindsocket = socket.socket()
    bindsocket.bind(('139.78.71.59', 10023))
    bindsocket.listen(5)
    #fix month, day, hour minute to have 0 in front of < 10 numbers
    while True:
       newsocket, fromaddr = bindsocket.accept()
       connstream = ssl.wrap_socket(newsocket,
                                    server_side=True,
                                    certfile="server.crt",
                                    keyfile="server.key",
                                    ssl_version=ssl.PROTOCOL_TLSv1)
       deal_with_client(connstream)
