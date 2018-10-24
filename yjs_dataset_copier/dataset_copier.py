"""YJ's Dataset Copier

Grabs .dta files that look like the following...
  - PMA2015_CDR4_Kinshasa_HHQFQ_v3_20Aug2018
  - PMA2015_ETR5_HHQFQ_v3_20Aug2018

...and saves somewhere else as:
  - CDR4_Kinshasa_HHQFQ
  - ETR5_HHQFQ

If you run this file directly, it will use the default parameters defined at
the top of the file.
"""
import glob
import os
import re
import shutil


username = 'YoonJoung Choi'

in_path_pattern = r"C:\\Users\\" + username + "\\Dropbox (Gates Institute)\\PMA*_Datasets\\Round*\\Final*\\HH*\\*\\*.dta"
out_dir_path = r"C:\\Users\\" + username + "\\Dropbox (Gates Institute)\\ychoi\\PMA\\PMAdata_YJ\\rawHHQFQ\\"
dataset_name_pattern = r"(PMA20\d\d_)(.*?)(_.*)"

target_dateset_type_identifier = 'HHQFQ'
ext = 'dta'
delimiter = '_'


def in_out_paths(in_paths, out_dir, pattern):
    """Looks for .dta files matching pattern, renames, and copies elsewhere.

    # TODO: This would be much better if just using a correct regexp.

    Args:
        in_paths (list): List of paths to input files.
        out_dir (string): Output directory.
        pattern (string): Regexp for file pattern matching.

    Returns:
         dict: Map of input file paths to new output paths, with files renamed.
    """
    paths = {}

    for in_file_path in in_paths:
        is_hhqfq_dataset = False
        dataset_name_pieces = []
        target = target_dateset_type_identifier
        filename = os.path.split(in_file_path)[1]
        dataset = re.search(pattern, filename)
        # ignores leading 'PMAYYYY_', where 'YYYY' is 4-digit year.
        if dataset:
            unsplit_name_pieces = list(dataset.groups())[1:]
            # fix for regexp that left leading _ in 2nd item.
            unsplit_name_pieces[1] = unsplit_name_pieces[1][1:]

            for piece in unsplit_name_pieces:
                new_pieces = piece.split(delimiter)
                for new_piece in new_pieces:
                    dataset_name_pieces.append(new_piece)
            is_hhqfq_dataset = any([x == target for x in dataset_name_pieces])

        if is_hhqfq_dataset:
            new_name_pieces = []
            for piece in dataset_name_pieces:
                if not new_name_pieces:
                    new_name_pieces.append(piece)
                elif len(new_name_pieces) > 0 and new_name_pieces[-1] != target:
                    new_name_pieces.append(piece)
                else:
                    break
            new_name = delimiter.join(new_name_pieces)
            paths[in_file_path] = out_dir + new_name + '.' + ext

    return paths


def dataset_copier(in_paths=glob.glob(in_path_pattern),
                   out_dir=out_dir_path,
                   pattern=dataset_name_pattern):
    """Looks for .dta files matching pattern, renames, and copies elsewhere.

    Args:
        in_paths (list): List of paths to input files.
        out_dir (string): Output directory.
        pattern (string): Regexp for file pattern matching.

    Side effects:
        Writes files.
    """
    paths = in_out_paths(in_paths=in_paths,
                         out_dir=out_dir,
                         pattern=pattern)
    # from pdb import set_trace
    # set_trace()
    for in_path, out_path in paths.items():
        shutil.copy(in_path, out_path)


if __name__ == '__main__':
    dataset_copier()
