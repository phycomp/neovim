vim.api.set_keymap('v', '<C-Insert>', '"+y', {'noremap':True, 'silent':True})
vim.api.set_keymap('n', '<S-Insert>', '"+gP<CR>', {'noremap':True, 'silent':True})
vim.api.set_keymap('i', '<S-Insert>', '<C-R>+', {'noremap':True, 'silent':True})
vim.api.set_keymap('c', '<S-Insert>', '<C-R>+', {'noremap':True, 'silent':False})
"""
vim.command(
  "snoremap <C-x> :"+x<CR>
  vnoremap <C-X> "+x<CR>
  imap <c-t> <c-o>:!./demo3.py<cr>
  tnoremap <C-q> <C-/><C-n>
)
"""
