import sys

#remote/destination smtp server -> stderr echoes stdin
def remoteserver(self):
    try:
        response = raw_input()
    except EOFError:
        sys.stdout.write('QUIT\n')
        sys.exit()
    if (self == 'mail' or self == 'done' or self == 'rcpt') and len(response)>3 and (response[0:3] == '250') and response[3].isspace():
        sys.stderr.write(response+'\n')
    elif self == 'data' and len(response)>3 and (response[0:3] == '354') and response[3].isspace():
        sys.stderr.write(response+'\n')
    else:
        sys.stderr.write(response+'\n')
        sys.stdout.write('QUIT\n')
        sys.exit()

def localserver():
    try:
        f = open(sys.argv[1],"r")
        lines = f.read().splitlines()
        #lines = open('jeffay@cs.unc.edu', 'r').read().splitlines()
    except:
        sys.exit()
    #lines = open('jeffay@cs.unc.edu', 'r').read().splitlines()
        
    data = False
    #print len(lines)
    while len(lines) > 0:
        line = lines[0]
        if line[0:5] == 'From:':
            #print 'just a from'
            sys.stdout.write('MAIL FROM: '+ line[6:]+'\n')
            remoteserver('mail')
            del lines[0]
        elif line[0:3] == 'To:':
            #print 'just a to'
            sys.stdout.write('RCPT TO: '+ line[4:]+'\n')
            remoteserver('rcpt')
            #print lines.index(line)
            #print len(lines)-1
            if lines.index(line) == len(lines)-1: #if msg line is the last line of the file
                #print 'msg is last line'
                sys.stdout.write('DATA\n')
                remoteserver('data')
                sys.stdout.write('.\n')
                remoteserver('done')
            if (lines.index(line)+1) < len(lines) and (lines[lines.index(line)+1])[0:5] == 'From:': #next line = From:
                #print 'to->from'
                sys.stdout.write('DATA\n')
                remoteserver('data')
                sys.stdout.write('.\n')
                remoteserver('done')
            del lines[0]
        elif (lines.index(line)+1) < len(lines) and (lines[lines.index(line)+1])[0:5] == 'From:': #msg w/ next line = From:
            #print 'msg->from'
            if data == False:
                sys.stdout.write('DATA\n')
                data = True #print DATA before the first line of msg
                remoteserver('data')
            sys.stdout.write(line+'\n')
            sys.stdout.write('.\n')
            remoteserver('done')
            data = False #resets data for next msg
            del lines[0]
        else: #msg w/o next line = From:
            #print 'msg->msg'
            if data == False:
                sys.stdout.write('DATA\n')
                data = True #print DATA before the first line of msg
                remoteserver('data')
            sys.stdout.write(line+'\n')
            if lines.index(line) == len(lines)-1: #if msg line is the last line of the file
            #if len(lines) == 1:
                #print 'msg is last'
                sys.stdout.write('.\n')
                remoteserver('done')
            del lines[0]
    sys.stdout.write('QUIT\n')
    sys.exit()

localserver()
        
