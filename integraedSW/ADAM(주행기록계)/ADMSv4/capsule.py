#Capsule Maker

import numpy as np
import hashlib
import pprint
'''
capsule manage for ARTIV Team Manager



'''
class capsule():
	def __init__(self, db=None):
		self.Policy = {'superuser' : 255, 'admin' : 1, 'guest' : 2, 'user' : 3, 'nonlocal' : 4}
		self.db = db if db else {}
		self._security = {'hashtype' : 'sha256', 'compresstype' : 'none' }


	def security(self, param=None):
	# Security Settings
	# Params:
	#	hashtype : 'sha256' etc. hashlib support part
	#   compresstype : image compress type
		if param :
			self._security.update(param)

	def encode(self, passwords):
		return hashlib.sha256(str(passwords).encode('utf-8')).hexdigest()

	def img_compress(self):
		pass


	def add(self, name, sid, passwords='guest', image='default', policy='user'):
		ppolicy = self.Policy.get(policy, 3)
		self.db.update({sid : [
			name,
			self.encode(passwords),
			image,
			sid,
			ppolicy]})

	def getCapsule(self):
		return self.db

	def retrieve(self, sid, params=all):
		authDict = self.getCapsule()

		data = authDict.get(sid)
		if not data:
			return -1;
		returnData = []
		if params=="all" : params=["name","password","image","sid","policy"]

		for param in params:
			if param == "name":
				returnData.append(data[0])
			if param == "password":
				returnData.append(data[1])
			if param == "image":
				returnData.append(data[2])
			if param == "sid":
				returnData.append(data[3])
			if param == "policy":
				returnData.append(data[4])

		return returnData

	def passValidation(self, sid, cmp2):
		cmp2_hash = self.encode(cmp2)
		cmp1 = self.retrieve(sid, ["password"])[0]
		return cmp2_hash == cmp1

	def idValidation(self, sid):
		for data in self.db:
			cmp_sid = data[-3:]
			#print(cmp_sid, sid)
			if sid == cmp_sid:
				return data
			else:
				return 0




if __name__ == '__main__':
	testdb = capsule()
	testdb.add('gwanjunshin', 201811093, 'kansan', [123,123,123], 'superuser')

	db = testdb.getCapusle()
	pprint.pprint(db)
	test2db = capsule(db)
	test2db.add('geonhee', 201811097, 'gunimon', [123,123,123])
	pprint.pprint(test2db.getCapusle())
