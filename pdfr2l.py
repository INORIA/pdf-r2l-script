#!/bin/env python2
# -*- mode:python; coding:utf-8-unix; -*-


"""
pdfr2l.py

@author hanepjiv <hanepjiv@gmail.com>
@since 2014/10/08
@date 2015/11/30
"""


# ##############################################################################
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

# ##############################################################################
# ==============================================================================
CURRENT = 1
AGE = 0
REVISION = 0
# ==============================================================================
MAJOR = CURRENT - AGE
VERSION = '{}.{}.{}'.format(MAJOR, AGE, REVISION)
# ##############################################################################
# ==============================================================================
import sys
import shutil
import argparse
# ==============================================================================
from pdfrw import PdfReader, PdfWriter
from pdfrw.objects import PdfDict, PdfName
# ##############################################################################
# ==============================================================================
def pdfr2l(a_src, a_dest):
    """
    pdfr2l
    """
    # --------------------------------------------------------------------------
    src = PdfReader(a_src)
    dest = PdfWriter()

    # dest.addpages(src.pages)

    dest.trailer = src

    # print dest.trailer.Root

    if dest.trailer.Root.ViewerPreferences:
        dest.trailer.Root.ViewerPreferences = PdfDict(Direction=PdfName.R2L)
    else:
        dest.trailer.Root.ViewerPreferences = PdfDict()
        dest.trailer.Root.ViewerPreferences.Direction = PdfName.R2L

    dest.trailer.Root.PageLayout = PdfName.TwoColumnRight

    dest.write(a_dest)
# ==============================================================================
def _parse_args():
    """
    _parse_args
    """
    # --------------------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('-i', '--inplace', nargs='?',
                        const=False, default=None,
                        type=str,
                        help="""
                        edit files in place
                        (makes backup if extension supplied)
                        """)
    parser.add_argument('-o', '--output', nargs='?',
                        type=argparse.FileType('wb'),
                        const=sys.stdout, default=sys.stdout,
                        help="""
                        output file (default: stdout)
                        """)
    parser.add_argument('input', nargs=1,
                        type=argparse.FileType('rb'),
                        help="""
                        input file
                        """)
    return parser.parse_args()
# ==============================================================================
def _main():
    """
    main
    """
    # --------------------------------------------------------------------------
    args = _parse_args()

    if hasattr(args.input, '__getitem__'):
        args.input = args.input[0]

    if args.input.name == args.output.name:
        sys.exit("ERROR: input is output")

    # inplace
    if not args.inplace is None and not args.input is sys.stdin:
        args.output = args.input.name
        # backup
        if not args.inplace is False:
            src = args.input.name
            shutil.copy2(src, src + '.' + args.inplace)

    pdfr2l(args.input, args.output)
# ##############################################################################
# ==============================================================================
if __name__ == '__main__':
    _main()
