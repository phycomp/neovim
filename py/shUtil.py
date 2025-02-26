def scpHost(host):
    fname=vim.funcs.expand('%')
    from os import system
    cmd=f'scp "{fname}" "{host}:"'
    print(cmd)
    system(cmd)

vim.command(':com! -nargs=* ScpHost py3 scpHost(<f-args>)')
vim.api.set_keymap('n', '<leader>rid', '<cmd>!rm ~/Downloads/*.Identifier<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>scp', ':ScpHost ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>jpnb', '<cmd>!jupyter-nbconvert --to python "%"<CR>', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<leader>xjs', '<cmd>!xjsMNPL.py ~/.gcin/XiangJingSheng.cin<CR>', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<leader>xia', '<cmd>e ~/.gcin/XiangJingSheng.cin<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>gcin', '<cmd>!gcin2tab ~/.gcin/XiangJingSheng.cin<CR>', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<leader>mkd', ':!mkdir ', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<leader>ntp', '<cmd>!sudo ntpdate tock.stdtime.gov.tw<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>ssn', '<cmd>!ls -trm ~/.config/nvim/sssn<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>chu', '<cmd>!killall chromium<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>fox', '<cmd>!killall firefox<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>chr', '<cmd>!killall chrome<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>lct', ':!locate ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>kall', ':!killall ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>ins', '<cmd>!sudo pacman -Syu --noconfirm<CR>', {'noremap':True, 'silent':False})
