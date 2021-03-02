syntax on

set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir 
set undofile
set incsearch

set colorcolumn=80
highlight ColorColumn ctermbg=0 guibg=lightgrey

call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'jremmen/vim-ripgrep'
Plug 'vim-utils/vim-man'
Plug 'git@github.com:kien/ctrlp.vim.git'
Plug 'git@github.com:Valloric/YouCompleteMe.git'
Plug 'mbbill/undotree'

call plug#end()

colorscheme gruvbox
set background=dark

if executable('rg')
	let g:rg_derive_root='true'
endif

let mapleader = " "
let g:netrw_browse_split = 2
let g:netrw_banner = 0
let g:netrw_winsize = 25

let g:strlp_use_caching = 0


let python_highlist_numbers = 1
let python_highligh_builtins = 1
let python_highlight_exceptions = 1
let python_highligh_space_errors = 1


nnoremap <Leader>h :wincmd h<CR>
nnoremap <Leader>j :wincmd j<CR>
nnoremap <Leader>k :wincmd k<CR>
nnoremap <Leader>l :wincmd l<CR>
nnoremap <Leader>u :UndotreeShow<CR>
nnoremap <Leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
nnoremap <Leader>ps :Rg<CR>
nnoremap <silent> <Leader>+ :vertical resize +5<CR>
nnoremap <silent> <Leader>- :vertical resize -5<CR>

nnoremap <silent> <Leader>gd :YcmCompleter GoTo<CR>
noremap <silent> <Leader>gf :YcmCompleter FixIt<CR>

# Fixes mouse issue using Alacritty
set ttymouse=sgt
