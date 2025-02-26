FTYPE={'python':'python', 'html':'html','py':'python', 'md':'markdown', 'vim':'vim', 'lua':'lua', 'txt':'text', 'csh':'sh', 'bash':'sh', 'sh':'sh'}
def setfType(ftype):
    fType=FTYPE.get(ftype, 'text')
    cmd=f'setf {fType}'
    vim.command(cmd)
vim.api.set_keymap('n', '<leader>sft', ':SetfType ', {'noremap':True, 'silent':False})
vim.command(':com! -nargs=* SetfType py3 setfType(<f-args>)')

def srchPttrn(*args):
  fext=vim.funcs.expand('%:e')
  lenARG=len(args)
  if not fext: fext='py'
  if lenARG==2:   #srchPath
    regExp, srchPath=args
    if srchPath.find('/')!=-1:
      cmd=f'''vimgrep {regExp} {srchPath}/**/*.{fext}'''  #
    else:
      if fext!=srchPath: ext=srchPath
      cmd=f'''vimgrep {regExp} **/*.{fext} **/*.{ext}'''  #
  elif lenARG==3:   #srchPath
    regExp, absPath, ext=args
    if fext!=ext:
      cmd=f'''vimgrep {regExp} {absPath}/**/*.{ext} {absPath}/**/*.{fext}'''  #
    else:
      cmd=f'''vimgrep {regExp} {absPath}/**/*.{fext}'''  #
  else:
    regExp=args[0]#' '.join(args)
    #ext=vim.funcs.expand('%:e')
    cmd=f'''vimgrep {regExp} **/*.{fext}'''  #
  print('cmd=', cmd)
  vim.command(cmd)
vim.command(':com! -nargs=* SrchPttrn py3 srchPttrn(<f-args>)')
vim.api.set_keymap('n', '<leader>spt', ':SrchPttrn ', {'noremap':True, 'silent':False})
"""
:echo @%                |" directory/name of file
:echo expand('%:t')     |" name of file ('tail')
:echo expand('%:p')     |" full path
:echo expand('%:p:h')   |" directory containing file ('head')
"""
