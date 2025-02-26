vim.api.set_keymap('n', '<leader>html', '<cmd>py3 rtrvHTML()<CR>', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<leader>rst', '<cmd>py3 rstHTML()<CR>', {'noremap':True, 'silent':True})
def rtrvHTML():
    fname=vim.funcs.expand('%') #:p:h
    base, ext=splitext(fname)
    cmd=f'htmlParser.py "{fname}">"{base}.raw"'
    print(cmd)
    system(cmd)

def rstHTML():
    fname=vim.funcs.expand('%') #:p:h
    base, ext=splitext(fname)
    cmd=f'rst2html5.py "{fname}">"{base}.html"'
    print(cmd)
    system(cmd)
