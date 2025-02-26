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
#******************************  comment **********************************
from re import search
def setComment():
  bufFtype=vim.eval('&filetype')
  if bufFtype=='python':
    curRaw=vim.api.get_current_line()
    if curRaw.find('#')!=-1:
      curRaw=curRaw.replace('#', '')    #, 'g'
      vim.api.set_current_line(curRaw)
    else:
      if mtch:=search(r'^(\s+)(.*)', curRaw):
        空白, 字串=mtch.groups()
        vim.api.set_current_line(f'{空白}#{字串}')
      else:
        vim.api.set_current_line(f'#{curRaw}')

def unComment():
  bufFtype=vim.eval('&filetype')
  if bufFtype=='python':
    curRaw=vim.api.get_current_line()
    vim.api.set_current_line(f'{curRaw[1:]}')
#bufFtype=None
vim.api.set_keymap('n', '<leader>cmt', '<cmd>py3 setComment()<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>ucmt', '<cmd>py3 unComment()<CR>', {'noremap':True, 'silent':False})
#  *****************************  去除punct符號 ***************************
vim.api.set_keymap('n', '<leader>pnct', '<cmd>%s/[；。：，]/ /g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>mdd', '/^\\d<S-V>nnkJ\\mb', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>slb', '<cmd>.s/ //g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>saz', '<cmd>%s/[a-zA-Z]\\+ \\?//g<CR>', {'noremap':True, 'silent':False})  #a-z
vim.api.set_keymap('n', '<leader>dgt', '<cmd>%s/\\d\\+//g<CR>', {'noremap':True, 'silent':False})   #digit
vim.api.set_keymap('n', '<leader>hes', '<cmd>.s/ //g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>mb', '<cmd>%s/ \\+/ /g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>rq', '<cmd>%s# \\?\\([：；、?。！？﹖◎]\\) \\?#\\1#g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>ad', '<cmd>%s#\\(\\d\\+\\)#\\1.#g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>aa', '<cmd>%s#\\([a-zA-Z]\\)#\\1.#g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>aad', '<cmd>%s#\\([a-zA-Z0-9]\\)#\\1.#g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>ru', '<cmd>%s#[^\\u4E00-\\u9FFF|，：。；、! ！#0-9:\\?\\.？a-zA-Z\\/」●◆「《》～\\%\\=◎|[:punct:]]##g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>qr', '<cmd>%s/[（）「」]//g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>rb', '<cmd>%s/[- ]\\+$//g<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>cmb', '<cmd>%s/ \\+/ /g<CR><cmd>%s/ \\+$//g<CR><cmd>%s# \\=\\([：、?！？]\\) \\=#\\1#g<CR>', {'noremap':True, 'silent':False})
