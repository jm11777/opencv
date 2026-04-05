import cv2
import numpy as np
def apply_color_filter(image, filter_type):
    filtered_image=image.copy()
    if filter_type=='red_tint':
        filtered_image[:, :, 1]=0
        filtered_image[:, :, 0]=0
    elif filter_type=='blue_tint':
        filtered_image[:, :, 1]=0
        filtered_image[:, :, 2]=0
    elif filter_type=='green_tint':
        filtered_image[:, :, 0]=0
        filtered_image[:, :, 2]=0
    elif filter_type=='increase_red':
        filtered_image[:, :, 2]=cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type=='decrease_blue':
        filtered_image[:, :, 0]=cv2.subtract(filtered_image[:, :, 0],50)
    return filtered_image
image_path='example.jpg'
image=cv2.imread(image_path)
if image is None:
    print('Error: I,age not found!')
else:
    filter_type='original'
    print("Press the following keys to apply filters")
    print('r-Red Tint')
    print('b-Blue Tint')
    print('g-Green Tint')
    print('i=Increase Red Intensity')
    print('d-Decrease Blue Intensity')
    print('q-Quit')
    x=0
    while x==0:
        filtered_image=apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image",filtered_image)
        key=input('Enter Key: ')
        if key=='r':
            filtered_type='red_tint'
            x+=1
        elif key=='b':
            filtered_type='blue_tint'
            x+=1
        elif key=='g':
            filtered_type='green_tint'
            x+=1
        elif key=='i':
            filtered_type='increase_red'
            x+=1
        elif key=='d':
            filter_type='decrease_blue'
            x+=1
        elif key=='q':
            print('Exiting...')
            x+=1
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")
cv2.destroyAllWindows()