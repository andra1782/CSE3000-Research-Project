import os
import random
import shutil

source_dir = 'wikiart'
target_dir = 'wikiart_samples'

os.makedirs(target_dir, exist_ok=True)

for style in os.listdir(source_dir):
    style_path = os.path.join(source_dir, style)
    if os.path.isdir(style_path): 
        files = [f for f in os.listdir(style_path) if f.endswith('.jpg')]
        
        if len(files) >= 10:
            selected_files = random.sample(files, 10)
        else:
            selected_files = files
        
        dest_style_path = os.path.join(target_dir, style)
        os.makedirs(dest_style_path, exist_ok=True)
        
        for file in selected_files:
            src_file_path = os.path.join(style_path, file)
            dest_file_path = os.path.join(dest_style_path, file)
            shutil.copy(src_file_path, dest_file_path)
