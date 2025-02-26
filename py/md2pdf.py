vim.command(':com! -nargs=* Md2PDF py3 md2pdf(<f-args>)')
vim.command(':com! -nargs=* Md2ODT py3 md2odt(<f-args>)')
#vim.command(':com! -nargs=* MrgCMD py3 mrgCMD(<f-args>)')
#vim.command('''command! Movebuf -nargs=* :wincmd c | call execute('tabnext ' . <f-args>[1]) | call execute('sbuffer ' . <f-args>[0]) ''')
#vim.api.create_autocmd("FileType", {
#  'desc':"python ft mappings",
#  #group = vim.api.create_augroup("pyMapping", { clear = true }),
#  'pattern':"python",
#  'callback':setfType, #function(opts)
#})
def md2odt(args, ext='.odt'):
  utfFont, CJKmainfont, pdfEngine='mainfont:URW Gothic', '華康魏碑體', 'xelatex'
  fname=vim.funcs.expand('%:p') #:h
  #fname=Path(fname)
  base, dmmy=splitext(fname)
  #base=fname.stem
  #fPrnt=fname.parent
  #Linux pandoc example.md -o example.pdf --latex-engine=xelatex --toc --from markdown --template eisvogel --listings
  #pandoc example.txt -o example_with_template.pdf --pdf-engine=xelatex --toc --toc-depth=4 --from markdown --template eisvogel --listings
  cmd=f"pandoc -f markdown -V CJKmainfont={CJKmainfont} -o {base}{ext} -V '{utfFont}' {fname}"
  print(cmd)
  system(cmd)

def md2pdf(args, ext='.pdf'):
  utfFont, CJKmainfont, pdfEngine='mainfont:URW Gothic', '華康魏碑體', 'xelatex'
  fname=vim.funcs.expand('%:p') #:h
  fname=Path(fname)
  base, dmmy=splitext(fname)
  #base=fname.stem
  #fPrnt=fname.parent
  #Linux pandoc example.md -o example.pdf --latex-engine=xelatex --toc --from markdown --template eisvogel --listings
  #pandoc example.txt -o example_with_template.pdf --pdf-engine=xelatex --toc --toc-depth=4 --from markdown --template eisvogel --listings
  cmd=f"pandoc -f markdown --pdf-engine={pdfEngine} -V CJKmainfont={CJKmainfont} -o {base}{ext} --toc -V '{utfFont}' {fname}"
  print(cmd)
  system(cmd)
  #cmd=f'htmlParser.py "{fname}">"{base}.raw"'
#autocmd FileType python setlocal shiftwidth=2 softtabstop=2 expandtab
#vim.api.set_keymap('n', '<leader>mpdf', '<cmd>py3 md2pdf<CR>', {'noremap':True, 'silent':False})  #'<cmd>
# -V colorlinks=true -V linkcolor=blue -V urlcolor=red -V toccolor=gray
vim.api.set_keymap('n', '<leader>mpdf', ':Md2PDF ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>modt', ':Md2ODT ', {'noremap':True, 'silent':False})
