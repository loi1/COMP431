import socket
import sys

def server():
    s = socket.socket()
    host = socket.getfqdn() #'localhost' #152.2.128.83 for snapper
    port = sys.argv[1]
    s.bind((host, port))
    s.listen(1)
    while True:
        try:
            c,addr = s.accept()
        except:
            sys.stdout.write('Error -- cannot connect')
            sys.exit()
        c.send('220 '+host) #1
        helo = c.recv(1024)
        if (helo[:4] != 'HELO'): #4
            c.close()
            sys.stdout.write('Error -- wrong cmd')
            continue
        c.send('250 Hello '+helo[5:]+' pleased to meet you') #5
        #MAIL FROM:
        sender = c.recv(1024)
        if (sender[:10] != 'MAIL FROM:'): #8
            c.close()
            sys.stdout.write('Error -- wrong cmd')
            continue
        else:
            c.send('250 OK') #9
        #RCPT TO:
        rcpts = []
        rcpt = c.recv(1024)
        if (rcpt[:8] != 'RCPT TO:'): #12
            c.close()
            sys.stdout.write('Error -- wrong cmd')
            continue
        else:
            if (rcpt[(rcpt.find('@')+1):(len(rcpt)-1)] in rcpts) == False:
                rcpts.append(rcpt[(rcpt.find('@')+1):(len(rcpt)-1)])
            c.send('250 OK') #13
        rcptdone = False
        while (rcptdone == False):
            response = c.recv(1024)  #12
            if response[:8] != 'RCPT TO:':
                rcptdone = True
            else:
                if (response[(response.find('@')+1):(len(response)-1)] in rcpts) == False:
                    rcpts.append(response[(response.find('@')+1):(len(response)-1)])
                c.send('250 OK') #13
        #DATA
        if response[:4] != 'DATA': #16
            c.close()
            sys.stdout.write('Error -- wrong cmd')
            continue
        else:
            c.send('354 Start mail input; end with <CRLF>.<CRLF>') #17
        msg = c.recv(1024) #20
        c.send('250 OK') #21
        #QUIT
        if c.recv(1024) != 'QUIT': #24
            c.close()
            sys.stdout.write('Error -- wrong cmd')
            continue
        else:
            c.send('221 '+host+' closing connection') #25
            c.close()
        for rcpt1 in rcpts:
            rcpt1 = rcpt1[(rcpt1.find('@')+1):]
            f= open('forward/'+rcpt1,"a+")
            f.write(msg[:len(msg)-2])
            f.close()
        
server()
