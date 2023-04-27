#!/bin/sh

for i in 112 176 304 560 1072; do python3 ./lanczos2.py 16 $i; done

