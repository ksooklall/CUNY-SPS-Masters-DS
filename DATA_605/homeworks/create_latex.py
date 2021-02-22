import subprocess
import pandas as pd

def get_latex(m):
    latex = "\[\nA = \\begin{{bmatrix}} \n\t{0} & {1} & {2} \\\ \n\t{3} & {4} & {5} \\\ \n\t{6} & {7} & {8} \\\ \n\t\\end{{bmatrix}}\n\]".format(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], m[8])
    print(latex)
    #cmd='echo '+ str(latex) + '| ccp'
    pd.Series([latex]).to_clipboard(index=False, header=False)
    #subprocess.check_call(cmd, shell=True)

a = [0,2,3,0,3,5,0,0,5]
get_latex(a)
