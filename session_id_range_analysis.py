import sys, requests
r = requests.get('http://pentesteracademylab.appspot.com/lab/webapp/sid/2')
id = []
count = 1

def sendRequest():
   global count
   count+=1
   global r
   sess_id = r.headers['set-cookie']
   sess_id = sess_id.split("=")[1]
   cookie = {'sessionid':str(sess_id)}
   r = requests.get('http://pentesteracademylab.appspot.com/lab/webapp/sid/2', cookies=cookie)
   return sess_id

try:
   while True:
      id.append(sendRequest())
      sys.stdout.write("Requests sent: %d :: min: %s :: max: %s\r" % (count, min(id), max(id)) )
      sys.stdout.flush()
      # print min(id)
      # print max(id)
except KeyboardInterrupt:
   # pass
   print("\nmin: %s :: max: %s" % (min(id), max(id)))
   # sys.stdout.write("\nmin: %s :: max: %s\n" % (min(id), max(id)))
   # sys.stdout.flush()
