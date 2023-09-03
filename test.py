from python_imagesearch.imagesearch import imagesearch
def quickImageSearch():
    pos = imagesearch("./imagesamples/apple_158989157.jpg")
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")

    
if __name__ == "__main__":
    quickImageSearch()
    pass