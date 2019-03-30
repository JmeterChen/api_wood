# -*- coding: utf-8 -*-#
# __author__ = 'Bo_lin Chen'
# Date: 2019/1/3

import unittest


class ParametrizedTestCase(unittest.TestCase):

    """
    | 目前只要保障 test，staging，pro环境正常即可
    dev环境后面划分给开发为开发环境，不需要再维护
    """
    # env = "dev"
    # env = 'test'
    # env = "staging"
    env = 'pro'
