How to use simpleLane
==========

Usage
------
```python
import line_fit_video as lf 

"""
def annotate_image(input)

@param
input : numpy ndarray

output : numpy ndarray

@description
input the image with lane and annotate it by only CPU power


"""


vis = lf.annotate_image(image : np.ndarray)
cv2.imshow('test', vis)
cv2.waitKey(0)
```
