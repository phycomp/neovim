#********************  tabs **************************
vim.api.set_keymap('n', '<leader>tn', '<cmd>tabnew<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>tp', '<cmd>-tabnew<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>tm0', '<cmd>0tabmove<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>tm$', '<cmd>$tabmove<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>tm#', '<cmd>tabmove #<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<C-S-PageDown>', '<cmd>+tabmove<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<C-S-PageUp>', '<cmd>-tabmove<CR>', {'noremap':True, 'silent':False})  #<A-h>
vim.api.set_keymap('n', '<leader>tl', '<cmd>tabnext<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>th', '<cmd>tabprevious<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>tc', '<cmd>tabclose<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>trn', ':TabRename ', {'noremap':True, 'silent':False})

#from pynvim import autocmd

#@autocmd('BufEnter,BufNewFile,BufRead', pattern='*.py', eval='expand("<afile>")', sync=True)
#def onBufenter(fname):
# print('testplugin is in ' + fname)

#au BufNewFile,BufRead *.py
#    \ set expandtab       |" replace tabs with spaces
#    \ set autoindent      |" copy indent when starting a new line
#    \ set tabstop=4
#    \ set softtabstop=4
#    \ set shiftwidth=4
from pathlib import Path
from os import system
from os.path import splitext
from os import system

#@autocmd('FileType,VimEnter,BufRead,BufNewFile', pattern='*', sync=True)

vim.command('vnoremap <C-X> "+x<CR>')
#vim.api.set_keymap('n', '<leader>prnt', '<cmd>!import -window root -pause 4 /tmp/kdjdk.png|gimp /tmp/kdjdk.png&<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>up', '<cmd>update<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap("c", "<M-b>", "<S-Left>", {'noremap':True, 'silent':False})
vim.api.set_keymap("c", "<M-f>", "<S-Right>", {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>new', '<cmd>enew<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>cpn', '<cmd>copen<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>qq', '<cmd>q<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bnw', '<cmd>new<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>spl', '<cmd>split<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>nhl', '<cmd>nohlsearch<CR>', {'noremap':True, 'silent':False})
##tabUtil
#vim.api.set_keymap('n', '<leader>sc', '<cmd>hi clear Search|hi Search ctermfg=46 ctermbg=DarkRed<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>zz', '<cmd>ZZ<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>trp', '<cmd>term python %<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>chd', "<cmd>CHADopen<CR>", {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>pyf', '<cmd>py3file %<CR>', {'noremap':True, 'silent':False})
##substituUtil
vim.api.set_keymap('n', '<leader>urs', '<cmd>call UltiSnips#RefreshSnippets()<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>qa', '<cmd>qa!<CR>', {'noremap':True, 'silent':False})
