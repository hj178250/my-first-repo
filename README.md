# 接口自动化测试（requests + pytest）

## 这是什么
用 Python 对 GitHub 公开 API 做的接口测试练习。
不含 UI，纯接口层：发请求 → 拿 JSON → 断言字段值。

## 测了什么
- 仓库状态码是否为 200
- 仓库主语言是否为 Python
- 仓库所有者是否为本人账号
- 默认分支是否为 main（用参数化一次跑 3 组数据）

## 怎么跑
先装 requests 和 pytest：
pip install requests pytest

再进到项目文件夹，敲：
python -m pytest -v


## 运行结果
9 passed in 8.73s


## 用到的技术
Python 3.14 / requests / pytest / @pytest.mark.parametrize / GitHub REST API
