import matplotlib
import os

matplotlib_path = matplotlib.__path__[0]

# ディレクトリ判別
is_directory = os.path.isdir(matplotlib_path)
# ファイル判別
is_file = os.path.isfile(matplotlib_path)

if is_directory:
    print('ディレクトリです')
    result = ('ディレクトリです')
else:
    print('ディレクトリではありません.ファイルです.')
    result = ('ディレクトリではありません.ファイルです.')

matplotlib_path, result