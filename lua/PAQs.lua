local paqTbl={
  --'iamcco/markdown-preview.nvim',
  'gennaro-tedesco/nvim-peekup',
  'voldikss/vim-floaterm',
  'windwp/vim-floaterm-repl',
  'AckslD/messages.nvim',
  'skywind3000/vim-quickui',
  'godlygeek/tabular',
  --'vim-pandoc/vim-pandoc',
  'vim-pandoc/vim-pandoc-syntax',
  'preservim/vim-markdown',
  'tpope/vim-fugitive',
  'pseewald/vim-anyfold',
  'nvim-lua/plenary.nvim',
  --'madox2/vim-ai',
  'yetone/avante.nvim',
  {"ellisonleao/glow.nvim", build=function() require("glow").setup() end},
  {'nvim-treesitter/nvim-treesitter', build=function() local ts_update = require('nvim-treesitter.install').update({with_sync=true}) ts_update() end},
  {"ms-jpq/chadtree", build=function()vim.cmd[[python3 -m chadtree deps]]end},  --branch='char',
    'BurntSushi/ripgrep',
    {"geg2102/nvim-python-repl", dependencies="nvim-treesitter", ft={"python", "lua", "scala"}, config = function()
        require("nvim-python-repl").setup({ execute_on_send = false, vsplit = false, })
    end },
    --'nanozuki/tabby.nvim',
------------image------
  'edluffy/hologram.nvim',
------------jupyter------
    --'luk400/vim-jukit',
    --{'dccsillag/magma-nvim', build=function()vim.cmd[[:UpdateRemotePlugins]]end },
    --{'dccsillag/magma-nvim', build=':UpdateRemotePlugins'},
    --'ms-jpq/sad',
    'makerj/vim-pdf',
    'arminveres/md-pdf.nvim',
    'ms-jpq/coq_nvim',
    'Vigemus/iron.nvim',
    ---'jupyter/jupyter_client',
    --'seebye/ueberzug',
    --'jupyter-vim/jupyter-vim',
    'dyng/ctrlsf.vim',
    'sharkdp/fd',
    'machakann/vim-sandwich',
    'windwp/nvim-autopairs',
    --'windwp/nvim-ts-autotag',
    'hrsh7th/nvim-cmp',
    'SirVer/ultisnips',
    'dcampos/nvim-snippy',
    'savq/paq-nvim',
    --'nathom/filetype.nvim',
------------'color'---
    --'whatyouhide/vim-gotham',
    --'nanotech/jellybeans.vim',
    --'jonathanfilip/vim-lucius',
    --'tomasr/molokai',
    --'MunifTanjim/nui.nvim',
    'MunifTanjim/nui.nvim',
    'VonHeikemen/fine-cmdline.nvim',
    'grapp-dev/nui-components.nvim',
    --'vonheikemen/fine-cmdline.nvim',
}
require "paq"( paqTbl)

vim.api.nvim_set_keymap('n', '<leader>pqi', "<cmd>PaqInstall<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pqu', "<cmd>PaqUpdate<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pqc', "<cmd>PaqClean<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pqs', "<cmd>PaqSync<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pqt', "<cmd>PaqList<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pqo', "<cmd>PaqLogOpen<CR>", {noremap=true, silent=false})
vim.api.nvim_set_keymap('n', '<leader>pln', "<cmd>PaqLogClean<CR>", {noremap=true, silent=false})
