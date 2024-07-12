# def test_abc():
#     assert 1==2
import re
from requests import Session

# 发送请求
session = Session()  # 共享参数，cookie，复用tcp连接（HTTP 1.1 keep-alive）

# 路径
base_url = 'http://47.107.116.139'


def test_go_home():
    resp = session.request('GET', base_url + '/phpwind/index.php')
    assert resp.status_code == 200


global _statu_g1

def test_login():
    resp = session.request('POST', base_url + '/phpwind/index.php', headers={},
    data={})
    assert resp.status_code == 200
    assert resp.json()['state'] == 'success'

    _statu_g1 = re.findall('_statu%3D(.*)', 'refresh', resp.text)[0]



def test_back_home():
    resp = session.request('POST', base_url + f'/phpwind/index.php?m=u&c=login&a=welcome&_statu={_statu_g1}', headers={},
                           data={})
    assert resp.status_code == 200
    assert resp.json()['state'] == 'success'
    assert '......' in resp.text



def test_new_post():
    assert False