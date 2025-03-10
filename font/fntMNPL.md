" Autoload portion of plugin/fontsize.vim.

if exists("autoloaded_fontsize")
    finish
endif
let autoloaded_fontsize = 1

" Font examples from http://vim.wikia.com/wiki/VimTip632

" Regex values for each platform split guifont into three
" sections (\1, \2, and \3 in capturing parentheses):
"
" - prefix
" - size (possibly fractional)
" - suffix (possibly including extra fonts after commas)

" gui_gtk2: Courier\ New\ 11
let fontsize#regex_gtk2 = '\(.\{-} \)\(\d\+\)\(.*\)'

" gui_photon: Courier\ New:s11
let fontsize#regex_photon = '\(.\{-}:s\)\(\d\+\)\(.*\)'

" gui_kde: Courier\ New/11/-1/5/50/0/0/0/1/0
let fontsize#regex_kde = '\(.\{-}\/\)\(\d\+\)\(.*\)'

" gui_x11: -*-courier-medium-r-normal-*-*-180-*-*-m-*-*
" TODO For now, just taking the first string of digits.
let fontsize#regex_x11 = '\(.\{-}-\)\(\d\+\)\(.*\)'

" gui_other: Courier_New:h11:cDEFAULT
let fontsize#regex_other = '\(.\{-}:h\)\(\d\+\)\(.*\)'

if has("gui_gtk2") || has("gui_gtk3")
    let s:regex = fontsize#regex_gtk2
elseif has("gui_photon")
    let s:regex = fontsize#regex_photon
elseif has("gui_kde")
    let s:regex = fontsize#regex_kde
elseif has("x11")
    let s:regex = fontsize#regex_x11
else
    let s:regex = fontsize#regex_other
endif

function! fontsize#getFontName()
    " On Neovim, `getfontname()` always returns the empty string; however,
    " Neovim GUIs seem to support the 'guifont' option.  Unlike Gvim (which
    " supports multiple comma-separated fonts in 'guifont'), Neovim GUIs seem
    " to support only a single font in 'guifont'.  Try `getfontname()` first to
    " handle the Gvim cases smoothly (such as when 'guifont' is empty, or
    " contains multiple fonts, or contains an invalid font), but fall back to
    " using 'guifont' directly if `getfontname()` returns the empty string.
    let fontName = getfontname()
    if fontName == ''
        let fontName = &guifont
    endif
    return fontName
endfunction

function! fontsize#setFontName(fontName)
    " `nvim-qt` has a `GuiFont(fontName, force)` function for changing the font.
    " Though `nvim-qt` also seems to support assigning to the 'guifont'
    " option, this causes various warnings and bad behavior for some fonts
    " (notably "Hack" and "Consolas"), such as:
    "   Warning: Font "Hack" reports bad fixed pitch metrics
    " Without the `force=1` argument, the `GuiFont()` function generates the
    " same warnings.
    " `neovide` lacks a `GuiFont()` function, but it seems well behaved when
    " changing the font by assigning to the 'guifont' option.
    if exists('*GuiFont')
        call GuiFont(a:fontName, 1)
    else
        let &guifont = a:fontName
    endif
endfunction

function! fontsize#setFontNameWide(fontName)
    " NOTE: `GuiFont()` doesn't work for the 'guifontwide' option.
    let &guifontwide = a:fontName
endfunction

function! fontsize#encodeFont(font)
    if has("iconv") && exists("g:fontsize#encoding")
        let encodedFont = iconv(a:font, &enc, g:fontsize#encoding)
    else
        let encodedFont = a:font
    endif
    return encodedFont
endfunction

function! fontsize#decodeFont(font)
    if has("iconv") && exists("g:fontsize#encoding")
        let decodedFont = iconv(a:font, g:fontsize#encoding, &enc)
    else
        let decodedFont = a:font
    endif
    return decodedFont
endfunction

function! fontsize#getSize(font)
    let decodedFont = fontsize#decodeFont(a:font)
    if match(decodedFont, s:regex) != -1
        " Add zero to convert to integer.
        let size = 0 + substitute(decodedFont, s:regex, '\2', '')
    else
        let size = 0
    endif
    return size
endfunction

function! fontsize#setSize(font, size)
    let decodedFont = fontsize#decodeFont(a:font)
    if match(decodedFont, s:regex) != -1
        let newFont = substitute(decodedFont, s:regex, '\1' . a:size . '\3', '')
    else
        let newFont = decodedFont
    endif
    return fontsize#encodeFont(newFont)
endfunction

function! fontsize#fontString(font)
    let fontName = fontsize#decodeFont(a:font)
    if len(fontName) == 0
        let fontName = "(Empty)"
        let fontSize = 0
    else
        let fontSize = fontsize#getSize(fontName)
    endif
    let maxFontLen = 50
    if len(fontName) > maxFontLen
        let fontName = fontName[:maxFontLen - 4] . "..."
    endif
    if fontSize == 0
        let fontString = "??: " . fontName
    else
        let fontString = fontSize . ": " . fontName
    endif
    return fontString
endfunction

function! fontsize#display()
    redraw
    sleep 100m
    echo fontsize#fontString(fontsize#getFontName()) . " (+/= - 0 ! q CR SP)"
endfunction

function! fontsize#ensureDefault()
    if !exists("g:fontsize#defaultSize")
        let g:fontsize#defaultSize = 0
    endif
    if g:fontsize#defaultSize == 0
        let g:fontsize#defaultSize = fontsize#getSize(fontsize#getFontName())
    endif
endfunction

" True when options have already been setup.
let g:fontsize#optionsActive = 0

function! fontsize#setupOptions()
    if g:fontsize#optionsActive
        return
    endif
    let g:fontsize#optionsActive = 1
    let g:fontsize#original_timeout = &timeout
    let g:fontsize#original_timeoutlen = &timeoutlen
    let g:fontsize#original_ttimeout = &ttimeout
    let g:fontsize#original_ttimeoutlen = &ttimeoutlen

    let mappingTimeout = &timeout
    let mappingTimeoutMsec = &timeoutlen
    let keyCodeTimeout = &timeout || &ttimeout
    let keyCodeTimeoutMsec = &ttimeoutlen < 0 ?  &timeoutlen : &ttimeoutlen

    if exists("g:fontsize#timeout")
        let modeTimeout = g:fontsize#timeout
    else
        let modeTimeout = &timeout
    endif
    if exists("g:fontsize#timeoutlen")
        let modeTimeoutMsec = g:fontsize#timeoutlen
    else
        let modeTimeoutMsec = &timeoutlen
    endif

    " In the worst case, the user had no keyCodeTimeout, but he wants "font
    " size" mode to timeout.  This means we have to enable a mapping timeout
    " which has the unfortunate side-effect of turning on the keyCodeTimeout.
    " The best we can do is make a long keyCodeTimeoutMsec in this case.
    if !keyCodeTimeout
        let keyCodeTimeoutMsec = 10000
    endif

    " Apply the user's effective keyCodeTimeout settings.
    let &ttimeoutlen = keyCodeTimeoutMsec
    let &ttimeout = keyCodeTimeout

    " To avoid any hint of a race condition, change 'timeoutlen' only if
    " we are going to enable timeouts.
    if modeTimeout
        let &timeoutlen = modeTimeoutMsec
    endif
    let &timeout = modeTimeout
endfunction

function! fontsize#restoreOptions()
    if !g:fontsize#optionsActive
        return
    endif
    let &timeout = g:fontsize#original_timeout
    let &timeoutlen = g:fontsize#original_timeoutlen
    let &ttimeout = g:fontsize#original_ttimeout
    let &ttimeoutlen = g:fontsize#original_ttimeoutlen
    let g:fontsize#optionsActive = 0
endfunction

function! fontsize#begin()
    call fontsize#setupOptions()
    call fontsize#display()
endfunction

function! fontsize#quit()
    echo fontsize#fontString(fontsize#getFontName()) . " (Done)"
    call fontsize#restoreOptions()
endfunction

function! fontsize#default()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    call fontsize#setFontName(
            \ fontsize#setSize(fontsize#getFontName(), g:fontsize#defaultSize))
    call fontsize#setFontNameWide(
            \ fontsize#setSize(&guifontwide, g:fontsize#defaultSize))
    call fontsize#display()
endfunction

function! fontsize#setDefault()
    call fontsize#setupOptions()
    let g:fontsize#defaultSize = fontsize#getSize(fontsize#getFontName())
endfunction

function! fontsize#inc()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    let newSize = fontsize#getSize(fontsize#getFontName()) + v:count1
    call fontsize#setFontName(fontsize#setSize(fontsize#getFontName(), newSize))
    call fontsize#setFontNameWide(
            \ fontsize#setSize(&guifontwide, newSize))
    call fontsize#display()
endfunction

function! fontsize#dec()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    let newSize = fontsize#getSize(fontsize#getFontName()) - v:count1
    if newSize > 0
        call fontsize#setFontName(
                \ fontsize#setSize(fontsize#getFontName(), newSize))
            call fontsize#setFontNameWide(
                    \ fontsize#setSize(&guifontwide, newSize))
    endif
    call fontsize#display()
endfunction

" vim: sts=4 sw=4 tw=80 et ai:
**************************************  keyMap  ******************************
" Autoload portion of plugin/fontsize.vim.

if exists("autoloaded_fontsize")
    finish
endif
let autoloaded_fontsize = 1

" Font examples from http://vim.wikia.com/wiki/VimTip632

" Regex values for each platform split guifont into three
" sections (\1, \2, and \3 in capturing parentheses):
"
" - prefix
" - size (possibly fractional)
" - suffix (possibly including extra fonts after commas)

" gui_gtk2: Courier\ New\ 11
let fontsize#regex_gtk2 = '\(.\{-} \)\(\d\+\)\(.*\)'

" gui_photon: Courier\ New:s11
let fontsize#regex_photon = '\(.\{-}:s\)\(\d\+\)\(.*\)'

" gui_kde: Courier\ New/11/-1/5/50/0/0/0/1/0
let fontsize#regex_kde = '\(.\{-}\/\)\(\d\+\)\(.*\)'

" gui_x11: -*-courier-medium-r-normal-*-*-180-*-*-m-*-*
" TODO For now, just taking the first string of digits.
let fontsize#regex_x11 = '\(.\{-}-\)\(\d\+\)\(.*\)'

" gui_other: Courier_New:h11:cDEFAULT
let fontsize#regex_other = '\(.\{-}:h\)\(\d\+\)\(.*\)'

if has("gui_gtk2") || has("gui_gtk3")
    let s:regex = fontsize#regex_gtk2
elseif has("gui_photon")
    let s:regex = fontsize#regex_photon
elseif has("gui_kde")
    let s:regex = fontsize#regex_kde
elseif has("x11")
    let s:regex = fontsize#regex_x11
else
    let s:regex = fontsize#regex_other
endif

function! fontsize#getFontName()
    " On Neovim, `getfontname()` always returns the empty string; however,
    " Neovim GUIs seem to support the 'guifont' option.  Unlike Gvim (which
    " supports multiple comma-separated fonts in 'guifont'), Neovim GUIs seem
    " to support only a single font in 'guifont'.  Try `getfontname()` first to
    " handle the Gvim cases smoothly (such as when 'guifont' is empty, or
    " contains multiple fonts, or contains an invalid font), but fall back to
    " using 'guifont' directly if `getfontname()` returns the empty string.
    let fontName = getfontname()
    if fontName == ''
        let fontName = &guifont
    endif
    return fontName
endfunction

function! fontsize#setFontName(fontName)
    " `nvim-qt` has a `GuiFont(fontName, force)` function for changing the font.
    " Though `nvim-qt` also seems to support assigning to the 'guifont'
    " option, this causes various warnings and bad behavior for some fonts
    " (notably "Hack" and "Consolas"), such as:
    "   Warning: Font "Hack" reports bad fixed pitch metrics
    " Without the `force=1` argument, the `GuiFont()` function generates the
    " same warnings.
    " `neovide` lacks a `GuiFont()` function, but it seems well behaved when
    " changing the font by assigning to the 'guifont' option.
    if exists('*GuiFont')
        call GuiFont(a:fontName, 1)
    else
        let &guifont = a:fontName
    endif
endfunction

function! fontsize#setFontNameWide(fontName)
    " NOTE: `GuiFont()` doesn't work for the 'guifontwide' option.
    let &guifontwide = a:fontName
endfunction

function! fontsize#encodeFont(font)
    if has("iconv") && exists("g:fontsize#encoding")
        let encodedFont = iconv(a:font, &enc, g:fontsize#encoding)
    else
        let encodedFont = a:font
    endif
    return encodedFont
endfunction

function! fontsize#decodeFont(font)
    if has("iconv") && exists("g:fontsize#encoding")
        let decodedFont = iconv(a:font, g:fontsize#encoding, &enc)
    else
        let decodedFont = a:font
    endif
    return decodedFont
endfunction

function! fontsize#getSize(font)
    let decodedFont = fontsize#decodeFont(a:font)
    if match(decodedFont, s:regex) != -1
        " Add zero to convert to integer.
        let size = 0 + substitute(decodedFont, s:regex, '\2', '')
    else
        let size = 0
    endif
    return size
endfunction

function! fontsize#setSize(font, size)
    let decodedFont = fontsize#decodeFont(a:font)
    if match(decodedFont, s:regex) != -1
        let newFont = substitute(decodedFont, s:regex, '\1' . a:size . '\3', '')
    else
        let newFont = decodedFont
    endif
    return fontsize#encodeFont(newFont)
endfunction

function! fontsize#fontString(font)
    let fontName = fontsize#decodeFont(a:font)
    if len(fontName) == 0
        let fontName = "(Empty)"
        let fontSize = 0
    else
        let fontSize = fontsize#getSize(fontName)
    endif
    let maxFontLen = 50
    if len(fontName) > maxFontLen
        let fontName = fontName[:maxFontLen - 4] . "..."
    endif
    if fontSize == 0
        let fontString = "??: " . fontName
    else
        let fontString = fontSize . ": " . fontName
    endif
    return fontString
endfunction

function! fontsize#display()
    redraw
    sleep 100m
    echo fontsize#fontString(fontsize#getFontName()) . " (+/= - 0 ! q CR SP)"
endfunction

function! fontsize#ensureDefault()
    if !exists("g:fontsize#defaultSize")
        let g:fontsize#defaultSize = 0
    endif
    if g:fontsize#defaultSize == 0
        let g:fontsize#defaultSize = fontsize#getSize(fontsize#getFontName())
    endif
endfunction

" True when options have already been setup.
let g:fontsize#optionsActive = 0

function! fontsize#setupOptions()
    if g:fontsize#optionsActive
        return
    endif
    let g:fontsize#optionsActive = 1
    let g:fontsize#original_timeout = &timeout
    let g:fontsize#original_timeoutlen = &timeoutlen
    let g:fontsize#original_ttimeout = &ttimeout
    let g:fontsize#original_ttimeoutlen = &ttimeoutlen

    let mappingTimeout = &timeout
    let mappingTimeoutMsec = &timeoutlen
    let keyCodeTimeout = &timeout || &ttimeout
    let keyCodeTimeoutMsec = &ttimeoutlen < 0 ?  &timeoutlen : &ttimeoutlen

    if exists("g:fontsize#timeout")
        let modeTimeout = g:fontsize#timeout
    else
        let modeTimeout = &timeout
    endif
    if exists("g:fontsize#timeoutlen")
        let modeTimeoutMsec = g:fontsize#timeoutlen
    else
        let modeTimeoutMsec = &timeoutlen
    endif

    " In the worst case, the user had no keyCodeTimeout, but he wants "font
    " size" mode to timeout.  This means we have to enable a mapping timeout
    " which has the unfortunate side-effect of turning on the keyCodeTimeout.
    " The best we can do is make a long keyCodeTimeoutMsec in this case.
    if !keyCodeTimeout
        let keyCodeTimeoutMsec = 10000
    endif

    " Apply the user's effective keyCodeTimeout settings.
    let &ttimeoutlen = keyCodeTimeoutMsec
    let &ttimeout = keyCodeTimeout

    " To avoid any hint of a race condition, change 'timeoutlen' only if
    " we are going to enable timeouts.
    if modeTimeout
        let &timeoutlen = modeTimeoutMsec
    endif
    let &timeout = modeTimeout
endfunction

function! fontsize#restoreOptions()
    if !g:fontsize#optionsActive
        return
    endif
    let &timeout = g:fontsize#original_timeout
    let &timeoutlen = g:fontsize#original_timeoutlen
    let &ttimeout = g:fontsize#original_ttimeout
    let &ttimeoutlen = g:fontsize#original_ttimeoutlen
    let g:fontsize#optionsActive = 0
endfunction

function! fontsize#begin()
    call fontsize#setupOptions()
    call fontsize#display()
endfunction

function! fontsize#quit()
    echo fontsize#fontString(fontsize#getFontName()) . " (Done)"
    call fontsize#restoreOptions()
endfunction

function! fontsize#default()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    call fontsize#setFontName(
            \ fontsize#setSize(fontsize#getFontName(), g:fontsize#defaultSize))
    call fontsize#setFontNameWide(
            \ fontsize#setSize(&guifontwide, g:fontsize#defaultSize))
    call fontsize#display()
endfunction

function! fontsize#setDefault()
    call fontsize#setupOptions()
    let g:fontsize#defaultSize = fontsize#getSize(fontsize#getFontName())
endfunction

function! fontsize#inc()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    let newSize = fontsize#getSize(fontsize#getFontName()) + v:count1
    call fontsize#setFontName(fontsize#setSize(fontsize#getFontName(), newSize))
    call fontsize#setFontNameWide(
            \ fontsize#setSize(&guifontwide, newSize))
    call fontsize#display()
endfunction

function! fontsize#dec()
    call fontsize#setupOptions()
    call fontsize#ensureDefault()
    let newSize = fontsize#getSize(fontsize#getFontName()) - v:count1
    if newSize > 0
        call fontsize#setFontName(
                \ fontsize#setSize(fontsize#getFontName(), newSize))
            call fontsize#setFontNameWide(
                    \ fontsize#setSize(&guifontwide, newSize))
    endif
    call fontsize#display()
endfunction

" vim: sts=4 sw=4 tw=80 et ai:
(ljbeauty-py3.13) [josh@α10.221.252.12 sof]cat fntSizeKeymap.vim
" Plugin for modifying guifont size.

" Note that Neovim always returns false for `has('gui')`, but
" `has('gui_running')` returns true for Neovim GUIs (at least for
" `nvim-qt` and `neovide`).
if exists("loaded_fontsize") || !has('gui_running')
    finish
endif
let loaded_fontsize = 1

" Save 'cpoptions' and set Vim default to enable line continuations.
let s:save_cpoptions = &cpoptions
set cpoptions&vim

if !hasmapto("<Plug>FontsizeBegin")
    nmap <silent> <Leader><Leader>=  <Plug>FontsizeBegin
endif

if !hasmapto("<Plug>FontsizeInc", "n")
    nmap <silent> <Leader><Leader>+  <Plug>FontsizeInc
endif

if !hasmapto("<Plug>FontsizeDec", "n")
    nmap <silent> <Leader><Leader>-  <Plug>FontsizeDec
endif

if !hasmapto("<Plug>FontsizeDefault", "n")
    nmap <silent> <Leader><Leader>0  <Plug>FontsizeDefault
endif

" "font size" mode mappings are inspired by the bufmru.vim plugin.
" The concept is to enter a "mode" via an initial mapping.  Once
" in this mode, some mode-specific keystrokes now behave as if they
" were mapped.  When time-outs are enabled (see g:fontsize_timeout), the
" new "mode" times out and the new "mappings" are effectively turned off.
"
" This emulation of a "mode" is accomplished via a clever techinque
" wherein each operation terminates with a partial mapping to <SID>(fontsize).
" Each new keystroke completes a mapping that itself terminates with
" <SID>(fontsize), keeping an extensible chain of mappings going as long as
" they arrive before g:fontsize_timeoutlen milliseconds elapses between
" keystrokes.  The string "(fontsize)" is chosen to take the entire ten
" characters of space available for Vim's 'showcmd' option.  It provides better
" visual appearance than <SID>m_, which comes out looking something like
" 80>yR91_m_.

" Externally mappable mappings to internal mappings.
nmap <silent> <Plug>FontsizeBegin       <SID>begin<SID>(fontsize)
nmap <silent> <Plug>FontsizeInc         <SID>inc<SID>(fontsize)
nmap <silent> <Plug>FontsizeDec         <SID>dec<SID>(fontsize)
nmap <silent> <Plug>FontsizeDefault     <SID>default<SID>(fontsize)
nmap <silent> <Plug>FontsizeSetDefault  <SID>setDefault<SID>(fontsize)
nmap <silent> <Plug>FontsizeQuit        <SID>quit

" "Font size" mode mappings.  (fontsize)<KEY> maps <KEY> in "font size" mode.
nmap <silent> <SID>(fontsize)+        <SID>inc<SID>(fontsize)
nmap <silent> <SID>(fontsize)=        <SID>inc<SID>(fontsize)
nmap <silent> <SID>(fontsize)-        <SID>dec<SID>(fontsize)
nmap <silent> <SID>(fontsize)0        <SID>default<SID>(fontsize)
nmap <silent> <SID>(fontsize)!        <SID>setDefault<SID>(fontsize)
nmap <silent> <SID>(fontsize)q        <SID>quit
nmap <silent> <SID>(fontsize)<SPACE>  <SID>quit
nmap <silent> <SID>(fontsize)<CR>     <SID>quit
nmap <silent> <SID>(fontsize)         <SID>quit

" Action mappings.
nnoremap <silent> <SID>begin       :<C-u>call fontsize#begin()<CR>
nnoremap <silent> <SID>inc         :<C-u>call fontsize#inc()<CR>
nnoremap <silent> <SID>dec         :<C-u>call fontsize#dec()<CR>
nnoremap <silent> <SID>default     :<C-u>call fontsize#default()<CR>
nnoremap <silent> <SID>setDefault  :<C-u>call fontsize#setDefault()<CR>
nnoremap <silent> <SID>quit        :<C-u>call fontsize#quit()<CR>

" Restore saved 'cpoptions'.
let &cpoptions = s:save_cpoptions
" vim: sts=4 sw=4 tw=80 et ai:
