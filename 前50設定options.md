Top 50 Vim Configuration Options
Tuesday, February 15, 2022
Few products rival Vim's flexibility, since it currently supports over 380 configuration options, not including the hundreds of possible key bindings. While the sheer magnitude of choices are overwhelming, here are 50 of the most important configurations you need to know.

Before We Begin
The "vimrc" (Vim resource configuration) file provides initialization settings that configure Vim every time it starts. This file can be found in "$HOME/.vimrc" for Linux/OSX and "$HOME/_vimrc" for Windows users. Inside Vim, type ":echo $HOME" to see the value of "$HOME" for your system.

Indention Options
set autoindent: New lines inherit the indentation of previous lines.
set expandtab: Convert tabs to spaces.
set filetype indent on: Enable indentation rules that are file-type specific.
set shiftround: When shifting lines, round the indentation to the nearest multiple of "shiftwidth."
set shiftwidth=4: When shifting, indent using four spaces.
set smarttab: Insert "tabstop" number of spaces when the "tab" key is pressed.
set tabstop=4: Indent using four spaces.
Search Options
set hlsearch: Enable search highlighting.
set ignorecase: Ignore case when searching.
set incsearch: Incremental search that shows partial matches.
set smartcase: Automatically switch search to case-sensitive when search query contains an uppercase letter.
Performance Options
set complete-=i: Limit the files searched for auto-completes.
set lazyredraw: Don't update screen during macro and script execution.
Text Rendering Options
set display+=lastline: Always try to show a paragraph's last line.
set encoding=utf-8: Use an encoding that supports unicode.
set linebreak: Avoid wrapping a line in the middle of a word.
set scrolloff=1: The number of screen lines to keep above and below the cursor.
set sidescrolloff=5: The number of screen columns to keep to the left and right of the cursor.
syntax enable: Enable syntax highlighting.
set wrap: Enable line wrapping.
User Interface Options
set laststatus=2: Always display the status bar.
set ruler: Always show cursor position.
set wildmenu: Display command line's tab complete options as a menu.
set tabpagemax=50: Maximum number of tab pages that can be opened from the command line.
set colorscheme wombat256mod: Change color scheme.
set cursorline: Highlight the line currently under cursor.
set number: Show line numbers on the sidebar.
set relativenumber: Show line number on the current line and relative numbers on all other lines.
set noerrorbells: Disable beep on errors.
set visualbell: Flash the screen instead of beeping on errors.
set mouse=a: Enable mouse for scrolling and resizing.
set title: Set the window's title, reflecting the file currently being edited.
set background=dark: Use colors that suit a dark background.
Code Folding Options
set foldmethod=indent: Fold based on indention levels.
set foldnestmax=3: Only fold up to three nested levels.
set nofoldenable: Disable folding by default.
Miscellaneous Options
set autoread: Automatically re-read files if unmodified inside Vim.
set backspace=indent,eol,start: Allow backspacing over indention, line breaks and insertion start.
set backupdir=~/.cache/vim: Directory to store backup files.
set confirm: Display a confirmation dialog when closing an unsaved file.
set dir=~/.cache/vim: Directory to store swap files.
set formatoptions+=j: Delete comment characters when joining lines.
set hidden: Hide files in the background instead of closing them.
set history=1000: Increase the undo limit.
set nomodeline: Ignore file's mode lines; use vimrc configurations instead.
set noswapfile: Disable swap files.
set nrformats-=octal: Interpret octal as decimal when incrementing numbers.
set shell: The shell used to execute commands.
set spell: Enable spellchecking.
set wildignore+=.pyc,.swp: Ignore files matching these patterns when opening files based on a glob pattern.
Hopefully, these settings help you configure Vim to suit your preferences. If not, there are 330 other settings to explore!
