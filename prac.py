import os
if os.path.exists("first.html"):
    print("Exists")
    f=open("first.html","a")
    s='''
<script> 
alert("Testing")
<script>'''
    f.write(s)
    f.close()
    f=open("first.html","r")
    for x in f:
        print(f.readline())
    f.close()
else:
    print("NOpe")
