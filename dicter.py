values = []
keys = []


ok = "<'hello':"", 'ok':"", 'z':'2'>"
def syntax_cheacker(dicter_str):
    ok1 = ok.replace(">","").replace("<","")
    firstlist = ok1.split(",")
    sectlist = [x.strip() for x in firstlist]

    check_on = 0
    check_i = 0
    for c in ok:
        if c == ':' and check_on == False:
            check_on = True
            check_i += 1
            
        if check_on == True and (c == " "):
            continue
            
        if check_on == True and check_i>0:
             
            if c.isnumeric():                
                check_on = False
                check_i = 0
                print("valid integer")
            else:
                if ord(c) == ord("'") or ord(c)  == ord('"'):
                    if check_i == 1:
                        check_i = 2
                    else:
                        check_on = False
                        check_i = 0
                        print("valid str")

       
    for i in sectlist:
        if ":" not in i:
            print("syntax error: invalid dicter format")
        if len(i.split(":")) != 2:
            print("syntax error: invalid dicter, dicter must contains key:value pairs")
    print(sectlist)
syntax_cheacker(ok)


class dicter():
    keys = []
    values = []
    dicter = ''
    def __init__(self,dicter):
         dicter = dicter.replace(">","").replace(">","")
         data = dicter.split(",")
    def get(key):
         return self.values[self.keys.index('hello')]
    
# print(values[keys.index('hello')])
