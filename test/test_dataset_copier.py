#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for package."""
import unittest

from yjs_dataset_copier.dataset_copier import in_out_paths, \
    dataset_name_pattern


class TestScript(unittest.TestCase):
    """Test the script.

    TODO: Test actually writing files.
    TODO: Test/handle non-windows file path.
    # in_path_pattern = r"/Users/joeflack4/Dropbox (Gates Institute)/PMA2020/DataManagement/PMA*_Datasets/Round*/Final*/HH*/*/*.dta"
    out_dir_path = "/Users/joeflack4/Desktop/"
    """

    def test_script(self):
        """Test the script."""
        expected = {'path/to/PMA2015_CDR4_Kinshasa_HHQFQ_v3_20Aug2018.dta':
                        '~/Desktop/CDR4_Kinshasa_HHQFQ.dta',
                    'path/to/PMA2015_ETR5_HHQFQ_v3_20Aug2018.dta':
                        '~/Desktop/ETR5_HHQFQ.dta'}
        in_path_filenames = ['PMA2015_CDR4_Kinshasa_HHQFQ_v3_20Aug2018',
                             'PMA2015_ETR5_HHQFQ_v3_20Aug2018',
                             'PMA2015_CDR4_Kinshasa_SQ_v3_20Aug2018']

        in_paths = ['path/to/' + x + '.dta' for x in in_path_filenames]

        result = in_out_paths(in_paths=in_paths,
                              out_dir='~/Desktop/',
                              pattern=dataset_name_pattern)

        self.assertEqual(expected, result)


if __name__ == '__main__':
        unittest.main()
