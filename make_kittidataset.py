from genericpath import isdir, isfile
import cv2
import function
import os
import tqdm

if not os.path.isdir('data'):
    os.makedirs('data/depth/train')
    os.makedirs('data/depth/val')
    os.makedirs('data/depth/test')
    os.makedirs('data/rgb/train')
    os.makedirs('data/rgb/val')
    os.makedirs('data/rgb/test')

for cheetsheet in os.listdir('cheetsheets'):
    if cheetsheet == 'train.txt':
        output_dir = 'data/depth/train'
        mode = 'train'
    elif cheetsheet == 'test.txt':
        output_dir = 'data/depth/val'
        mode = 'val'
    else:
        output_dir = 'data/depth/test'
        mode = 'test'
    
    print(mode)
    i = 0
    with open(os.path.join('cheetsheets', cheetsheet)) as f:
        for rgb_path in tqdm.tqdm(f):
            rgb_path = rgb_path.replace('\n','')
            depth_path = rgb_path.replace('image_02/data', 'proj_depth/groundtruth/image_02')
            print(depth_path)
            if os.path.isfile(depth_path):
                rgb = cv2.imread(rgb_path)
                depth = cv2.imread(depth_path)
                output = function.fill_depth_colorization(rgb, depth)
                cv2.imwrite(output_dir + '/%08d' %i + '.png', output)
                cv2.imwrite(output_dir.replace('depth', 'rgb') + '/%08d' %i + '.png', rgb)
                i += 1


