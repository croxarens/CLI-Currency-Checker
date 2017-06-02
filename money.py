#!/bin/env python3
# -*- coding: utf-8 -*

import sys, list, converter, settings

if __name__ == '__main__' :
    nargs = len(sys.argv)

    if ( nargs == 1 ) :
        orig = settings.settings['currency']['default']

        for curr in settings.settings['currency']['favourite'] :
            val = converter.convert(orig, curr)
            print('1', orig, '=', val, curr)

        print('\nPass -h as agrument to see the help')

    if ( nargs == 2 ) :
        if sys.argv[1] == '-h' :
            print('HELP') # TODO : Write help
        elif sys.argv[1] == 'list' :
            curr = list.list_currencies()
            
            for k in curr:
                print(k, '-', curr[k])

        else :
            print('ERROR : The argument passed is not recognised')


    if ( nargs == 3 ) :
# TODO : Check if the two currencies exists
        if True :
            val = converter.convert(sys.argv[1], sys.argv[2])
            print('1', sys.argv[1], '=', val, sys.argv[2])

    if ( nargs == 4 ) :
# TODO : Check all the parameters
        if True :
            amount = sys.argv[1]
            from_ = sys.argv[2]
            to = sys.argv[3]

            val = converter.convert(from_, to, amount)
            print(amount, from_, '=', val, to)

    if ( nargs > 4 ) :
        print('ERROR : Too many arguments.\nPass -h as argumnet to see the help')
