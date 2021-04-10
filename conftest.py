# -*- coding: utf-8 -*-

import pytest

import os

@pytest.fixture(scope = 'module')
def config_pruebas():

    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

    DATA_DIR = os.path.join(CURRENT_DIR,'tests/testData/test_config.yaml')

    return DATA_DIR