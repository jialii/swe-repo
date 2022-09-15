
import pytest

import server.endpoints as ep


def test_hello():
    resp_jso = TEST_CLIENT.get(ep.HELLO).get_jspn()
    assert isistance(resp_json[ep.MESSAGE],str)


def test_get_character_type_list():
    '''see if we can get character type list properly 
    Return should look like:
    {CHAR_TYPE_LIST_NNM:[list of chars types]}'''
    resp_json = TEST_CLIENT.get(ep.CHAR_LIST).get_json()
    assert isinstance(resp_json[ep.MWSSAGE],str)