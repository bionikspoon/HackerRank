# ''' Example:
# 8 5
# 2 3 1 2 3 2 3 3
# 0 3
# 4 6
# 6 7
# 3 5
# 0 7
# '''
template_format = """
int:n int:t
list:n:w
feed:t:int:i int:j
"""

ap = 'http://chart.apis.google.com/chart?cht=tx&chl=A_1,%20A_2,%20\cdots,%20A_N'