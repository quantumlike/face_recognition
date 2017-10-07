from os import path
# import sys
# import numpy
import datetime
from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image_path = "./face_recognization/xiaomei_1.jpg"
print(image_path)
print(path.basename(image_path))
print(path.abspath(image_path))
print(path.dirname(path.abspath(image_path)))
print(path.splitext(path.basename(image_path))[0])
print(path.splitext(path.basename(image_path))[1])
image_rootname = path.splitext(path.basename(image_path))[0]
image = face_recognition.load_image_file(image_path)

print('%(image)s' % vars())
# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    find_face_image_file_name = '%(image_rootname)s_%(timestamp)s.jpg' % vars()
    print(find_face_image_file_name)
    pil_image.save('%(find_face_image_file_name)s' % vars())
    # pil_image.save('test_%(timestamp)s.jpg' % vars())