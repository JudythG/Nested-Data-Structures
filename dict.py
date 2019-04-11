# Assignment
# Design a dictionary whose keys describe what values you'd like to learn 
#   about your peers in this class. Design the dictionary on paper, specifying 
#   the data type of the value. You must store at least one of each of our 
#   review types.
# Once the specification is done, pass the dictionary design to a peer, and 
#   ask them to populate the dictionary values with appropriate syntax.
# Now, at a computer, create a simple program which creates this dictionary, 
#   whose keys are all strings, and hard-code the values from yet a third 
#   person's dictionary.
# Create a simple mechanism for retrieving the value of one of the keys in the a
#   dictionary using user input.
# Prepare to demonstrate your program to your peers.

# idea to use classes from article "Unifying types and classes in Python 2.2"
# html: https://www.python.org/download/releases/2.2/descrintro/#cooperation

import io

class mystr():
    s = ''

    def getinputfromuser (self, p):
        print (p)
        #self.s = raw_input()
        self.s = input()

    def getdata (self): return self.s

# for now, assume list of strings
class mylist():
    l = []

    def getinputfromuser (self, p):
        prompt = 'Enter ' + p + " or q to quit"
        response = ""
        s = mystr()
        while True:
            s.getinputfromuser (prompt)
            response = s.getdata()
            if response == 'q':
                break
            self.l.append (response)

    def getdata (self): return self.l

class mytuple():
    t = ()

    def getinputfromuser (self, p):
        prompt = 'Enter ' + p + " or q to quit"
        response = ""
        s = mystr()
        while True:
            s.getinputfromuser (prompt)
            response = s.getdata()
            if response == 'q':
                break
            t1 = (response,)
            self.t = self.t + t1

    def getdata (self): return self.t

class mydate():
    date = {'month': mystr(), 'day': mystr(), 'year': mystr()}
    date_name = ''

    def getinputfromuser (self, dummy):
         prompt = 'for ' + self.date_name + ' enter ' 

         year= mystr()
         year_prompt = prompt + 'enter year'
         year.getinputfromuser (year_prompt)

         month = mystr()
         month_prompt = prompt + 'enter month'
         month.getinputfromuser (month_prompt)

         day= mystr()
         day_prompt = prompt + 'enter day'
         day.getinputfromuser (day_prompt)
 
         self.date['month'] = month
         self.date['year'] = year
         self.date['day'] = day

    def getdata (self):
        retString = self.date['day'].getdata() + ' ' 
        retString = retString + self.date['month'].getdata() + ' ' 
        retString = retString + self.date['year'].getdata()
        return retString

    def __init__(self, name):
        self.date_name = name

def test_str():
    s = mystr()
    s.getinputfromuser ("Please enter your best friend's name")
    data = s.getdata()
    print ("Your best friend is " + data)

def test_list():
    l = mylist()
    l.getinputfromuser("enter string")
    print (l.getdata())

def test_tuple():
    t = mytuple()
    t.getinputfromuser("enter string")
    print (t.getdata())

# input: a dict object
def getinputfromuser (d):
    for k,v in d.items():
        if type(d[k]) is dict:
            d[k] = getinputfromuser (d[k])
        else:
            d[k].getinputfromuser (k)
            d[k] = d[k].getdata()
    print ()
    return d

def test_dict():
    start_date = mydate('start date')
    end_date = mydate('end date')

    date_range = {'start date':start_date, 'end date':end_date}

    vacay_info = {'vacation_spot':mystr(), 'travel_date':date_range}
    peer_info = {'fav_kid_books':mytuple() , 
	'hobbies': mylist() ,
	"best friend's name": mystr() ,
	'travel': vacay_info }
    peer_info = getinputfromuser(peer_info)
    print (peer_info)

# main
test_dict()

