def getRegister(*args):
    allReg=[]
    for reg in '*+\"-/_=#%.0123456789abcdefghijklmnopqrstuvwxyz:':
        reginfo=vim.funcs.getreg(reg)
        if reginfo:
            reginfo=reginfo.replace('\n', '')
            regInfo='\t'.join([reg, reginfo])
            allReg.append(regInfo)
    bufWin(allReg)

def rtrvOpt():
    from math import floor
    ui = vim.api.list_uis()[0]
    width, height=ui['width'], ui['height']
    midWidth, midHeight=floor(width/2), floor(height/2)
    opts = {'relative':'editor', 'width':midWidth, 'height':midHeight, 'col':floor(midWidth/2), 'row':floor(midHeight/2), 'anchor':'NW', 'style':'minimal'}
    return opts

def rtrvOPT():
  ui = vim.api.list_uis()[0]
  width, height=ui['width'], ui['height']
  midWidth, midHeight=floor(width/2), floor(height/2)
  opts = {'relative':'editor', 'width':midWidth, 'height':midHeight, 'col':floor(midWidth/2), 'row':floor(midHeight/2), 'anchor':'NW', 'style':'minimal'}
  return opts

def getMark(*args):
    opts = rtrvOpt()    #{'relative':'editor', 'width':width, 'height':height, 'col':0, 'row':1, 'anchor':'NW', 'style':'minimal'}
    allReg=getRegister(args)
    bufWin(allReg)

def cmdVWR(*args):
  opts=rtrvOpt()
  CMD=' '.join(args)
  bufnr=vim.api.create_buf(False, True)
  #vim.api.buf_set_lines(buf, 0, -1, True, rndrInfo)
  vim.command('setlocal buftype=nofile')    # buftype=prompt
  #vim.api.set_current_buf(bufnr)
  #buf_open_scratch()
  win = vim.api.open_win(bufnr, True, opts)
  #vim.command('highlight CustomFloatingWindow ctermbg=darkblue ctermfg=yellow')  #guibg=yellow  guifg=green
  #vim.command('highlight NvimFloatingWindow guifg=yellow guibg=darkblue') #guibg=#f94e3e  term=None guifg=black 
  #vim.api.win_set_option(win, 'winhl', 'Normal:NvimFloatingWindow')   #Normal:MyHighlight CustomFloatingWindow
  vim.command(CMD)
  mkESC(buf)

def bufWin(rndrInfo):
  opts=rtrvOpt()
  buf = vim.api.create_buf(False, True)
  vim.api.buf_set_lines(buf, 0, -1, True, rndrInfo)
  win = vim.api.open_win(buf, 1, opts)
  #vim.command('highlight CustomFloatingWindow ctermbg=darkblue ctermfg=yellow')  #guibg=yellow  guifg=green
  vim.command('highlight NvimFloatingWindow guifg=yellow guibg=darkblue') #guibg=#f94e3e  term=None guifg=black 
  vim.api.win_set_option(win, 'winhl', 'Normal:NvimFloatingWindow')   #Normal:MyHighlight CustomFloatingWindow
  mkESC(buf)

def rndrHELP(hlpTrm):
  opts=rtrvOpt()
  bufnr = vim.api.create_buf(False, True)
  #vim.api.buf_set_lines(buf, 0, -1, True, rndrInfo)
  mkESC(bufnr)
  #local win_id = vim.api.nvim_open_win(buff, true, { relative="editor", border="rounded", style="minimal", width=win_width , height=win_height , row=row , col=col})
  #vim.api.nvim_set_current_win(win_id)
  vim.command('highlight NvimFloatingWindow guifg=yellow guibg=darkblue') #guibg=#f94e3e  term=None guifg=black 
  vim.command(f'help {hlpTrm}')
  winnr = vim.api.open_win(bufnr, True, opts)
  vim.api.set_current_win(winnr)
  vim.api.win_set_option(winnr, 'winhl', 'Normal:NvimFloatingWindow')   #Normal:MyHighlight CustomFloatingWindow
  #vim.command('highlight CustomFloatingWindow ctermbg=darkblue ctermfg=yellow')  #guibg=yellow  guifg=green

def mkESC(buf):
  escKeys = ['<Esc>', '<CR>', '<Leader>q']
  for eKey in escKeys:
      vim.api.buf_set_keymap(buf, 'n', eKey, ':close<CR>', {'silent':True, 'nowait':True, 'noremap':True})

def vwrHelp(*args):
    #bufWin()
    #buf = vim.api.buf_open_scratch(False, True)
    opts=rtrvOpt()
    buf = vim.api.create_buf(False, False)  #True, False
    #vim.command('''setlocal buftype=nofile
    #setlocal bufhidden=hide
    #setlocal noswapfile''')
    CMD=' '.join(args)
    #print('CMD=', CMD)
    win = vim.api.open_win(buf, 1, opts)
    #vim.command('highlight CustomFloatingWindow ctermbg=darkblue ctermfg=yellow')  #guibg=yellow  guifg=green
    vim.command('highlight NvimFloatingWindow guifg=yellow guibg=darkblue') #guibg=#f94e3e  term=None guifg=black 
    vim.api.win_set_option(win, 'winhl', 'Normal:NvimFloatingWindow')   #Normal:MyHighlight CustomFloatingWindow
    mkESC(buf)
    vim.api.set_current_buf(buf)
    vim.command(CMD)

vim.api.set_keymap('n', '<leader>fwr', ":VwrReg ", {'noremap':True, 'silent':False})    #py3 getRegister(f-args)<CR>
vim.api.set_keymap('n', '<leader>fwm', ":VwrMark ", {'noremap':True, 'silent':False})   #py3 getMark(f-args)<CR>
vim.api.set_keymap('n', '<leader>fwc', ":VwrCMD ", {'noremap':True, 'silent':False})   #py3 getMark(f-args)<CR>
vim.api.set_keymap('n', '<leader>fwh', ':HelpVwr ', {'noremap':True, 'silent':False})
vim.command(':com! -complete=command -nargs=* VwrReg py3 getRegister(<f-args>)')
vim.command(':com! -complete=command -nargs=* VwrCMD py3 cmdVWR(<f-args>)')
vim.command(':com! -complete=command -nargs=* VwrMark py3 getMark(<f-args>)')
vim.command(':com! -complete=help -nargs=* HelpVwr py3 rndrHELP(<f-args>)')
#vim.api.set_keymap('n', '<leader>fwh', "<cmd>py3 vwrHelp('f-args')<CR>", {'noremap':True, 'silent':False})
#vim.command(':com! -nargs=* VwrHelp py3 vwrHelp(<f-args>)')
#vim.api.set_keymap('n', '<leader>fwh', ':VwrHelp ', {'noremap':True, 'silent':False})
