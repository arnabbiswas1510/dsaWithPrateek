"""
Add metadata to all the .mp4 files within the given directory, based on the file
names of the input files.
Each input file should use the following format for their filename:
[album]  [title]  [artist]
Note that there are two spaces between each element.
Usage: python add_metadata.py /path/to/mp4/files/
In order to run this script, you must have ffmpeg installed. On Ubuntu, you can 
do so by running `apt-get install ffmpeg`.
Sources:
http://superuser.com/questions/349518/how-to-use-ffmpeg-to-add-metadata-to-an-aac-file-without-reencoding
http://jonhall.info/how_to/create_id3_tags_using_ffmpeg
"""

import sys
import os
import os.path as op
import subprocess


if __name__ == '__main__':
    dirname = sys.argv[1]
    for r,s,f in os.walk(dirname):
        for mp4_file in f:
            if mp4_file.endswith('.mp4'):
                input_path = op.join(dirname, mp4_file)
                title = op.splitext(mp4_file)[0]
                output_path = op.join(dirname, '%s-@#$.mp4' % (title))

                cmd = [
                    'avconv',
                    '-i', input_path,
                    '-vn', '-acodec', 'copy',   # copy, dont' reencode
                    '-metadata', 'title=' + title,
                    output_path,
                                 ]
                print(' '.join(cmd))
                subprocess.call(cmd)