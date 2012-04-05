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

ri=0
defMsgs = 'no message'
defComments = 'no comments'
defFrom = 'nowhere'
defData = 'no data'

if sys.argv[1] == 'p':
  status = fbconsole.post("/me/feed", {"message":sys.argv[2]})
elif sys.argv[1] == 'r':
  for post in fbconsole.iter_pages(fbconsole.get('/me/home')):
    print ''
    dedented_text = textwrap.dedent(post.get('message',defMsgs)).strip()
    print textwrap.fill(dedented_text,width=40, initial_indent=' '+post.get('from',defMsgs).get('name',defMsgs)+":", subsequent_indent='    ')
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
    if ri == int(sys.argv[2]):
      break
      