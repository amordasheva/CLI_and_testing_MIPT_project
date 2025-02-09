import unittest
import os
import shutil
import tempfile
from feature_directory_analysis import analyze_directory, get_size
from feature_renaming import rename_photos
from feature_copying_files import copy_photos


class TestFeatures(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()

        with open(os.path.join(self.test_dir, 'test1.txt'), 'wb') as f:
            f.write(b'0' * 100)
        with open(os.path.join(self.test_dir, 'test2.jpg'), 'wb') as f:
            f.write(b'0' * 200)

        with open(os.path.join(self.source_dir, 'photo1.jpg'), 'wb') as f:
            f.write(b'0' * 100)
        with open(os.path.join(self.source_dir, 'photo2.jpg'), 'wb') as f:
            f.write(b'0' * 200)
        with open(os.path.join(self.source_dir, 'document.txt'), 'wb') as f:
            f.write(b'0' * 300)

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_analyze_directory(self):
        results = analyze_directory(self.test_dir)
        sizes = [size for _, size in results]
        self.assertEqual(len(results), 2)
        self.assertEqual(sum(sizes), 300)

    def test_get_size(self):
        size = get_size(self.test_dir)
        self.assertEqual(size, 300)

    def test_copy_photos(self):
        copied_files = copy_photos(self.source_dir, self.target_dir)
        self.assertEqual(len(copied_files), 2)

    def test_rename_photos(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
            
        test_file = os.path.join(self.test_dir, 'test.jpg')
        with open(test_file, 'wb') as f:
            f.write(b'0' * 1024)
        rename_photos(self.test_dir)
        files = os.listdir(self.test_dir)
        self.assertEqual(len(files), 1)
        new_filename = files[0]
        self.assertTrue(new_filename.startswith('Photo_'))
        self.assertTrue(new_filename.endswith('.jpg'))

if __name__ == '__main__':
    unittest.main()