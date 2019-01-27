import requests


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total resposerise:", response_dict['total_count'])   # 指出github包含多少个Python仓库
# 探索有关仓库的信息
repo_dicts = response_dict['items'] # respose_dict字典存储在列表中, 列表里每个字典都包含有关一个Python仓库的信息
print("Repositorise returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nkeys:", len(repo_dicts))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
for repo_dicts in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
