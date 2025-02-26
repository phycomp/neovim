Vim與Python真乃天作之合：打造強大的Python開發環境 2018.05.27軟體開發工具ide, python, vimNO IMAGE
HOME軟體開發工具Vim與Python真乃天作之合：打造強大的Python開發環境 Advertisement 本文由程式設計派-EarlGrey翻譯，原文出自realpython，是Vim的愛好者專門針對利用Sublime Text 3設定Python IDE一文所寫。譯者本人也是依照Sublime Text那篇文章配置的開發環境，但一直對Vim作為神器的美名非常仰慕，又看到了一篇這麼全面的配置文章，覺得有必要翻譯過來與大家分享，想必可以省卻很多自己研究如何配置的時間。

我注意到，有人在realpython.com宣揚Sublime Text 3。作為公司的資深開發人員（呃，也就是老古董），我覺得有義務介紹一個真正的Python開發環境給大家——我要推薦的當然就是Vim了。不錯，Vim編輯器無處不在，速度快，從來不會崩潰。並且，它能做任何事情！

不過，不利之處也有，就是Vim配置起來很讓人頭疼。但是，別擔心，本文將告訴你如何配置一個強大的Vim環境，專門用於天天搗鼓Python開發。

下面是最終效果預覽。

Vim as Python IDE

如果想充分地利用好本文，你應該對如何使用Vim和它的命令模式至少有一個基本的瞭解。如果你是初學者，你可以通過vim-adventure或者openvim網站學習。在繼續閱讀本文之前，請花點時間瀏覽那兩個網站的內容。

目錄 
1. 安裝
1.1. OS X
1.2. Unix衍生系統
1.3. Windows
2. 驗證安裝
3. Vim擴充套件
3.1. Vundle
4. 開始打造IDE吧
4.1. 扔掉滑鼠
4.2. 分割佈局（Split Layouts）
4.3. 緩衝區（Buffers）
4.4. 程式碼摺疊（Code Folding）
4.5. Python程式碼縮排
4.6. 標示不必要的空白字元
4.7. 支援UTF-8編碼
4.8. 自動補全
4.9. 支援Virtualenv虛擬環境
4.10. 語法檢查/高亮
4.11. 配色方案
4.12. 檔案瀏覽
4.13. 超級搜尋
4.14. 顯示行號
4.15. Git整合
4.16. Powerline狀態列
4.17. 系統剪貼簿
4.18. Shell開啟Vim編輯模式
5. 結語
6. 資源
7. 網友評論精選
安裝
因為許多Unix衍生系統已經預裝了Vim，我們首先要確認編輯器是否成功安裝：

vim --version
如果已經安裝了，你應該看到類似下面的文字：

VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Nov  5 2014 21:00:28)
Compiled by root@apple.com
Normal version without GUI.  Features included ( ) or not (-):
-arabic  autocmd -balloon_eval -browse  builtin_terms  byte_offset  cindent
-clientserver -clipboard  cmdline_compl  cmdline_hist  cmdline_info  comments
-conceal  cryptv  cscope  cursorbind  cursorshape  dialog_con  diff  digraphs
-dnd -ebcdic -emacs_tags  eval  ex_extra  extra_search -farsi  file_in_path
find_in_path  float  folding -footer  fork() -gettext -hangul_input  iconv
insert_expand  jumplist -keymap -langmap  libcall  linebreak  lispindent
listcmds  localmap -lua  menu  mksession  modify_fname  mouse -mouseshape
-mouse_dec -mouse_gpm -mouse_jsbterm -mouse_netterm -mouse_sysmouse
mouse_xterm  multi_byte  multi_lang -mzscheme  netbeans_intg -osfiletype
path_extra -perl  persistent_undo  postscript  printer -profile  python/dyn
-python3  quickfix  reltime -rightleft  ruby/dyn  scrollbind  signs
smartindent -sniff  startuptime  statusline -sun_workshop  syntax  tag_binary
tag_old_static -tag_any_white -tcl  terminfo  termresponse  textobjects  title
-toolbar  user_commands  vertsplit  virtualedit  visual  visualextra  viminfo
vreplace  wildignore  wildmenu  windows  writebackup -X11 -xfontset -xim -xsmp
-xterm_clipboard -xterm_save
system vimrc file: "$VIM/vimrc"
user vimrc file: "$HOME/.vimrc"
user exrc file: "$HOME/.exrc"
fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -D_FORTIFY_SOURCE=0 -Iproto -DHAVE_CONFIG_H -arch i386 -arch x86_64 -g -Os -pipe
Linking: gcc -arch i386 -arch x86_64 -o vim -lncurses
在這一步，你要確保已經滿足以下兩點要求：

Vim編輯版本應該大於7.3。
支援Python語言。在所選編輯器的功能中，確保你看到了 python。
如果滿足上述要求，接下來可以安裝Vim擴充套件了。如果不滿足，則需要安裝/升級。

OS X 如果沒有Homebrew，建議馬上安裝，並執行：brew update
brew install vim
Unix衍生系統
Debian或Ubuntu系統，可以使用下面的程式碼：

sudo apt-get remove vim-tiny
apt-get update
apt-get install vim
如果是其他版本的Linux系統，請查閱相應版本包管理器的文件。不清楚的話，可以先閱讀這篇文章：安裝Vim

Windows Windows系統下安裝Vim有很多種方法。請查閱官方文件。驗證安裝 確保你已經安裝了7.3版本以上、支援Python的Vim編輯器。你可以再次執行vim --version進行確認。如果你想知道Vim中使用的Python版本，你可以在編輯器中執行:python import sys; print(sys.version)。

2.7.6 (default, Sep  9 2014, 15:04:36)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.39)]
這行命令會輸出你的編輯器當前的Python版本。如果報錯，那麼你的編輯器就不支援Python語言，需要重灌或重新編譯。

Vim編輯器安裝完成後，我們來看看如何將其設定為Python開發的強大環境。

Vim擴充套件
Vim本身能夠滿足開發人員的很多需求，但是它的可擴充套件性也極強，並且已經有一些殺手級的擴充套件，可以讓Vim擁有“現代”整合開發環境的特性。所以，你所需要的第一件東西就是一個好用的擴充套件管理器。

Vim的擴充套件通常也被成為bundle或外掛。

Vundle Vim有多個擴充套件管理器，但是我們強烈推薦Vundle。你可以把它想象成Vim的pip。有了Vundle，安裝和更新包這種事情不費吹灰之力。

我們現在來安裝Vundle：
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
該命令將下載Vundle外掛管理器，並將它放置在你的Vim編輯器bundles資料夾中。現在，你可以通過.vimrc配置檔案來管理所有擴充套件了。

將配置檔案新增到你的使用者的home資料夾中：touch ~/.vimrc
接下來，把下來的Vundle配置新增到配置檔案的頂部：

set nocompatible              " required
filetype off                  " required
" set the runtime path to include Vundle and initialize
set rtp =~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
這樣，你就完成了使用Vundle前的設定。之後，你就可以在配置檔案中新增希望安裝的外掛，然後開啟Vim編輯器，執行下面的命令：

:PluginInstall
這個命令告訴Vundle施展它的魔法——自動下載所有的外掛，併為你進行安裝和更新。
vim PluginInstall image
對於Windows使用者，請查閱Windows安裝指南。

開始打造IDE吧 本文不可能列舉Vim的全部功能，只能快速介紹一些Vim自帶的強大功能，它們對於Python開發來說是非常有用的。
扔掉滑鼠 或許，Vim編輯器最重要的功能就是它不要求使用滑鼠（除了GUI版本外）。一開始，你可能會覺得這是個非常糟糕的做法，但是隻要你投入時間——是的，這很花時間——學習快捷組合鍵，就可以大幅提升工作流的速度。

分割佈局（Split Layouts）
Split layout of vim

使用:sv <filename>命令開啟一個檔案，你可以縱向分割佈局（新檔案會在當前檔案下方介面開啟），使用相反的命令:vs <filename>， 你可以得到橫向分割佈局（新檔案會在當前檔案右側介面開啟）。

你還可以巢狀分割佈局，所以你可以在分割佈局內容再進行分割，縱向或橫向都可以，直到你滿意為止。眾所周知，我們開發時經常需要同時檢視多個檔案。
專業貼士：記得在輸入完:sv後，利用tab補全功能，快速查詢檔案。
專業貼士：你還可以指定螢幕上可以進行分割佈局的區域，只要在.vimrc檔案中新增下面的程式碼即可：
set splitbelow
set splitright
專業貼士：想要不使用滑鼠就切換分割佈局嗎？只要將下面的程式碼新增到.vimrc檔案中，你就可以通過快捷組合鍵進行切換。

"split navigations
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
組合快捷鍵：

Ctrl-j 切換到下方的分割視窗

Ctrl-k 切換到上方的分割視窗
Ctrl-l 切換到右側的分割視窗
Ctrl-h 切換到左側的分割視窗

換句話說, 按Ctrl Vim的標準移動鍵，就可以切換到指定視窗。
等等，nnoremap是什麼意思？——簡單來說，nnoremap將一個組合快捷鍵對映為另一個快捷鍵。一開始的n，指的是在Vim的正常模式（Normal Mode）下，而不是可視模式下重新對映。基本上，nnoremap <C-J> <C-W><C-j>就是說，當我在正常模式按下<C-J>時，進行<C-W><C-j>操作。更多資訊請看這裡。

緩衝區（Buffers）
雖然Vim支援tab操作，仍有很多人更喜歡緩衝區和分割佈局。你可以把緩衝區想象成最近開啟的一個檔案。Vim提供了方便訪問近期緩衝區的方式，只需要輸入:b <buffer name or number>，就可以切換到一個已經開啟的緩衝區（此處也可使用自動補全功能）。你還可以通過ls命令檢視所有的緩衝區。
專業貼士: 在:ls命令輸出的最後，Vim會提示“敲擊Enter繼續檢視”，這時你可以直接輸入:b <buffer name>，立即選擇緩衝區。這樣可以省掉一個按鍵操作，也不必去記憶緩衝區的名字。

程式碼摺疊（Code Folding）
大多數“現代”整合開發環境（IDE）都提供對方法（methods）或類（classes）進行摺疊的手段，只顯示類或方法的定義部分，而不是全部的程式碼。
你可以在.vimrc中新增下面的程式碼開啟該功能：
" Enable folding
set foldmethod=indent
set foldlevel=99
這樣就可以實現，但是你必須手動輸入za來摺疊（和取消折疊）。使用空格鍵會是更好的選擇。所以在你的配置檔案中加上這一行命令吧：

" Enable folding with the spacebar
nnoremap <space> za
現在你可以輕鬆地隱藏掉那些當前工作時不需要關注的程式碼了。

第一個命令，set foldmethod=ident會根據每行的縮排開啟摺疊。但是這樣做會出現超過你所希望的摺疊數目。但是別怕，有幾個擴充套件就是專門解決這個問題的。在這裡，我們推薦SimplyFold。在.vimrc中加入下面這行程式碼，通過Vundle進行安裝：

Plugin 'tmhedberg/SimpylFold'
不要忘記執行安裝命令：:PluginInstall
專業貼士: 希望看到摺疊程式碼的文件字串？
let g:SimpylFold_docstring_preview=1
Python程式碼縮排
當然，想要程式碼摺疊功能根據縮排情況正常工作，那麼你就會希望自己的縮排是正確的。這裡，Vim的自帶功能無法滿足，因為它實現不了定義函式之後的自動縮排。我們希望Vim中的縮排能做到以下兩點：
首先，縮排要符合PEP8標準。
其次，更好地處理自動縮排。

PEP8 要支援PEP8風格的縮排，請在.vimrc檔案中新增下面的程式碼：

au BufNewFile,BufRead *.py
\ set tabstop=4
\ set softtabstop=4
\ set shiftwidth=4
\ set textwidth=79
\ set expandtab
\ set autoindent
\ set fileformat=unix
這些設定將讓Vim中的Tab鍵就相當於4個標準的空格符，確保每行程式碼長度不超過80個字元，並且會以unix格式儲存檔案，避免在推送到Github或分享給其他使用者時出現檔案轉換問題。

另外，對於全棧開發，你可以設定針對每種檔案型別設定au命令：

au BufNewFile,BufRead *.js, *.html, *.css
\ set tabstop=2
\ set softtabstop=2
\ set shiftwidth=2
自動縮排

自動縮排有用，但是在某些情況下（比如函式定義有多行的時候），並不總是會達到你想要的效果，尤其是在符合PEP8標準方面。我們可以利用indentpython.vim外掛，來解決這個問題：

Plugin 'vim-scripts/indentpython.vim'
標示不必要的空白字元
我們希望避免出現多餘的空白字元。可以讓Vim幫我們標示出來，使其很容易發現並刪除。

au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\ $/
這會將多餘的空白字元標示出來，很可能會將它們變成紅色突出。

支援UTF-8編碼
大部分情況下，進行Python開發時你應該使用UTF-8編碼，尤其是使用Python 3的時候。確保Vim設定檔案中有下面的命令：

set encoding=utf-8
自動補全
支援Python自動補全的最好外掛是YouCompleteMe。我們再次使用Vundle安裝：

Bundle 'Valloric/YouCompleteMe'
YouCompleteMe外掛其實底層使用了一些不同的自動補全元件（包括針對Python開發的Jedi），另外要安裝一些C庫才能正常工作。外掛官方文件提供了很好的安裝指南，我就不在這裡重複了。切記跟隨文件的步驟進行安裝。

安裝完成後，外掛自帶的設定效果就很好，但是我們還可以進行一些小的調整：

let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
上面的第一行確保了在你完成操作之後，自動補全視窗不會消失，第二行則定義了“轉到定義”的快捷方式。

支援Virtualenv虛擬環境
上面“轉到定義”功能的一個問題，就是預設情況下Vim不知道virtualenv虛擬環境的情況，所以你必須在配置檔案中新增下面的程式碼，使得Vim和YouCompleteMe能夠發現你的虛擬環境：

"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
project_base_dir = os.environ['VIRTUAL_ENV']
activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
EOF
這段程式碼會判斷你目前是否在虛擬環境中編輯，然後切換到相應的虛擬環境，並設定好你的系統路徑，確保YouCompleteMe能夠找到相應的site packages資料夾。

語法檢查/高亮
通過安裝syntastic外掛，每次儲存檔案時Vim都會檢查程式碼的語法：

Plugin 'scrooloose/syntastic'
還可以通過這個小巧的外掛，新增PEP8程式碼風格檢查：

Plugin 'nvie/vim-flake8'
最後，讓你的程式碼變得更漂亮：

let python_highlight_all=1
syntax on
配色方案
配色方案可以和你正在使用的基礎配色共同使用。GUI模式可以嘗試solarized方案, 終端模式可以嘗試Zenburn方案：

Plugin 'jnurmine/Zenburn'
Plugin 'altercation/vim-colors-solarized'
接下來，只需要新增一點邏輯判斷，確定什麼模式下使用何種方案就可以了：


if has('gui_running')
set background=dark
colorscheme solarized
else
colorscheme Zenburn
endif
Solarized方案同時提供了暗色調和輕色調兩種主題。要支援切換主題功能（按F5）也非常簡單，只需新增：

call togglebg#map("<F5>")
檔案瀏覽
如果你想要一個不錯的檔案樹形結構，那麼NERDTree是不二之選。

Plugin 'scrooloose/nerdtree'
如果你想用tab鍵，可以利用vim-nerdtree-tabs外掛實現：


Plugin 'jistr/vim-nerdtree-tabs'
還想隱藏.pyc檔案？那麼再新增下面這行程式碼吧：

let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
超級搜尋
想要在Vim中搜尋任何檔案？試試ctrlP外掛吧：

Plugin 'kien/ctrlp.vim'
正如外掛名，按Ctrl P就可以進行搜尋。如果你的檢索詞與想要查詢的檔案相匹配的話，這個外掛就會幫你找到它。哦，對了——它不僅僅可以搜尋檔案，還能檢索標籤！更多資訊，可以觀看這個Youtube視訊.

顯示行號
開啟顯示行號：

set nu
Git整合
想要在Vim中執行基本的Git命令？vim-fugitive外掛則是不二之選。

Plugin 'tpope/vim-fugitive'
git integration in vim

請看Vimcasts的這部視訊，瞭解更多情況。

Powerline狀態列
Powerline是一個狀態列外掛，可以顯示當前的虛擬環境、Git分支、正在編輯的檔案等資訊。

這個外掛是用Python編寫的，支援諸如zsh、bash、tmux和IPython等多種環境。

Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
請查閱外掛的官方文件，瞭解配置選項。

系統剪貼簿
通常Vim會忽視系統剪貼簿，而使用自帶的剪貼簿。但是有時候你想從Vim之外的程式中剪下、複製、貼上文字。在OS X平臺上，你可以通過這行程式碼訪問你的系統剪貼簿：

set clipboard=unnamed
Shell開啟Vim編輯模式
最後，當你熟練掌握了Vim和它的鍵盤快捷方式之後，你會發現自己經常因為shell中缺乏相同的快捷鍵而懊惱。沒關係，大部分的shell程式都有Vi模式。在當前shell中開啟Vi模式，你只需要在~/.inputrc檔案中新增這行程式碼：

set editing-mode vi
現在，你不僅可以在shell中使用Vim組合快捷鍵，還可以在Python直譯器以及任何利用GNU Readline程式的工具（例如，大多數的資料庫shell）中使用。現在，你在什麼地方都可以使用Vim啦！

結語
Vim的設定到這裡就差不多了（至少對於Python開發來說是這樣的）。當然，開源世界裡還有大量你可以使用的其他擴充套件，以及本文中所提到外掛的替代品。你最喜愛的擴充套件是什麼？你又是如何將Vim設定符合你喜好的？

這是我本人的Vim配置檔案連結。你有沒有自己的設定程式碼？請與我們分享！

謝謝！

資源
Vim Tutor是Vim自帶的程式，安裝結束之後，只要在命令列輸入vimtutor即可，程式將會用Vim編輯器教你如何使用Vim。

Vimcasts是一系列的高階視訊教程，內容涉及許多Vim的功能。

Vim官方文件

Open Vim

笨辦法學Vimscript是學習vimscript的極好材料。

全文結束

網友評論精選
譯者也按照本文的步驟，在Vagrant虛擬機器上嘗試了Vim設定，但是可惜在YouCompleteMe外掛那遇到了些問題，沒有繼續配置下去。在原文頁，我也發現一些網友留言，說根據本文的建議進行了設定，但是碰到了問題。最後，譯者從中摘取了部分，供大家參考。

Wei-Hao Lin

The commands in “Python Indentation” keep throwing “e518: unknown option: set”, so i altered it and it works fine as following:

au BufNewFile,BufRead *.py
\ set tabstop=4 |
\ set softtabstop=4 |
\ set shiftwidth=4 |
\ set textwidth=79 |
\ set expandtab |
\ set autoindent |
\ set fileformat=unix |
au BufNewFile,BufRead *.js,*.html,*.css
\ set tabstop=2 |
\ set softtabstop=2 |
\ set shiftwidth=2 |
Konstantin Gagarin

change powerline to airlineand add powerline fonts.

Ruslan Kiianchuk

It seems like the hack with Python virtualenv can be solved with plugin without the need to pollute vimrc with Python code: https://github.com/jmcantrell/vim-virtualenv
