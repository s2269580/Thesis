import pandas as pd
import cv2
import torch
import torch.nn.utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.model_selection import train_test_split
from sam2.build_sam import build_sam2
from sam2.sam2_image_predictor import SAM2ImagePredictor
import random
import tifffile as tiff
from scipy.ndimage import label
import os
import argparse


def read_each_tiff(input_folders):
  gfap_files = sorted(os.listdir(input_folders[2]))
  gfap_files = [f for f in gfap_files if f.endswith('.tif')]
  print(gfap_files)
  
  return gfap_files


def main(args):
  read_each_tiff(args.input_folders)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train SAM2 model")
    parser.add_argument('--input_folder', type=sxtring, default=None, help='Path for input data')

    args = parser.parse_args()
    main(args)
  
  
  
