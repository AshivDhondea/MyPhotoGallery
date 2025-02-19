from galleryorg import gphotos_json
from galleryorg.utils import data_io
from typing import List
import argparse
import os
import pandas as pd


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True, help="Google Photos folder.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Gallery Metadata file")
    parser.add_argument("-f", "--function", choices=['i', 'index'], required=True, help="Operation to execute.")

    args = parser.parse_args()
    input_folder = args.input
    function = args.function
    output_file = args.output

    # Check input folder.
    data_io.check_directory(input_folder)

    # Check arguments.
    if function not in ('i', 'index'):
        ni_err = f"{function} is not implemented."
        raise NotImplementedError(ni_err)

    if not data_io.check_file_types_in_directory(input_folder, 'json'):
        fnf_err = f"No JSON files in {input_folder}"
        raise FileNotFoundError(fnf_err)

    json_files: List[str] = [f for f in os.listdir(input_folder) if f.endswith('json')]
    metadata_list = list()

    for j in json_files:
        # For each JSON file, check if the corresponding image file is available.
        json_prefix = j.split('.json')[0]
        file_path = os.path.join(input_folder, json_prefix) # JSON file accompanies an image or video file.
        if j != 'metadata.json':
            # Ignore the metadata JSON for the whole album.
            data_io.check_file(file_path)

            metadata_dict = gphotos_json.parse_json(os.path.join(input_folder, j))
            metadata_list.append(metadata_dict)

    metadata_df = pd.DataFrame(metadata_list)
    metadata_df.to_csv(output_file, encoding='utf-8', index=False, header=True)




