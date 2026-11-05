# ============================================
# 参数化：一条用例，测 N 组数据
# 跑法：python -m pytest -v test_param.py
# ============================================

import pytest            # 这次要用 pytest 自带的一个装饰器，所以要 import 它
import requests

BASE = "https://api.github.com"
REPO = "hj178250/my-first-repo"


# ---------- 参数化写法 ----------
# parametrize 的意思是"参数化"：下面那张表有 N 行数据，这条用例就会跑 N 次
# 每一行 -> 一次独立执行 -> 输出里有独立的一行 PASSED / FAILED
#
# 参数名必须和函数括号里的名字一模一样：field, expected
@pytest.mark.parametrize("field, expected", [
    ("name", "my-first-repo"),          # 第 1 次：字段 name 应该是 my-first-repo
    ("language", "Python"),             # 第 2 次：字段 language 应该是 Python
    ("default_branch", "main"),         # 第 3 次：默认分支应该是 main
])
def test_repo_fields(field, expected):
    r = requests.get(f"{BASE}/repos/{REPO}")
    data = r.json()

    # data[field] = 用变量名去取值（field 这次是 "name"，下次是 "language"）
    # 这一行代码，被 3 行数据复用了 3 次
    assert data[field] == expected
