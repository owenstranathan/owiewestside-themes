# -*- coding: utf-8 -*-
"""
    Owiewestside Colorscheme
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Operator, Generic, Name, Number, Comment, Keyword, String, Literal

class OwiewestsideStyle(Style):

    background_color = '#0c0c0c'
    styles = {
        Token:              'noinherit #cccccc bg:#0c0c0c',
        Literal:            'noinherit #b4009e',
        Comment:            'noinherit #61d6d6',
        Keyword:            'noinherit #f9f1a5',
        Name.Tag:           'noinherit #f9f1a5',
        Keyword.Type:       'noinherit #15c60d',
        Name.Constant:      'noinherit #b4009e',
        Generic.Output:     'noinherit #3b78ff',
        Comment.Preproc:    'noinherit #3b78ff',
        Name.Builtin:       'noinherit #b4009e',
        Name.Class:         'noinherit #15c60d',
    }
