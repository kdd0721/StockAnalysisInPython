import matplotlib.pyplot as plt
import matplotlib.image as mping

dst_img = mping.imread('dst.png')
pseudo_img = dst_img[:, :, 0]

plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mping.imread('src.png'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mping.imread('dst.png')
plt.imshow(pseudo_img)
plt.show()