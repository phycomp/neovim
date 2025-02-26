winnr=vim.funcs.winnr
bufnr=vim.funcs.bufnr
getpos=vim.funcs.getpos
setpos=vim.funcs.setpos
execute=vim.funcs.execute
prunFtypes=['help', 'netrw', 'nvimtree']
bufFtype=vim.eval('&filetype')
isFtyped=True if bufFtype not in prunFtypes else False

def RightWin():
    if winnr()==winnr('$'):return
    buf=vim.current.buffer  #bufnr(0)
    #line, col
    prvPos=_, line, col, _=getpos('.')
    #mark=vim.api.buf_set_mark(buf, 'M', line, col, {})
    curBufID=bufnr(buf)
    execute('wincmd l')     #移動游標
    buf=vim.current.buffer  #bufnr(0)
    prvBufID=bufnr(buf)
    execute(f'buffer! {curBufID}')
    execute('wincmd h')     #移動游標
    #print('mark', mark)
    execute(f'buffer! {prvBufID}')
    execute('wincmd l')     #移動游標
    if isFtyped: setpos('.', prvPos)

def LeftWin():
    if winnr()==1:return
    buf=vim.current.buffer  #bufnr(0)
    #line, col
    prvPos=_, line, col, _=getpos('.')
    #mark=vim.api.buf_set_mark(buf, 'M', line, col, {})
    curBufID=bufnr(buf)
    execute('wincmd h')     #移動游標
    buf=vim.current.buffer  #bufnr(0)
    prvBufID=bufnr(buf)
    execute(f'buffer! {curBufID}')
    execute('wincmd l')     #移動游標
    #print('mark', mark)
    execute(f'buffer! {prvBufID}')
    execute('wincmd h')     #移動游標
    if isFtyped: setpos('.', prvPos)
    #setpos(line, col)

vim.api.set_keymap('n', '<leader>wh', '<cmd>py3 LeftWin()<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>wl', '<cmd>py3 RightWin()<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>wcl', '<cmd>wincmd L<CR>', {'noremap':True, 'silent':False})
#vim.api.set_keymap('n', '<leader>alr', '<cmd>wincmd L<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>vn', '<cmd>vnew<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<M-l>', '<cmd>wincmd l<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<M-h>', '<cmd>wincmd h<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<M-j>', '<cmd>wincmd j<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<M-k>', '<cmd>wincmd k<CR>', {'noremap':True, 'silent':False})
