import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total resposerise:", response_dict['total_count'])   # 指出github包含多少个Python仓库
# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
    }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()  # 创建Pygal类COnfig实例,通过修改my_config定制图标外观
my_config.x_label_rotation = 45 # 让标签绕x轴旋转45度(x_label_rotatio=45)
my_config.show_legend = False # 隐藏图例(show_legend=False)
my_config.title_font_size = 24 # 图标标题
my_config.label_font_size = 14 # 副标题
my_config.major_label_font_size = 18 # 主标题(Y轴5000证书倍的刻度)
my_config.truncate_label = 15 # 将较长的项目名缩短为15个字符
my_config.show_y_guides = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义宽度

# 图表
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)#创建条形图，让标签绕x轴旋转45度（x_label_rotation=45 ），隐藏图例（show_legend=False ）
chart.title = 'Most-Starred Python Projects on GitHub'#指定标题
chart.x_labels=names#横坐标标签
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

