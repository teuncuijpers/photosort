import pandas as pd
import os
import pickle
from PIL import Image, ExifTags

path = "C:\\Users\\teun0\\Documents"

extensions = [".jpg", ".jpeg"]

def extract_exif(filepath, file): 

    print(f"Now processing {filepath}")
    image = Image.open(filepath)
    exif = image.getexif()

    def get_field(exif, field):
        for (k,v) in exif.items():
            if ExifTags.TAGS.get(k, k) == field:
                return v
            
    out_dict = {
        "Filepath": filepath, 
        "File": file,
        "DateTimeOriginal": get_field(exif, "DateTimeOriginal"),
        "ImageWidth": get_field(exif, "ExifImageWidth"),
        "ImageHeight": get_field(exif, "ExifImageHeight"),
        "CameraMake": get_field(exif, "Make"),
        "CameraModel": get_field(exif, "Model"),
        "Software": get_field(exif, "Software"), 
        "Orientation": get_field(exif, "Orientation")
    }

    return out_dict

        
def walk(rootpath, extensions, action=extract_exif):

    list_of_dicts = []

    for root, dirs, files in os.walk(rootpath): 
        for file in files:
            if file.endswith(".jpg"): 
                exif_dict = action("\\".join((root, file)), file)
                list_of_dicts.append(exif_dict)

    return list_of_dicts

def main(): 
    df = pd.DataFrame(walk(path, extensions, extract_exif))
    with open(r"data\df.pickle", "wb") as f:
        pickle.dump(df, f)

if __name__ == "__main__": 
    main()
