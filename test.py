from python_imagesearch.imagesearch import imagesearch


def quickImageSearch():
    pos = imagesearch("./imagesamples/video.png")
    if pos[0] != -1:
        # prints out the x,y coordinate positions of the image
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")



    
if __name__ == "__main__":
    quickImageSearch()
    pass