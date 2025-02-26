colors = {}

vim.api.set_option('termguicolors', True)
LightViolet='#0c1014' #{'gui':'lightviolet', 'cterm':'lightviolet'} #16
Cyan=LightCyan='#11151c' #{'gui':'lightcyan', 'cterm':'lightcyan'}#233
LightGreen='#091f2e' #17#lightgreen={ 'gui':'lightgreen', 'cterm':'lightgreen'}
LightOrange='#0a3749' #{'gui':'lightorange', 'cterm':'lightorange'} #18
Orange = '#d26937'    #{ 'gui': 'Orange', 'cterm':'orange' } # 166
LightRed='#d3ebe9' #{'gui':'lightred', 'cterm':'lightred'}#194
LightBlue='#1e6479'   #{'gui':'lightblue', 'cterm':'lightblue'}#31
LightPurple='#599cab' #{'gui':'lightpurple', 'cterm':'lightpurple'} #81
LightYellow='#99d1ce' #{'gui':'lightyellow', 'cterm':'lightyellow'}#122
lightVio='#8cfa16'
#Yellow='#99d1ce'  #{'gui':'Yellow', 'cterm':'Yellow'}#122
Yellow = '#edb443'    #{ 'gui': 'yellow', 'cterm':'yellow' } # 226
White='#ff0000'  #{'gui': 'White', 'cterm':'White' } #d3ebe9
#White='#2aa889' #{ 'gui': 'white', 'cterm':'White' }  46
Purple='#599cab'  #{'gui':'purple', 'cterm':'purple'} #81
Red='#c23127'   #{ 'gui': 'red', 'cterm':'red' } # 196
Magenta = '#888ca6'   #{ 'gui': 'magenta', 'cterm':'magenta' }  90
#Magenta='#2aa889'  #{ 'gui': 'Magenta', 'cterm':'Magenta' }  46
Violet = '#4e5166'    #{ 'gui': 'violet', 'cterm':'violet' }  60
Blue='#195466'  #{ 'gui': 'blue', 'cterm':'blue' }  24
Cyan='#33859E'  #cyan={ 'gui': 'cyan', 'cterm':'cyan' }  44
Green='#2aa889' #green={ 'gui': 'green', 'cterm':'green' }  46


def hiSET(hiTerm, guifg, guibg, isBold=None):
  #print('Color=', ctermfg, ctermbg)
  """
  if ctermbg and ctermbg!='None':
  # ctrmbg=ctermbg.get('cterm', None) if ctermbg else None
  guibg=ctermbg.get('gui', None)
  else:
  guibg=None #ctermbg.get('gui', )
  #if ctermfg and ctermfg!='None':
  # ctrmfg=ctermfg.get('cterm', None) if ctermfg else None
  guifg=ctermfg.get('gui', None)
  """
 
  #CMD=f'exec "hi clear {hiTerm}|hi {hiTerm} ctermfg={ctermfg} ctermbg={ctermbg} guifg={ctermfg} guibg={ctermbg} gui=NONE cterm=NONE"'
  #set termguicolors
  #if ctermbg:
  CMD=f'exec "hi clear {hiTerm}|hi! {hiTerm} guifg={guifg} guibg={guibg}"' #ctermfg={ctrmfg} ctermbg={ctrmbg}
  if isBold:
    #boldTerm=''
    CMD=f'exec "hi clear {hiTerm}|hi! {hiTerm} guifg={guifg} guibg={guibg} gui=bold"' #ctermfg={ctrmfg} ctermbg={ctrmbg}
  #print('CMD=', CMD)
  vim.command(CMD)

"""
Red LightRed DarkRed Green LightGreen DarkGreen SeaGreen Blue LightBlue DarkBlue SlateBlue Cyan LightCyan DarkCyan Magenta LightMagenta DarkMagenta Yellow LightYellow Brown DarkYellow Gray LightGray DarkGray Black White Orange Purple Violet
Red LightRed DarkRed Green LightGreen DarkGreen SeaGreen Blue LightBlue DarkBlue SlateBlue Cyan LightCyan DarkCyan Magenta LightMagenta DarkMagenta Yellow LightYellow Brown DarkYellow Gray LightGray DarkGray Black White Orange Purple Violet
The format is "#rrggbb", where "rr" is the Red value "gg" is the Green value "bb" is the Blue value. All values are hexadecimal, range from "00" to "ff".  :highlight Comment guifg=#11f0c3 guibg=#ff00ff
cyanVio='#c7fc4c'
orangeYellow='#fac916'
orangeCyan='#d2fc6f'
deepOrange='#fa671e'
lightYellow='#f2dc6d'
"""
螢光, 乳白, 粉紅='#5def60', 'FFFED3', 'FF76CE'
天空, 海='5BBCFF', '7EA1FF'
hiSET('Normal', 'Yellow', None)   #LightPurple lightYellow orangeCyan deepOrange cyanVio Magenta
hiSET('Cursor', 'Cyan', None) #orange
hiSET('Search', 'Red', None, isBold=True)
hiSET('CursorLine', 'White', None)
#hiSET('CursorColumn', 'magenta', base1)
#hiSET('CursorLineNr', 'base5', 'lnrBckgrnd')
#hiSET('LineNr', 'yellow', 'lnrBckgrnd')
#hiSET('SignColumn', None, 'lnrBckgrnd')
#hiSET('ColorColumn', None, 'lnrBckgrnd')
#hiSET('Conceal', 'Cyan', 'bckGrnd')
#hiSET('Todo', 'Magenta', 'bckGrnd')

hiSET('pythonComment', 螢光, None)   #White 'Green'
hiSET('pythonStatement', 'LightGreen', None)
#hiSET('pythonStatement', 'LightBlue', None)
hiSET('pythonFunction', 'LightRed', None)
hiSET('pythonString', 'White', None) #Red Yellow , isBold=True
hiSET('String', 'Yellow', None)   #Green
hiSET('Number', 'Orange', None)
hiSET('Comment', 'Cyan', None)
hiSET('Statement', 'Red', None)    #LightGreen
#hiSET('Special', orange, None)
#hiSET('Identifier', base5, None)
#hiSET('Constant', magenta, None)

#hiSET('VertSplit', 'Red', None, isBold=True) #'LightGreen'
hiSET('WinSeparator', 'Yellow', None, isBold=True)    #LightGreen
hiSET('StatusLine', 'LightRed', None, isBold=True)
hiSET('WildMenu', 'LightPurple', 'Cyan')
#hiSET('StatusLineNC', Blue, base2)
#hiSET('ErrorMsg', Cyan, base1)
hiSET('MsgArea', 'Cyan', None)
hiSET('Error', 'Red', None)   #base1
#hiSET('ModeMsg', Blue, None)
hiSET('WarningMsg', 'Yellow', None)

hiSET('TabLineSel', 'Yellow', None, isBold=True)
hiSET('TabLine', 'Cyan', None)
hiSET('TabLineFill', 'Green', None)
#hiSET('Title', orange, yellow)

hiSET('Visual', 'Yellow', 'Magenta', isBold=True)
hiSET('CurSearch', 'Cyan', None, isBold=True)
hiSET('IncSearch', 'Orange', None, isBold=True)
hiSET('MatchParen', 'LightOrange', 'Orange')
#call s:Attr('IncSearch', 'reverse')
hiSET('Pmenu', 'Cyan', None)
hiSET('PmenuSel', 'Magenta', 'Blue', isBold=True)
hiSET('PmenuSbar', 'Yellow', None)
hiSET('PmenuThumb', 'Red', 'Blue')
#hiSET('CtrlPNoEntries', base7, orange)
#hiSET('CtrlPMatch', green, orange)
#hiSET('CtrlPPrtBase', blue, orange)
#hiSET('CtrlPPrtText', cyan, orange)
#hiSET('CtrlPPtrCursor', base7, orange)

vim.command(':com! -nargs=* SetHiColor py3 hiSET(<f-args>)')
vim.api.set_keymap('n', '<leader>his', '<cmd>SetHiColor<CR>', {'noremap':True, 'silent':False})
#vim.api.set_hl(0, "Visual", {'fg':"yellow", 'bg':"Violet", 'bold':True})
