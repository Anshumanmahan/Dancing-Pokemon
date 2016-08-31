def pokemon():
	 non = raw_input() 
	 no = map(int,non.split(' '))
 	 na = raw_input()
 	 n = map(int, na.split(' '))
 	 if len(n) != no[0]:
 	 	print ('Invalid')
 	 	return
	 qa = raw_input()
	 q = map(int, qa.split(' '))
	 if len(q) != no[1]:
	 	print('Invalid')
	 	return
	 response = []
	 test = []
	 for i in range(len(q)):
 		 temp = 0
 		 for j in range(len(n)):
			 if q[i] == n[j]:
				 print ('YES')
				 temp = 1
				 break
	
		 if temp == 0:
			 for k in range(len(response)):
				 if q[i] == response[k]:
					 print ('YES')
					 temp = 1
					 break
			 response.append(q[i])		
		 if temp == 0:
	 		 print ('NO')
			 test.append(q[i])

test1 = int(raw_input())
while(test1 > 0):
	pokemon()
	test1 -= 1
