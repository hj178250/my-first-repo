# ============================================
# 我的第一个 pytest 接口测试文件
# 跑法：终端里敲   python -m pytest -v
# 注意：文件名和函数名必须以 test 开头，pytest 才认
# ============================================

import requests          # 发请求用的工具箱

# 把不会变的部分提出来，改地址时只改这一行
BASE = "https://api.github.com"
REPO = "hj178250/my-first-repo"


# ---------- 用例 1：状态码应该是 200 ----------
# 一条用例 = 一个函数 + 一句 assert
# assert 后面写"必须成立的条件"，成立就通过，不成立就红
# 不用自己写 if / print，pytest 全包了
def test_repo_status():
    r = requests.get(f"{BASE}/repos/{REPO}")
    assert r.status_code == 200


# ---------- 用例 2：仓库语言应该是 Python ----------
# assert 左边是"实际值"，右边是"预期值"
# 一眼就能看出谁跟谁比，比 if...print 清楚得多
def test_repo_language():
    r = requests.get(f"{BASE}/repos/{REPO}")
    data = r.json()
    assert data["language"] == "Python"


# ---------- 用例 3：盒子套盒子，主人应该是 hj178250 ----------
# 这就是昨天学的嵌套取值，直接放进了断言里
def test_owner_login():
    r = requests.get(f"{BASE}/repos/{REPO}")
    data = r.json()
    assert data["owner"]["login"] == "hj178250"


# ---------- 用例 4：仓库名应该是 my-first-repo ----------
def test_repo_name():
    r = requests.get(f"{BASE}/repos/{REPO}")
    data = r.json()
    assert data["name"] == "my-first-repo"
