# Image Recognition research

Libraries used are based on this [article](https://brokencode.io/how-to-easily-image-search-with-python/)

Things I found while trying to test whether an image is recognised
- Screen resolution and image size (in pixels) does affect whether an image is on screen
- The current library does not support finding what is the width and height of the image that is found in the page, hense will need to use OpenCV for this function
    - However, this needs to be paired with PyAutoGui to screenshot the screen to use as reference as OpenCV only supports local files 