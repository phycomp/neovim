TABs=['仁', '義', '禮', '智', '信', '儒', '釋', '道', '耶', '回', '儒', '聖', '賢', '仙', '佛', '乾', '兌', '離', '震', '巽', '坎', '艮', '坤']  #, '九', '十', '干', '支'
def showTabline():
  s, wn  = '', ''
  tabID, ndx  = vim.funcs.tabpagenr(), 1
  lastTP=vim.funcs.tabpagenr('$')
  while ndx <= lastTP:
      buflist = vim.funcs.tabpagebuflist(ndx)
      winnr = vim.funcs.tabpagewinnr(ndx)
      s += f'%{ndx}T'    # + str(ndx) + 'T'
      s += '%1*' if ndx == tabID else '%2*'
      s += ' '
      wn = vim.funcs.tabpagewinnr(ndx, '$')
      s += '%#TabNum#'
      # s .= '%*'
      s += '%#TabLineSel#' if ndx == tabID else '%#TabLine#'
      s += str(ndx)
      bufnr = buflist[winnr - 1]
      file = vim.funcs.bufname(bufnr)
      buftype = vim.funcs.getbufvar(bufnr, 'buftype')
      #print('buftype=', buftype)
      s += f'{TABs[ndx-1]} '
      #s += f' {file} '
      ndx += 1
  s += '%T%#TabLineFill#%='
  s += '%999XX' if vim.funcs.tabpagenr('$') > 1 else  'X'
  return s
tabLine=showTabline()
#print('tabLine=', tabLine)
#print('tablineVar=', vim.api.get_var('g:tabline'))    #, tabLine
vim.api.set_option('showtabline', 2)
vim.api.set_option('tabline', tabLine)
vim.command('''autocmd! TabEnter,BufEnter,CmdlineChanged * py3f ~/.config/nvim/py/tabLine.py''')
