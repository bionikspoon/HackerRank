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
template_format2 = """
n(2, 10**5) t(1, 10**3)
n[w(1, 3)]
t{i(1, n-2) j(n-1, n)}
"""

ap = 'http://chart.apis.google.com/chart?cht=tx&chl=A_1,%20A_2,%20\cdots,%20A_N'