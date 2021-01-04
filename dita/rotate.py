import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os

def plot(t,s):
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='height', ylabel='percentile',
           title='find line')
    ax.grid()
    plt.show()

def main():
    img_name = os.path.join(os.path.dirname(__file__), 'data/200940463.jpg')
    img = cv2.imread(img_name)
    print(type(img))
    print(img.shape)

    height = img.shape[0]
    per = np.percentile(img, 80, [1, 2])
    t = range(height)
    #plot(t, per)
    print(np.percentile(per, 91))
    print(np.percentile(per, 92))
    print(np.percentile(per, 96))
    print(np.percentile(per, 97))
    print(np.percentile(per, 98))

    thres = np.percentile(per, 90)
    print("thres " + str(thres))
    margin = per > thres
    diff = np.diff(margin)
    print(diff.shape)
    cut_off = np.where(diff!=0)[0]
    print(cut_off)

    mids = []
    for i in range(len(cut_off)):
        if i%2 == 1:
            continue
        mid = (cut_off[i] + cut_off[i+1])//2
        mids.append(mid)
        img[mid][:][:] = 0

    for i in range(len(mids)-1):
        upper_line = mids[i]
        lower_line = mids[i+1]
        upper_weight = 0.5
        lower_weight = 1 - upper_weight
        cut = int(upper_line * upper_weight + lower_line * lower_weight)
        img[cut][:][:] = 0

    cv2.imwrite("test.jpg",img)



if __name__ == '__main__':
    main()
