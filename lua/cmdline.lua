require('fine-cmdline').setup({
  cmdline = { enable_keymaps = true, smart_history = true, prompt = ': ' },
  popup = {
    position = { row = '10%', col = '50%'},
    size = { width = '60%', },
    border = { style = 'rounded'},
    win_options = { winhighlight = 'Normal:Normal,FloatBorder:FloatBorder'},
  },
  hooks = {
    before_mount = function(input)
      -- code
    end,
    after_mount = function(input)
      -- code
    end,
    set_keymaps = function(imap, feedkeys)
      -- code
    end
  }
})

vim.api.nvim_set_keymap('c', '<C-A>', '<HOME>', {silent=false, noremap=true})
vim.api.nvim_set_keymap('c', '<C-F>', '<Right>', {silent=false, noremap=true})
vim.api.nvim_set_keymap('c', '<C-D>', '<Delete>', {silent=false, noremap=true})
vim.api.nvim_set_keymap('c', '<C-B>', '<Left>', {silent=false, noremap=true})
vim.api.nvim_set_keymap('c', '<C-E>', '<End>', {silent=false, noremap=true})
vim.api.nvim_set_keymap('c', '<C-K>', ":lua vim.fn.strpart(vim.fn.getcmdline(), 0, vim.fn.getcmdpos() - 1)<CR>", {silent=true, noremap=true})
