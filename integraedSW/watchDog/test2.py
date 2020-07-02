import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M
from PyQt5.QtMultimedia import *
import sys
import os
app=C.QCoreApplication(sys.argv)


playlist = QMediaPlaylist()
url = C.QUrl.fromLocalFile(os.path.join(os.getcwd(), "./warning2.mp3"))
playlist.addMedia(QMediaContent(url))
playlist.setPlaybackMode(QMediaPlaylist.Loop)

player = QMediaPlayer()
player.setPlaylist(playlist)
player.play()
app.exec()
