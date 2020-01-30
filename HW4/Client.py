import socket
import sys
def checkfrom():
    while(1):
        sys.stdout.write('From:\n')
        try:
            email = raw_input()
        except EOFError:
            sys.exit()
            break
        charlist = list(email)
        filename = ''
        sender = ''
        if charlist[0] == '@':
            print '501 Syntax error in parameters or arguments'
            continue
        while charlist[0] != ' ' and charlist[0] != '	' and charlist[0] != '<' and charlist[0] != '>' and charlist[0] != '(' and charlist[0] != ')' and charlist[0] != '[' and charlist[0] != ']' and charlist[0] != '\\' and charlist[0] != '.' and charlist[0] != ',' and charlist[0] != ';' and charlist[0] != ':' and charlist[0] != '@' and charlist[0] != '"':
            sender = sender + charlist[0]
            del charlist[0]
            if len(charlist) == 0:
                break
        if len(charlist) == 0:
            print '501 Syntax error in parameters or arguments'
            continue
        if charlist[0] == ' ' or charlist[0] == '	' or charlist[0] == '<' or charlist[0] == '>' or charlist[0] == '(' or charlist[0] == ')' or charlist[0] == '[' or charlist[0] == ']' or charlist[0] == '\\' or charlist[0] == '.' or charlist[0] == ',' or charlist[0] == ';' or charlist[0] == ':' or charlist[0] == '"':
            print '501 Syntax error in parameters or arguments'
            continue
        if charlist[0] == '@':
            sender = sender + charlist[0]
            del charlist[0]
            if len(charlist) == 0:
                print '501 Syntax error in parameters or arguments'
                continue
        if charlist[0].isalpha() == False and charlist[0].isdigit() == False:
            print '501 Syntax error in parameters or arguments'
            continue
        #check After '@'; confirmed that list is not empty!
        endswithdot = False
        wrongchar = False
        nofirstletter = False
        while len(charlist) != 0:
            #checks that first char is a letter
            if charlist[0].isalpha():
                #checks for following chars that are letters or numbers while list is NOT empty
                while len(charlist) != 0 and charlist[0] != '.':
                    #if not a letter or number
                    if charlist[0].isdigit() == False and charlist[0].isalpha() == False:
                        wrongchar = True
                        break
                    else:
                        sender = sender + charlist[0]
                        filename = filename + charlist[0]
                        del charlist[0]
                if wrongchar == True:
                    break
                if len(charlist) == 0:
                    break
                if charlist[0] == '.':
                    sender = sender + charlist[0]
                    filename = filename + charlist[0]
                    del charlist[0]
                    if len(charlist) == 0:
                        endswithdot = True
                        break
                    continue
            else:
                nofirstletter = True
                break
        if wrongchar == True or endswithdot == True or nofirstletter == True:
            print '501 Syntax error in parameters or arguments'
            continue
        if len(charlist) == 0:
            return sender, filename
            break
        if charlist[0] != ' ' and charlist[0] != '	':
            print '501 Syntax error in parameters or arguments'
            continue
        while (charlist[0] == ' ' or charlist[0] == '	'):
            del charlist[0]
            if len(charlist) == 0:
                break
        if len(charlist) == 0:
            return sender, filename
            break
        else:
            print '501 Syntax error in parameters or arguments'
            continue
def checkto():
    while 1:
        sys.stdout.write('To:\n')
        try:
            recipients = raw_input()
        except EOFError:
            sys.exit()
            break
        rcpts = []
        charlist = list(recipients)
        wrong = False
        if len(recipients) == 0:
            print '501 Syntax error in parameters or arguments'
            continue
        while len(charlist) != 0:
            if (',' in charlist) == False: #OPTION 1
                rcpt = [] #rcpt before next comma
                while len(charlist) != 0: #get rcpt
                    rcpt.append(charlist[0])
                    del charlist[0]
                recipient = ''.join(rcpt)
                
                if rcpt[0] == '@':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                while rcpt[0] != ' ' and rcpt[0] != '	' and rcpt[0] != '<' and rcpt[0] != '>' and rcpt[0] != '(' and rcpt[0] != ')' and rcpt[0] != '[' and rcpt[0] != ']' and rcpt[0] != '\\' and rcpt[0] != '.' and rcpt[0] != ',' and rcpt[0] != ';' and rcpt[0] != ':' and rcpt[0] != '@' and rcpt[0] != '"':
                    del rcpt[0]
                    if len(rcpt) == 0:
                        break
                if len(rcpt) == 0:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if rcpt[0] == ' ' and rcpt[0] == '	' and rcpt[0] == '<' and rcpt[0] == '>' and rcpt[0] == '(' and rcpt[0] == ')' and rcpt[0] == '[' and rcpt[0] == ']' and rcpt[0] == '\\' and rcpt[0] == '.' and rcpt[0] == ',' and rcpt[0] == ';' and rcpt[0] == ':' and rcpt[0] == '@' and rcpt[0] == '"':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if rcpt[0] == '@':
                    del rcpt[0]
                    if len(rcpt) == 0:
                        print '501 Syntax error in parameters or arguments'
                        wrong = True
                        break
                if rcpt[0].isalpha() == False and rcpt[0].isdigit() == False:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                #check After '@'; confirmed that list is not empty!
                endswithdot = False
                wrongchar = False
                nofirstletter = False
                while len(rcpt) != 0:
                    #checks that first char is a letter
                    if rcpt[0].isalpha():
                        #checks for following chars that are letters or numbers while list is NOT empty
                        while len(rcpt) != 0 and rcpt[0] != '.':
                            #if not a letter or number
                            if rcpt[0].isdigit() == False and rcpt[0].isalpha() == False:
                                wrongchar = True
                                break
                            else:
                                del rcpt[0]
                        if wrongchar == True:
                            break
                        if len(rcpt) == 0:
                            break
                        if rcpt[0] == '.':
                            del rcpt[0]
                            if len(rcpt) == 0:
                                endswithdot = True
                                break
                            continue
                    else:
                        nofirstletter = True
                        break
                if wrongchar == True or endswithdot == True or nofirstletter == True:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if len(rcpt) == 0:
                    rcpts.append(recipient)
                    break
                if rcpt[0] != ' ' and rcpt[0] != '	':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                while (rcpt[0] == ' ' or rcpt[0] == '	'):
                    del rcpt[0]
                    if len(rcpt) == 0:
                        break
                if len(rcpt) == 0:
                    rcpts.append(recipient)
                    break
                else:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
            else: #OPTION 2
                rcpt = [] #rcpt before next comma
                while charlist[0] != ',': #get rcpt
                    rcpt.append(charlist[0])
                    del charlist[0]
                recipient = ''.join(rcpt)
                
                del charlist[0] #del comma
                if len(charlist) == 0: #error if no email after comma
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                while charlist[0].isspace(): #del white space
                    del charlist[0]
                    if len(charlist) == 0:
                        break
                if len(charlist) == 0: #error if no email after comma
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                
                #parse rcpt, append to rcpts; if error: wrong = True, break
                if rcpt[0] == '@':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                while rcpt[0] != ' ' and rcpt[0] != '	' and rcpt[0] != '<' and rcpt[0] != '>' and rcpt[0] != '(' and rcpt[0] != ')' and rcpt[0] != '[' and rcpt[0] != ']' and rcpt[0] != '\\' and rcpt[0] != '.' and rcpt[0] != ',' and rcpt[0] != ';' and rcpt[0] != ':' and rcpt[0] != '@' and rcpt[0] != '"':
                    del rcpt[0]
                    if len(rcpt) == 0:
                        break
                if len(rcpt) == 0:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if rcpt[0] == ' ' and rcpt[0] == '	' and rcpt[0] == '<' and rcpt[0] == '>' and rcpt[0] == '(' and rcpt[0] == ')' and rcpt[0] == '[' and rcpt[0] == ']' and rcpt[0] == '\\' and rcpt[0] == '.' and rcpt[0] == ',' and rcpt[0] == ';' and rcpt[0] == ':' and rcpt[0] == '@' and rcpt[0] == '"':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if rcpt[0] == '@':
                    del rcpt[0]
                    if len(rcpt) == 0:
                        print '501 Syntax error in parameters or arguments'
                        wrong = True
                        break
                if rcpt[0].isalpha() == False and rcpt[0].isdigit() == False:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                #check After '@'; confirmed that list is not empty!
                endswithdot = False
                wrongchar = False
                nofirstletter = False
                while len(rcpt) != 0:
                    #checks that first char is a letter
                    if rcpt[0].isalpha():
                        #checks for following chars that are letters or numbers while list is NOT empty
                        while len(rcpt) != 0 and rcpt[0] != '.':
                            #if not a letter or number
                            if rcpt[0].isdigit() == False and rcpt[0].isalpha() == False:
                                wrongchar = True
                                break
                            else:
                                del rcpt[0]
                        if wrongchar == True:
                            break
                        if len(rcpt) == 0:
                            break
                        if rcpt[0] == '.':
                            del rcpt[0]
                            if len(rcpt) == 0:
                                endswithdot = True
                                break
                            continue
                    else:
                        nofirstletter = True
                        break
                if wrongchar == True or endswithdot == True or nofirstletter == True:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                if len(rcpt) == 0:
                    rcpts.append(recipient)
                    continue
                if rcpt[0] != ' ' and rcpt[0] != '	':
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
                while (rcpt[0] == ' ' or rcpt[0] == '	'):
                    del rcpt[0]
                    if len(rcpt) == 0:
                        break
                if len(rcpt) == 0:
                    rcpts.append(recipient)
                    continue
                else:
                    print '501 Syntax error in parameters or arguments'
                    wrong = True
                    break
            if wrong == True:
                break
            else:
                continue 
        if wrong == True:
            continue
        else:
            return rcpts
            break
def checksubject():
    sys.stdout.write('Subject:\n')
    try:
        subject = raw_input()
    except EOFError:
        sys.exit()
    return subject
def checkmsg():
    sys.stdout.write('Message:\n')
    message = ''
    while 1<2:
        try:
            msg = raw_input()
        except EOFError:
            sys.exit()
        if (msg == '.'):
            break
        else:
            message = message+msg+'\n'
    return message
def promptemail():
    data = ''
    sender, domainname = checkfrom()#from:
    data = 'From: <'+sender+'>\n'
    rcpts = checkto()#to:
    data=data+'To: '
    i = 0
    while i<len(rcpts):
        if i == len(rcpts)-1:
            data = data+'<'+rcpts[i]+'>\n'
        else:
            data=data+'<'+rcpts[i]+'>, '
        i = i+1
    subject = checksubject()#subject:
    data=data+'Subject: '+subject+'\n'
    msg = checkmsg()#msg:
    data=data+'\n'+msg
    sender = '<'+sender+'>'
    rcpts = ['<'+rcpt+'>' for rcpt in rcpts]
    return sender, rcpts, msg, data
def client():
    sender, rcpts, msg, data = promptemail()
    s = socket.socket()
    client = sys.argv[1] #socket.gethostname()
    port = sys.argv[2]
    try:
        s.connect((client, port))
    except:
        sys.stdout.write('Error -- cannot connect')
        s.close()
        sys.exit()
    #3-way handshake
    if s.recv(1024)[:3] != '220': #2
        sys.stdout.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    s.send('HELO '+client+' pleased to meet you\n') #3
    if s.recv(1024)[:3] != '250': #6
        sys.stdout.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    #MAIL FROM 
    s.send('MAIL FROM: '+sender) #7
    if s.recv(1024)[:3] != '250': #10
        sys.stdout.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    #RCPT TO
    for rcpt in rcpts: 
        s.send('RCPT TO: '+rcpt) #11
        if s.recv(1024)[:3] != '250': #14
            sys.stdout.write('Error -- wrong cmd')
            s.close()
            sys.exit()
    #DATA
    s.send('DATA') #15
    if s.recv(1024)[:3] != '354': #18
        sys.stdout.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    s.send(data+'.\n') #19 s.send('.')
    if s.recv(1024)[:3] != '250': #22
        sys.stdout.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    #QUIT
    s.send('QUIT') #23
    if s.recv(1024)[:3] != '221': #26
        sys.stdin.write('Error -- wrong cmd')
        s.close()
        sys.exit()
    else:
        s.close()
        sys.exit()

#print socket.getfqdn() #-->use for host = socket.gethostbyname(socket.gethostname())
#promptemail()
client()
