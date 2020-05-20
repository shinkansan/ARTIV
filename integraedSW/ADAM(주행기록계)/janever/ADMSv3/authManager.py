from filestack import Client
from filestack import Filelink


class authentication_server():
	def __init__(self):
		self.client = Client('AJD6nNwZORdSkQOAkpN7Mz')

	def new(self, filepath_org):
		new_filelink = self.client.upload(filepath = filepath_org )
		self.FileID = new_filelink.url.split('/')[-1]
		return self.FileID

	def __str__(self):
		if self.FileID:
			return self.FileID
		else:
			raise Exception("No Upload Action")

	#test id GB3aPVArRzGQRTjePq0w
	def update(self, fileID):
		Filelink(str(fileID)).download('./adms_user_db.npz')


	def image(self, buffer):
		decoded = cv2.imdecode(np.frombuffer(buffer, np.uint8), -1)
		cv2.imshow("test", decoded)
		cv2.waitKey(0)