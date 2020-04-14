# Remove and Rebuild Node Tips While Threading   
Author : GEONHEE SIM   

pyqt5와 연계되어 Thread를 실행할 때 subscriber 노드를 생성하고, thread를 중지할 때 노드도 destroy하는 프로그램을 생각해보자.
```python
from PyQt5.QtCore import *

class rosTopicInfo(QThread):
    def __init__(self, selectedItem, sec=0, parent=None):
        QThread.__init__(self)
        self.main = parent
        self.isRun = True
        self.item = rclpy.create_node('topic')
     
    def __del__(self):
        print("Command Job Done")
        self.wait()
        
    @pyqtSlot()
    def run(self):
        if self.isRun:
            eval(str(eval(self.selectedItem[1])[0]).split('/')[-1]),
                self.selectedItem[0],
                self.sub_callback)
            rclpy.spin(self.item)
        else:
            pass

    def sub_callback(self, msg):
        myWindow.echoTopic.addItem(msg.data)
        
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.playBtn.clicked.connect(self.playTopic)
        self.stopBtn.clicked.connect(self.stopTopic) 
    
    @pyqtSlot()
    def playTopic(self):
        selectedItem = self.topicList.currentItem().text()
        self.rosTopicInfo_class = rosTopicInfo(selectedItem)
        self.rosTopicInfo_class.isRun = True
        self.rosTopicInfo_class.start()

    @pyqtSlot()
    def stopTopic(self):
        try:
            if self.rosTopicInfo_class.isRunning():
                self.rosTopicInfo_class.isRun = False
                self.rosTopicInfo_class.item.destroy_node()
                self.rosTopicInfo_class.quit()
                self.echoTopic.addItem("\nThreading is Finished")
        except:
            self.echoTopic.addItem('No topic is playing')
```
 위의 코드는 테스트 목적에 맞게 명시해야하는 부분 외에 생략되어 있다. 즉 온전한 코드가 아니다.   
pyqt5로 만든 GUI창에서 playBtn을 클릭할 때 selectedItem의 echo 값을 받아오기 위해 subscriber 노드를 생성하고, StopBtn을 클릭하면 subscriber 
노드를 삭제하고 해당 thread를 끝내는 목적의 코드를 작성하였다.   
실제로 코드를 실행하면 play를 눌렀을 때 선택한 토픽의 값이 잘 출력되고, stop을 누르면 작동을 멈춘다.   
문제는 위 상황에서 다시 play을 누를 때 발생한다.   
다음과 같은 오류가 발생하며 topic 값이 출력이 되지 않는다.
> ValueError: generator already executing "rclpy"

(오류가 발생한 이유는 지금의 나로선 정확히 규명하긴 힘들지만, 러프하게 추측하자면 
item node를 destory했지만 rclpy상에선 완전히 remove되지 않았다.
따라서 새로 생성한 노드가 동일한 이름으로 생성되어 서로 충돌이 발생하여 오류가 발생했을 것이다.)   
이와 같은 오류가 발생하지 않기 위해선 node 생성과 삭제할 각각의 경우에 `rclpy.init()`과 `rclpy.shutdown()`을 수행해주어야 한다.   
수정한 코드는 다음과 같다.
```python
from PyQt5.QtCore import *

class rosTopicInfo(QThread):
    def __init__(self, selectedItem, sec=0, parent=None):
        QThread.__init__(self)
        rclpy.init()    ### 쓰레드 실행시 rclpy 초기화, rclpy는 shutdown 되어있던 상태여야 함.
        self.main = parent
        self.isRun = True
        self.item = rclpy.create_node('topic')
     
    def __del__(self):
        print("Command Job Done")
        self.wait()
        
    @pyqtSlot()
    def run(self):
        if self.isRun:
            eval(str(eval(self.selectedItem[1])[0]).split('/')[-1]),
                self.selectedItem[0],
                self.sub_callback)
            rclpy.spin(self.item)
        else:
            pass

    def sub_callback(self, msg):
        myWindow.echoTopic.addItem(msg.data)
        
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self)
        self.playBtn.clicked.connect(self.playTopic)
        self.stopBtn.clicked.connect(self.stopTopic) 
    
    @pyqtSlot()
    def playTopic(self):
        rclpy.shutdown()   ###새로운 노드 생성 전 기존 실행중이던 rclpy를 shutdown.
        selectedItem = self.topicList.currentItem().text()
        self.rosTopicInfo_class = rosTopicInfo(selectedItem)
        self.rosTopicInfo_class.isRun = True
        self.rosTopicInfo_class.start()

    @pyqtSlot()
    def stopTopic(self):
        try:
            if self.rosTopicInfo_class.isRunning():
                self.rosTopicInfo_class.isRun = False
                self.rosTopicInfo_class.item.destroy_node()
                self.rosTopicInfo_class.quit()
                self.echoTopic.addItem("\nThreading is Finished")
        except:
            self.echoTopic.addItem('No topic is playing')
```
