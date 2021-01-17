import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os
import sys


def plot(t, s):
    return
    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='height', ylabel='percentile',
           title='find line')
    ax.grid()
    plt.show()


def main():
    #img_name = os.path.join(os.path.dirname(__file__), 'data/200940463.jpg')
    img_name = input_fn
    img = cv2.imread(img_name)
    print(img.shape)

    height = img.shape[0]
    per = np.percentile(img, 80, [1, 2])
    t = range(height)
    plot(t, per)
    print(np.percentile(per, 91))
    print(np.percentile(per, 92))
    print(np.percentile(per, 96))
    print(np.percentile(per, 97))
    print(np.percentile(per, 98))

    thres = np.percentile(per, 88)
    print("thres " + str(thres))
    margin = per > thres
    diff = np.diff(margin)
    print(diff.shape)
    cut_off = np.where(diff != 0)[0]
    print(cut_off)
    cut_demo = np.copy(img)

    mids = []
    for i in range(len(cut_off)):
        if i % 2 == 1:
            continue
        mid = (cut_off[i] + cut_off[i + 1]) // 2
        mids.append(mid)
        cut_demo[mid][:][:] = 0

    cuts = []
    for i in range(len(mids) - 1):
        upper_line = mids[i]
        lower_line = mids[i + 1]
        upper_weight = 0.5
        lower_weight = 1 - upper_weight
        cut = int(upper_line * upper_weight + lower_line * lower_weight)
        cuts.append(cut)
        cut_demo[cut][:][:] = 0

    cv2.imwrite("test.jpg",cut_demo)
    #exit(0)

    print(cut_off, mids)

    boundaries = []
    boundaries += mids
    boundaries += cuts
    boundaries = sorted(boundaries)
    print("bounds: ", boundaries, len(boundaries))
    assert(len(boundaries) == 15)

    image_pieces = []

    month = os.path.basename(input_fn).split('.')[0].split('-')[1]
    right_img_name = "god/god_{}.jpg".format(month)
    right_img = cv2.imread(right_img_name)
    print(right_img.shape)


    for i in range(len(boundaries) - 1):
        start = boundaries[i]
        end = boundaries[i + 1]
        image_pieces.append(np.copy(img[start:end][:][:]))
        print("peice shape: ", image_pieces[-1].shape,)

    for start_index in range(7):
        starting_height = boundaries[0]
        for i in range(7):
            weekday_idx = 2 * (i + start_index) % 14

            height = image_pieces[weekday_idx].shape[0]
            img[starting_height: starting_height + height] = image_pieces[weekday_idx]
            starting_height += height

            days_idx = 2 * i + 1

            height = image_pieces[days_idx].shape[0]
            img[starting_height: starting_height + height] = image_pieces[days_idx]
            starting_height += height

            #print(i, weekday_idx, days_idx, height)
            os.path.basename(input_fn).split('.')

        target_img_name = os.path.join("result", "{}_{}.jpg".format(os.path.basename(input_fn).split('.')[0], ((start_index + 3) % 7) +1))
        output_img = cv2.hconcat([img,right_img])
        cv2.imwrite( target_img_name, output_img)


if __name__ == '__main__':
    input_fn = sys.argv[1]
    main()
