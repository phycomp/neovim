10 essential Vim plugins for 2018 Alex Hunt Jan 12, 2018 · 6 min read
Vim remains a powerful and ubiquitous application to tackle any number of text editing tasks conveniently from the terminal (some learning required). If you’re looking to add Vim to your toolkit this year, here is my list of absolutely essential plugins to begin supercharging your workflow.
If you’ve never set up a Vim plugin before, see the Installing Vim plugins section later on for a runthrough.
1. fzf https://github.com/junegunn/fzf.vim Working on a substantial codebase usually involves traversing several files at a time. fzf stands for “fuzzy finder” and works similarly to the Goto Anything menu in Sublime Text, allowing you to open a file instantly after typing a rough representation of its name.
Whilst CtrlP has existed for a while, fzf offers significantly better performance. You can activate the search pane with the :Files command, but I use this so often that I’ve mapped it to a single key.
map ; :Files<CR>
fzf is actually its own terminal command as well, which you can use to get the same awesome file searching functionality anywhere.
2. lightline
https://github.com/itchyny/lightline.vim
Many users like to use a plugin to replace their statusline — whether as an improved visual aid (particularly in split panes), or just to make their editor more attractive. For me, lightline is an elegant and versatile choice.
Image source: lightline repository
The default layout is pretty clean, displaying the current mode with some nice colour feedback, as well as the file name, file properties and cursor position. It’s easy to configure what to show in each section in your .vimrc file, and there’s also a choice of built-in colour schemes.
let g:lightline = {
  \     'active': {
  \         'left': [['mode', 'paste' ], ['readonly', 'filename', 'modified']],
  \         'right': [['lineinfo'], ['percent'], ['fileformat', 'fileencoding']]
  \     }
  \ }
3. vim-multiple-cursors
https://github.com/terryma/vim-multiple-cursors
This is another plugin bringing a much-loved Sublime feature to Vim, doing exactly what it says in the name. You’ve got to love multiple selections.
To make a basic selection, use the Ctrl+N keystroke in normal mode, followed by a motion:
    c – change text.
    I – insert at start of range.
    A – insert at end of range.
More actions can be found in the plugin’s quick start information.
4. vim-eunuch
https://github.com/tpope/vim-eunuch
This cryptically-named plugin adds a dozen core Unix file operations as Vim commands in the context of the current file. :!mv no more!
:Rename new_name.sh
:Chmod +x
:SudoWrite
These small helpers add up fast to not breaking your Vim workflow. All commands are documented in the project README.
5. surround
https://github.com/tpope/vim-surround
In a graphical text editor, typing an open bracket or quotes on a selected region will wrap or surround that region with with a matching pair of characters.
With this plugin, you can do that and more — with motions to add, change or remove surrounding characters and strings in a variety of ways. Definitely check out the docs for this one.
6. NERDTree
https://github.com/scrooloose/nerdtree
NERDTree is a popular plugin to display an interactive file tree view in a side panel, which can be useful when working in larger project. I have the NERDTreeToggle command mapped to Ctrl+O.
map <C-o> :NERDTreeToggle<CR>
7. EditorConfig
https://github.com/editorconfig/editorconfig-vim
EditorConfig is a multi-editor tool for defining base file handling and code style preferences in a project and aligning these between editors. With this plugin, rulesets defined in a local .editorconfig file will automatically configure Vim settings such as indentation size, and apply formatting such as removing trailing whitespace on save.
root = true[*]
charset = utf-8
indent_style = space
indent_size = 4
trim_trailing_whitespace = true
insert_final_newline = true[*.md]
trim_trailing_whitespace = false
This is a boon for everyone, and prevents incoming developers from altering their default preferences manually when working between projects. Recommended for every editor you use.
8. Emmet
https://github.com/mattn/emmet-vim
Another plugin you’re likely to have used in another editor is Emmet. Emmet is a powerful completion tool for HTML, CSS and JavaScript which allows you to make dynamic completions from a shorthand expression.
In Vim, enter a expression such as the above in an HTML file and use Ctrl+Y, , from normal mode to expand it. If you’re not familiar with the abbreviation syntax, there’s a short demo video as well as documentation on the Emmet website. Along with Vim’s snippets feature, this plugin can seriously up your code completion game, and again is essential if you’re working on web projects in other editors.
9. ALE
https://github.com/w0rp/ale
ALE (Asynchronous Lint Engine) is a comprehensive code analysis plugin for Vim. As you edit, it’ll run the current file through an external tool of choice and displays marks for any errors and warnings directly in Vim’s sign column. Navigate to these or toggle a summary pane with :ALEDetail to see a specific message.
Built-in are strong defaults for matching common tools for most programming and config languages if they are present on your system. It’s also fairly easy to reconfigure these mappings. Remember, you can define per-file-type settings for Vim in ~/.vim/ftplugin/{filetype}.vim. Here, I’ve extended the available linters for Python files:
let b:ale_linters = ['pyflakes', 'flake8', 'pylint']
You can also configure fixers for applying formatting on save:
let b:ale_fixers = ['eslint']
let b:ale_fix_on_save = 1
10. vim-gitgutter
https://github.com/airblade/vim-gitgutter
This plugin adds a column to the left margin indicating lines changed in the active file since the last Git revision. As in other editors, this can be a useful bit of context during editing.
vim-gitgutter also lets you jump between changes and stage/discard individual hunks. Here are the default mappings:
nmap ]c <Plug>GitGutterNextHunk
nmap [c <Plug>GitGutterPrevHunk
nmap <Leader>hs <Plug>GitGutterStageHunk
nmap <Leader>hu <Plug>GitGutterUndoHunk
Installing Vim plugins
There are several to manage plugins Vim, including Pathogen, Vundle, and Vim 8’s native package loading. I recommend vim-plug, which can be installed using curl, or auto-installed in .vimrc:
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
With vim-plug, I create a ~/.vim/plugins.vim file and add a Plug line for each dependency to install, between the required plug#begin and plug#endcalls.
call plug#begin('~/.vim/plugged')Plug 'airblade/vim-gitgutter'
Plug 'editorconfig/editorconfig-vim'
Plug 'itchyny/lightline.vim'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'mattn/emmet-vim'
Plug 'scrooloose/nerdtree'
Plug 'terryma/vim-multiple-cursors'
Plug 'tpope/vim-eunuch'
Plug 'tpope/vim-surround'
Plug 'w0rp/ale'call plug#end()
Source this by adding the following statement to your .vimrc.
so ~/.vim/plugins.vim
Finally, launch Vim and run :PlugInstall.
Closing notes
These are just some of my picks for general-purpose Vim editing, and I hope most people who read this will find at least one useful thing. Feel free to comment if you think I missed anything! Update: I’ve made two substitutions thanks to great suggestions by @AntonK52 and @frioux — thanks guys.
Vim still isn’t quite my primary editor, but over a period of years I’ve slowly been using it more and more. Thanks to some looking around and great help from the community above, I’ve been able to significantly improve and personalise my Vim experience with each new setting and plugin. This also takes time. If you’ve read this article and want more, definitely explore the vast selection of other plugins out there for yourself — VimAwesome is the place to look.
