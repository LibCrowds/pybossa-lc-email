# -*- coding: utf8 -*-
"""Main package for pybossa-lc-email."""

import os
import json
from flask.ext.plugins import Plugin
from flask import current_app as app
from distutils.dir_util import copy_tree


__plugin__ = "PyBossaLCEmail"
__version__ = json.load(open(os.path.join(os.path.dirname(__file__),
                                          'info.json')))['version']


class PyBossaLCEmail(Plugin):
    """A PYBOSSA plugin for LibCrowds custom email templates."""

    def setup(self):
        self.replace_email_templates()

    def replace_email_templates(self):
        """Replace email templates in the current theme."""
        if not app.config.get('TESTING'):
            out_path = os.path.join('pybossa', app.template_folder, 'account',
                                    'email')
            in_path = os.path.join('pybossa', 'plugins', 'pybossa_lc',
                                   'templates', 'email')
            if not os.path.exists(out_path):
                os.mkdir(out_path)
            copy_tree(in_path, out_path)
