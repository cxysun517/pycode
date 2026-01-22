"""
说明：cxy的烹饪步骤
"""


def cxy_cook_step():
    print('第一步，买菜')
    print('第二步，洗菜')
    print('第三步，切菜')
    print('第四步，炒菜')


print(__name__)

# 以下三行为功能调试代码，只在直接运行此cxy.py文件时才会执行，其它模块import此模块时不执行
if __name__ == '__main__':
    print('我是cxy，今天要炒一个回锅肉')
    cxy_cook_step()
    print('cxy炒完回锅肉啦')

# 如果直接运行此cxy.py文件，__name__值为__main__，功能调试代码就可以被执行，运行结果如下

# __main__
# 我是cxy，今天要炒一个回锅肉
# 第一步，买菜
# 第二步，洗菜
# 第三步，切菜
# 第四步，炒菜
# cxy炒完回锅肉啦
