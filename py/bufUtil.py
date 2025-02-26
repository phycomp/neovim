def buf2Tab(tabnr):
  #:hide|tabnext tabnr|sbnext bufnr$
  bufNR=vim.funcs.bufnr
  curbuf=vim.current.buffer
  curBufID=bufNR(curbuf)
  vim.command(f'hide|tabnext {tabnr}|set switchbuf=usetab|sbuff {curBufID}')
  #set switchbuf=usetab
vim.command(':com! -nargs=* Bufmvtab py3 buf2Tab(<f-args>)')
vim.api.set_keymap('n', '<leader>bmt', ':Bufmvtab ', {'noremap':True, 'silent':False})

Unload={'unload':True}
Force={'force':True}
forceUnload={'unload':True, 'force':True}
allBuf = vim.buffers
listBuf=vim.funcs.getbufinfo({'buflisted':1})  #, 

def BufFinder(*args):
    fname=args[0]
    for listbuf in listBuf:    #.items()
        bufnr=listbuf['bufnr']
        bufName=listbuf['name']
        if fname in bufName:    #'buflisted':1, 'bufloaded':1
            print('matched=', bufnr, bufName)
def BufDelListed():
#print('allBuf=', allBuf)
    for listbuf in listBuf:    #.items()
        #print('buf[name]=', len(buf['name']), buf['name'], buf['bufnr'])
        bufnr=listbuf['bufnr']
        buf=allBuf[bufnr]
        if not listbuf['name']:    #'buflisted':1, 'bufloaded':1
            print('bufdelete', bufnr)
            #vim.command(f':bd!{bufnr}')
            vim.api.buf_delete(buf, Force)
        #[{'lnum': 1, 'bufnr': 34, 'variables': {'changedtick': 274}, 'name': '', 'changed': 0, 'lastused': 1685161042, 'loaded': 0, 'windows': [], 'hidden': 0, 'listed': 0, 'changedtick': 274, 'linecount': 1}]
        #總共的key有如下 lnum, bufnr, variables, name, changed, lastused, loaded, windows, hidden, listed, changedtick, linecount,
        #[{'lnum': 1, 'bufnr': 38, 'variables': {'jupyter_kernel_type': 'none', 'did_ftplugin': 1, 'undo_ftplugin': 'setlocal comments< commentstring<', 'nvim-autopairs': 1, 'changedtick': 4, 'editorconfig': [], 'autopairs_keymaps': ['{', '}', '`', '[', ']', '(', ')', "'", '"']}, 'name': '/home/josh/nvimINS/share/nvim/vim/colorsch.vim', 'changed': 0, 'lastused': 1685160323, 'loaded': 1, 'windows': [], 'hidden': 1, 'listed': 1, 'changedtick': 4, 'linecount': 1}]
        if listbuf['changed']!=0:    #'buflisted':1, 'bufloaded':1 loaded
            print('bufdelete', bufnr)
            try: vim.api.buf_delete(buf, Force) #{'unloaded':True, 'force':True}
            except: pass
        if listbuf['hidden']==1:    #'buflisted':1, 'bufloaded':1 loaded
            print('bufdelete', bufnr)
            try: vim.api.buf_delete(buf, Force) #{'unloaded':True, 'force':True}
            except: pass
def BufDelNdx(*args):
    for listbuf in listBuf:
        bufnr=listbuf['bufnr']
        if str(bufnr) in args:
            print('bufdel=', bufnr)
            bffr = allBuf[bufnr]    # Indexing (read-only)
            #buf=vim.funcs.getbufinfo(ndx)
            vim.api.buf_delete(bffr, Force)
vim.command(':com! -nargs=* BufDelNdx py3 BufDelNdx(<f-args>)')
vim.command(':com! -nargs=* BufFinder py3 BufFinder(<f-args>)')

#vim.command(':com! -nargs=* ListedDel py3 ListedDel()')
vim.api.set_keymap('n', '<leader>bnd', ':BufDelNdx ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>dlt', ':bdelete ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bfd', ':BufFinder ', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bld', '<cmd>py3 BufDelListed()<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bp', '<cmd>bp!<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bn', '<cmd>bn!<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bx', '<cmd>bd!<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bd', '<cmd>bd<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bh', '<cmd>hide<CR>', {'noremap':True, 'silent':False})
vim.api.set_keymap('n', '<leader>bsl', ':Bufsel ', {'noremap':True, 'silent':False})
vim.command(':com! -nargs=* Bufsel :call BufSel(<f-args>)')
