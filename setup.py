# -*- mode:python; coding:utf-8-unix; -*-


"""
setup.py

@author hanepjiv <hanepjiv@gmail.com>
@since 2014/10/20
@date 2015/11/30
"""


#############################################
# The MIT License (MIT)
#
# Copyright (c) <2014> hanepjiv <hanepjiv@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


if __name__ == '__main__':
    from sys import version
    if version < '2.2.3':
        from distutils.dist import DistributionMetadata
        DistributionMetadata.classifiers = None
        DistributionMetadata.download_url = None

    from pdfr2l import VERSION
    from distutils.core import setup
    setup(name='pdfr2l',
          version=VERSION,
          description='PDF R2L',
          author='hanepjiv',
          author_email='hanepjiv@gmail.com',
          url='https://bitbucket.org/hanepjiv/pdfr2l',
          download_url='https://bitbucket.org/hanepjiv/pdfr2l/downloads',
          packages=[],
          py_modules=[],
          scripts=['pdfr2l.py'],
          ext_modules=[],
          data_files=[],
          classifiers=[],
          license='The MIT License (MIT)',
          requires=['pdfrw(>=0.1, <1.0)'],
    )
