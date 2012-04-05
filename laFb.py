from __future__ import unicode_literals
#from urllib import urlretrieve
#import imp
import sys
import fbconsole
import unicodedata
import textwrap


#urlretrieve('https://raw.github.com/facebook/fbconsole/master/src/fbconsole.py', '.fbconsole.py')
#fb = imp.load_source('fb', '.fbconsole.py')
fbconsole.AUTH_SCOPE = ['publish_stream','publish_checkins','read_stream']
fbconsole.authenticate()

CODE={
    'ENDC':0,  # RESET COLOR
    'BOLD':1,
    'UNDERLINE':4,
    'BLINK':5,
    'INVERT':7,
    'CONCEALD':8,
    'STRIKE':9,
    'GREY30':90,
    'GREY40':2,
    'GREY65':37,
    'GREY70':97,
    'GREY20_BG':40,
    'GREY33_BG':100,
    'GREY80_BG':47,
    'GREY93_BG':107,
    'DARK_RED':31,
    'RED':91,
    'RED_BG':41,
    'LIGHT_RED_BG':101,
    'DARK_YELLOW':33,
    'YELLOW':93,
    'YELLOW_BG':43,
    'LIGHT_YELLOW_BG':103,
    'DARK_BLUE':34,
    'BLUE':94,
    'BLUE_BG':44,
    'LIGHT_BLUE_BG':104,
    'DARK_MAGENTA':35,
    'PURPLE':95,
    'MAGENTA_BG':45,
    'LIGHT_PURPLE_BG':105,
    'DARK_CYAN':36,
    'AUQA':96,
    'CYAN_BG':46,
    'LIGHT_AUQA_BG':106,
    'DARK_GREEN':32,
    'GREEN':92,
    'GREEN_BG':42,
    'LIGHT_GREEN_BG':102,
    'BLACK':30,
}

def termcode(num):
    return '\033[%sm'%num

def colorstr(astr,color):
    return termcode(CODE[color])+astr+termcode(CODE['ENDC'])


ri=0
rMax=10
defMsgs = 'no message'
defComments = 'no comments'
defFrom = 'nowhere'
defData = 'no data'
subFolder = "home"



if len(sys.argv) == 1:
  print "laFb.py <option> <para1> <para2...>"
  print "<option> <para1> <para2> | describe"
  print "p        message         | update your fb status"
  print "r        counts          | read counts from your fb home page"
  exit()

#==== input control ====
if len(sys.argv) >= 3:
  if len(sys.argv[2]) == 0:
    rMax = 10
  else:
    rMax = int(sys.argv[2])

if len(sys.argv) >= 4:
  if len(sys.argv[3]) == 0:
    subFolder="home"
  elif sys.argv[3] == 'h':
    subFolder="home"
  elif sys.argv[3] == 'm':
    subFolder="feed"
  else:
    subFolder="home"
#==== input control ====

if sys.argv[1] == 'p':
  status = fbconsole.post("/me/feed", {"message":sys.argv[2]})
elif sys.argv[1] == 'r':



  for post in fbconsole.iter_pages(fbconsole.get('/me/'+subFolder)):
    print ''
    dedented_text = textwrap.dedent(post.get('message',defMsgs)).strip()
    print colorstr(textwrap.fill(dedented_text,width=40, initial_indent=' '+post.get('from',defMsgs).get('name',defMsgs)+":", subsequent_indent='    '),'YELLOW')
    #print post.get('comments',defComments)
    #print len(post.get('comments',defComments))
    #print post.get('comments',defComments)
    if post.get('comments',defComments).get('count',defMsgs) != 0:
      #print type(post.get('comments',defComments))
      for reply in post.get('comments',defComments).get('data',defMsgs):
        #print type(reply)
        if type(reply) != unicode:
          dedented_textC = textwrap.dedent(reply.get('message',defMsgs))
          print textwrap.fill(dedented_textC,width=40, initial_indent=' >'+reply.get('from',defMsgs).get('name',defMsgs)+":", subsequent_indent='    ')
    #for comments in post.get('comments',defComments):
    #  print comments.get('id',defFrom)
    
    ri+=1
    if ri == rMax:
      break
      