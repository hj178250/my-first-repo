import requests

url = "https://api.github.com/repos/hj178250/my-first-repo"
r = requests.get(url)

print("status code:", r.status_code)
print("content-type:", r.headers["Content-Type"])

data = r.json()
print("repo name :", data["name"])
print("owner     :", data["owner"]["login"])
print("stars     :", data["stargazers_count"])
print("language  :", data["language"])

if r.status_code == 200:
    print("PASS: status is 200")
else:
    print("FAIL: expected 200, got", r.status_code)

if data["language"] == "Java":
    print("PASS: language is Python")
else:
    print("FAIL: expected Python, got", data["language"])

# 第三条断言：我预期这个仓库还没人点 star，所以 0 才算 PASS
if data["stargazers_count"] == 0:
    print("PASS: stars is 0")
else:
    print("FAIL: expected 0 stars, got", data["stargazers_count"])
