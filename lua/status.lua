--vim.o.statusline = table.concat(stl)
vim.cmd([[set laststatus=3
set statusline=%F
set statusline+=\%= " separator
set statusline+=%m,%{mode(1)},%n,%Y,%l,%c,%P  "--,BN%n,%c
]])
