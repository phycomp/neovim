from math import ceil as mthCeil
def rtrvOPT():
  #ui=vim.api.list_uis()[0]
  #width, height=ui.get('width'), ui.get('height')
  #opts={'relative':'editor', 'width':width, 'height':height, 'col':width/2-(width/2), 'row':height/2-(height/2), 'anchor':'NW', 'style':'minimal'}
  width=vim.api.get_option('columns')
  height=vim.api.get_option('lines')
  winHeight=mthCeil(height*.8 - 4)
  winWidth=mthCeil(width*.8)
  row=mthCeil((height-winHeight)/2 - 1)
  col=mthCeil((width-winWidth)/2)
  opts={'style':'minimal', 'relative':'editor', 'width':winWidth, 'height':winHeight, 'row':row, 'col':col, 'border':'rounded'}
  return opts

def bufWin(msg):
  bufnr=vim.api.create_buf(False, True)
  vim.api.buf_set_lines(bufnr, 0, -1, True, msg)
  opts=rtrvOPT() #{'relative':'cursor', 'width':10, 'height':2, 'col':0, 'row':1, 'anchor':'NW', 'style':'minimal'}
  winnr=vim.api.open_win(bufnr, 0, opts) #optional: change highlight, otherwise Pmenu is used
  vim.api.set_option_value('winhl', 'Normal:MyHighlight', {'win':winnr})
  return bufnr, winnr

def vwrCMD(*args):
  bufnr=vim.api.create_buf(False, True)
  #vim.api.buf_set_lines(bufnr, 0, -1, True, msg)
  opts=rtrvOPT() #{'relative':'cursor', 'width':10, 'height':2, 'col':0, 'row':1, 'anchor':'NW', 'style':'minimal'}
  winnr=vim.api.open_win(bufnr, 0, opts) #optional: change highlight, otherwise Pmenu is used
  vim.api.set_option_value('winhl', 'Normal:MyHighlight', {'win':winnr})
  CMD=' '.join(args)
  vim.command('setlocal buftype=nofile')
  vim.command(CMD)
  return bufnr, winnr
***************************************  float win ***********************************
  def rtrvOPT():
  ui=nvim.api.list_uis()[0]
  opts={'relative':'editor', 'width':ui.width, 'height':ui.height, 'col':(ui.width/2) - (width/2), 'row':(ui.height/2) - (height/2), 'anchor':'NW', 'style':'minimal'}
  return opts

def escBuf(bufnr):
  escKeys = ['<Esc>', '<CR>', '<Leader>']
  for esc in escKeys:
    nvim.api.buf_set_keymap(bufnr, 'n', esc, ':close<CR>', {'silent': True, 'nowait': True, 'noremap': True})
def bufAssgn(keys, message):
  for key in keys:
    nvim.api.set_keymap('n', key, ':py bufWin(message)<CR>', {'silent':True, 'nowait':True, 'noremap':True})

def bufWin(msg):
  width, height = 50, 10
  bufnr = nvim.api.create_buf(False, True)
  let top = f"╭─{'-'*(width-2)}╮"
  let mid = f"│ {' '*(width-2)}│"
  let bot = f"╰─{'-'*(width-2)}╯"
  #horBorder=f"+{'-'*(width-2)}+"
  #emptyLine=f"|{' '*(width - 2)}|"
  lines = flatten([horBorder, map(range(height-2), 'emptyLine'), horBorder])
  nvim.api.buf_set_lines(buf, 0, -1, False, lines)
  offset = 0
  for line in msg:
    start = (width - len(line))/2
    end = start + len(line)
    current = height/2-len(a:message)/2 + offset
    offset += 1
    nvim.api.buf_set_text(buf, current, start, current, end, [line])

  winnr = nvim.api.open_win(bufnr, True, opts)
  nvim.api.win_set_option(winnr, 'winhl', 'Normal:ErrorFloat')

