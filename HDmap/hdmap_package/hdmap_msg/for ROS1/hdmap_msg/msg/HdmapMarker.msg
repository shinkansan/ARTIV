uint8 PERSON=0
uint8 CENTERLANE=1
uint8 CURB=2
uint8 WHITELINE=3
uint8 DASHEDLINE=4
uint8 GUIDELINE=5
uint8 TRAFFICLIGHT = 6
uint8 TRAFFICSIGN = 7
uint8 CROSS=8
uint8 CCTV=9
uint8 STOPLINE=10
uint8 BUMP=11
uint8 AREA = 12

# Default ADD
uint8 ADD=0
uint8 MODIFY=0
uint8 DELETE=2
uint8 DELETEALL=3

			# Update marker if MODIFY is set


std_msgs/Header header
string ns
int32 id

int32 type
int32 action

geometry_msgs/Pose pose
geometry_msgs/Vector3 scale

# If want to set specific color of element
std_msgs/ColorRGBA color

# LINEs or MultiLine
geometry_msgs/Point[] points
std_msgs/ColorRGBA[] colors

string text
