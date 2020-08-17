import re 
keyword = ['auto','double','int','struct',
'break','else','long','switch'
,'case','enum','register','typedef',
'char','extern','return','union',
'continue','for','signed','void'
,'do','if','static','while'
,'default','goto','sizeof','volatile',
'const','float','short','unsigned']

operator = ['+','-','*','/','%',
 '=','+=','*=','/=','%=',
'==','<=','>=','!=','<','>',
 '&&','||','!',
 '&','|','^','<<','>>','~',
 ',','++','--'
 ]
 
separator = ['{','}']

r1 = '^[A-Za-z_]+'

l1 = []
key=[]
ope=[]
sep=[]
ide=[]
q=[]
p=[]
r=[]

def check(b):
    if (b in keyword):
        key.append(b)

    elif(b in operator):
        ope.append(b)

    elif(b in separator):
        sep.append(b)
    
    elif(b in re.findall(r1,b)):
        ide.append(b)
        
    
def david(code):
    for j in code:
        if j not in (' ','\t','\n'):
            p.append(j)
        else:
            c = "".join(p)
            p.clear()
            r.append(c)
        

file = open("c.txt", "r")
for line in file.readlines():
    line = re.sub('//[A-Za-z0-9 ]*','',line)
    print(line)
    david(line)

for i in r:
    check(i)
print("Keyword is",list(dict.fromkeys(key)))
print("Operator is",list(dict.fromkeys(ope)))
print("Separator is",list(dict.fromkeys(sep)))
print("Identifier is",list(dict.fromkeys(ide)))

for i in key:
    print()




'''
        
    
    
    
 elif j=='\t':
            c = "".join(p)
            #print(p)
            p.clear()
            r.append(c)
        elif j=='\n':
            c = "".join(p)
            #print(p)
            p.clear()
            r.append(c)
        
    
    
    
    
    
    
    
    
    
        
    elif(i in operator):
        ope.append(i)
        l1.clear()
        
        
    elif(i in separator):
        sep.append(i)
        l1.clear()
        

    
    else:     
        l1.append(i)
    a = "".join(l1)
    
    
key.append(a)
for i in key:
    if i=='':
      key.remove(i)
print('Keyword is',key)
print('Operator is',ope)
print('Separator is ',sep)

txt= "gf1231 = 30"   
d = re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', key)
print(d.group())







'''

