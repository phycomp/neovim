def bufWindow():
  col=vim.api.get_option('columns')
  LINE=vim.api.get_option('lines')
  width, height=min([col - 4, max([80, col - 20])]), min([LINE - 4, max([20, LINE - 10])])
  top, left=(LINE-height)/2-1, (col-width)/2
  opts = {'relative':'editor', 'row':top, 'col':left, 'width':width, 'height':height, 'style':'minimal'}

  top = f"╭{'─'*(width - 2)}╮"
  mid = f"│{' '*(width - 2)}│"
  bot = f"╰{'─'*(width - 2)}╯"
  msg = [top] + [mid]*(height - 2) + [bot]
  bufnr = vim.api.create_buf(False, True)
  vim.api.buf_set_lines(bufnr, 0, -1, True, msg)
  vim.api.open_win(bufnr, True, opts)
  vim.api.set_option('winhl', 'Normal:Floating')
  #vim.command('set winhl=Normal:Floating')
  #opts.row += 1
  #opts.height -= 2
  #opts.col += 2
  #opts.width -= 4
  textbuf=vim.api.create_buf(False, True)
  vim.api.open_win(textbuf, True, opts)
  #vim.command(f'au BufWipeout <buffer> bw {bufnr}')
  return textbuf

def fwHelp(query):
  bufnr = bufWindow()
  vim.api.set_current_buf(bufnr)
  vim.command('setlocal filetype=help')
  vim.command('setlocal buftype=help')
  vim.command(f'help {query}')
vim.command('command! -complete=help -nargs=? HelpVwr py3 fwHelp(<q-args>)')
