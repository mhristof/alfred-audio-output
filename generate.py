#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 mhristof <mhristof@chessell.local>
#
# Distributed under terms of the MIT license.


import json
from sh import SwitchAudioSource


def items():
    ret = []
    for output in SwitchAudioSource('-a'):
        output = output.strip()
        if not output.endswith('(output)'):
            continue
        name = ' '.join(output.split()[0:-1])
        ret += [{
            'uid': name,
            'title': name,
            'arg': name,
        }]

    return ret


def main():
    """docstring for main"""
    print(json.dumps(
        {
            'items': items()
        },
        indent=4))


if __name__ == '__main__':
    main()
