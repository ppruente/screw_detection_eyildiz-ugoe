import h5py
import cv2
import os

filepath_screw = './dataset/data/screw.h5'
filepath_non_screw = './dataset/data/non_screw.h5'
target_screw = './dataset/data/screw'
target_non_screw = './dataset/data/non_screw'

for target_path in [target_screw, target_non_screw]:
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    else:
        raise Exception(f'Path {target_path} already exists!')

for filepath, target_path in zip([filepath_screw, filepath_non_screw], [target_screw, target_non_screw]):
    print(f'Processing {filepath}', end='\n')
    data = h5py.File(filepath)['data']
    num_images = len(data)
    for idx, img in enumerate(data):
        cv2.imwrite(os.path.join(target_path, f'image_{idx}.jpg'), img)
        print(f'Processing {idx} of {num_images}', end='\r')
    print(f'\nDone processing {filepath}', end='\n')
