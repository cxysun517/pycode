# zsh模块导入cxy模块时，cxy.py的代码被执行，__name__值为cxy，cxy模块的功能调试代码不会被执行
import cxy

print(cxy.__doc__)

print('欢迎来到学徒zsh的店')
print('我是zsh，我今天学习炒菜')
cxy.cxy_cook_step()
print('我学完啦!')

# cxy
#
# 说明：cxy的烹饪步骤
#
# 欢迎来到学徒zsh的店
# 我是zsh，我今天学习炒菜
# 第一步，买菜
# 第二步，洗菜
# 第三步，切菜
# 第四步，炒菜
# 我学完啦!
