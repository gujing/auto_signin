import cv2
from matplotlib import pyplot as plt

img = cv2.imread('screen.png', 0)
img2 = img.copy()
template = cv2.imread('temp.png', 0)
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


img = img2.copy()
method = cv2.TM_CCOEFF

# Apply template Matching
res = cv2.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

print(top_left)
print(bottom_right)
print((top_left[0] + bottom_right[0])/2, (top_left[1] + bottom_right[1])/2)
cv2.rectangle(img, top_left, bottom_right, 255, 2)
cv2.imwrite('new_screen.jpg',img)

# plt.subplot(121), plt.imshow(res, cmap='gray')
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img, cmap='gray')
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle('cv2.TM_CCOEFF')
#
# plt.show()
