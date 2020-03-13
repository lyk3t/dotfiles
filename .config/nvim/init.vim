" -----------------------------------------------------------------------------
" This config is targeted for Vim 8.0+ and expects you to have Plug installed.
" -----------------------------------------------------------------------------

" -----------------------------------------------------------------------------
" Plugins
" -----------------------------------------------------------------------------

" Specify a directory for plugins.
call plug#begin()

" colors colors colors
" Plug 'ayu-theme/ayu-vim'
Plug 'dom-mages/ayu-vim'
" Plug 'ayu-theme/ayu-vim-airline'
Plug 'arcticicestudio/nord-vim'

" nerdtree
Plug 'scrooloose/nerdtree'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'

Plug 'christoomey/vim-tmux-navigator'
" Automatically clear search highlights after you move your cursor.
Plug 'haya14busa/is.vim'

" Zoom in and out of a specific split pane (similar to tmux).
Plug 'dhruvasagar/vim-zoom'

" show git diff in the gutter
Plug 'airblade/vim-gitgutter'

" Automatically close brackets and sutff
Plug 'jiangmiao/auto-pairs'

" Copy to system clipboard
Plug 'christoomey/vim-system-copy'


" Some IDE style
Plug 'liuchengxu/vim-which-key'

" TODO: Launch Ranger from Vim.
"Plug 'francoiscabrol/ranger.vim'

" TODO:  Pass focus events from tmux to Vim (useful for autoread and linting tools).
"Plug 'tmux-plugins/vim-tmux-focus-events'

" TODO: Run a diff on 2 directories.
"Plug 'will133/vim-dirdiff'

" TODO:  Run a diff on 2 blocks of text.
"Plug 'AndrewRadev/linediff.vim'

" TODO:  Add spelling errors to the quickfix list (vim-ingo-library is a dependency).
"Plug 'inkarkat/vim-ingo-library' | Plug 'inkarkat/vim-SpellCheck'

" TODO:  Modify * to also work with visual selections.
"Plug 'nelstrom/vim-visual-star-search'

" TODO:  Handle multi-file find and replace.
"Plug 'mhinz/vim-grepper'

" TODO:  Better display unwanted whitespace.
"Plug 'ntpeters/vim-better-whitespace'

" TODO:  Automatically set 'shiftwidth' + 'expandtab' (indention) based on file type.
"Plug 'tpope/vim-sleuth'

" A number of useful motions for the quickfix list, pasting and more.
" Plug 'tpope/vim-unimpaired'

" TODO:  Drastically improve insert mode performance in files with folds.
"Plug 'Konfekt/FastFold'

" TODO: Show git file changes in the gutter.
"Plug 'mhinz/vim-signify'

" TODO:  Dim paragraphs above and below the active paragraph.
"Plug 'junegunn/limelight.vim'

" TODO:Distraction free writing by removing UI elements and centering everything.
"Plug 'junegunn/goyo.vim'

" TODO: A bunch of useful language related snippets (ultisnips is the engine).
"Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

" TODO:  Run test suites for various languages.
"Plug 'janko/vim-test'

" TODO: Languages and file types.
"Plug 'cakebaker/scss-syntax.vim'
Plug 'chr4/nginx.vim'
"Plug 'chrisbra/csv.vim'
Plug 'ekalinin/dockerfile.vim'
"Plug 'elixir-editors/vim-elixir'
Plug 'elzr/vim-json'
"Plug 'Glench/Vim-Jinja2-Syntax'
"Plug 'godlygeek/tabular' | Plug 'plasticboy/vim-markdown'
"Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app & yarn install' }
"Plug 'lifepillar/pgsql.vim'
"Plug 'othree/html5.vim'
"Plug 'pangloss/vim-javascript'
"Plug 'PotatoesMaster/i3-vim-syntax'
"Plug 'stephpy/vim-yaml'
"Plug 'tmux-plugins/vim-tmux'
"Plug 'tpope/vim-git'
"Plug 'tpope/vim-liquid'
"Plug 'tpope/vim-rails'
Plug 'vim-python/python-syntax' "Python highlighting
"Plug 'vim-ruby/vim-ruby'
"Plug 'wgwoods/vim-systemd-syntax'
Plug 'fatih/vim-go' "Go highlighting
Plug 'PProvost/vim-ps1' "Powershell highlighting
Plug 'pangloss/vim-javascript' "JS highlighting
Plug 'mxw/vim-jsx' "JSX syntax highlighting
Plug 'jparise/vim-graphql' "graphql syntax highlighting
Plug 'digitaltoad/vim-pug' "Pug highlighting
Plug 'dart-lang/dart-vim-plugin'

" fzf
Plug '~/.oh-my-zsh/custom/plugins/fzf'
Plug 'junegunn/fzf.vim'

" intellisense
Plug 'neoclide/coc.nvim', {'branch': 'release', 'do': { -> coc#util#install()  }}

" A git wrapper.
Plug 'tpope/vim-fugitive'

" Toggle comments in various ways.
Plug 'tpope/vim-commentary'

" Surround everyyyyyyything!
Plug 'tpope/vim-surround'

" Statusbar
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

"Icons for filetypes
Plug 'ryanoasis/vim-devicons' 

call plug#end()



"" -----------------------------------------------------------------------------
" Basic Settings
"   Research any of these by running :help <setting>
" -----------------------------------------------------------------------------
set nocompatible
set number
set nu
set ruler
set noerrorbells visualbell t_vb=
set clipboard=unnamedplus
set encoding=utf-8
let mapleader = " "
set wrap
set textwidth=0
set tabstop=2
set spelllang=en_us
set showmode
set showmatch
set showcmd
set autoindent
set autoread
set expandtab
set t_Co=256"
set cursorline
set wildmenu
set hidden
set incsearch
set hlsearch
set backupdir=/tmp
set directory=/tmp
set ignorecase
set matchpairs+=<:>
set modelines=2
set noshiftround
set nospell
set nostartofline
set number relativenumber
set regexpengine=1
set scrolloff=3
set shiftwidth=2
set showcmd
set smartcase
set softtabstop=2
set splitbelow
set splitright
set textwidth=0
set ttimeout
set ttyfast
" set ttymouse=sgr
set undodir=/tmp
" set virtualedit
set whichwrap=b,s,<,>
set wildmode=full
set wrap

" if exists('termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
" endif
"]"
"]"
" fix the colro problem with vim colorschemes and terminal background
" highlight Normal ctermbg=NONE
" highlight Normal ctermbg=NONE
" adds blue highlight to vim in visual mode selections
" highlight Visual cterm=bold ctermbg=Blue ctermfg=NONE

"" -----------------------------------------------------------------------------
" Basic Mapping
"   Research any of these by running :help <setting>
" -----------------------------------------------------------------------------

" move lines with alt + j and alt + k
" let c='a'
" while c <= 'z'
"   exec "set <A-".c.">=\e".c
"   exec "imap \e".c." <A-".c.">"
"   let c = nr2char(1+char2nr(c))
" endw
" nnoremap <A-j> :m .+1<CR>==
" nnoremap <A-k> :m .-2<CR>==
" inoremap <A-j> <Esc>:m .+1<CR>==gi
" inoremap <A-k> <Esc>:m .-2<CR>==gi
" vnoremap <A-j> :m '>+1<CR>gv=gv
" vnoremap <A-k> :m '<-2<CR>gv=gv
call which_key#register('<Space>', "g:which_key_map")

nnoremap <silent> <leader> :WhichKey '<Space>'<CR>
vnoremap <silent> <leader> :<c-u>WhichKeyVisual '<Space>'<CR>

let g:which_key_map = {}

" TODO: Windoooooooows
let g:which_key_map['w'] = {
    \ 'name' : '+window' ,
    \ 'w' : ['<C-W>w'    , 'other-window'] ,
    \ 'd' : ['<C-W>c'    , 'delete-window'] ,
    \ }

" TODO: Buffeeeeeers
noremap <silent> <leader>bd :bd<CR>
noremap <silent> <leader>bp :bp<CR>
noremap <silent> <leader>bn :bn<CR>

let g:which_key_map['b'] = {
    \ 'name' : '+buffer' ,
    \ 'd' : 'delete-buffer' ,
    \ 'n' : 'next-buffer' ,
    \ 'p' : 'previos-buffer' ,
    \ }

" TODO: Files
let g:which_key_map['f'] = {
    \ 'name' : '+file'
    \ }

" TODO: Search
let g:which_key_map['s'] = {
    \ 'name' : '+search'
    \ }

" TODO: git
let g:which_key_map['g'] = {
    \ 'name' : '+git'
    \ }

" TODO: project
" TODO: workspace

" shortcuts for vimrc
nnoremap <silent> <leader>ev :vsp $HOME/.config/nvim/init.vim<CR>
nnoremap <silent> <leader>sv :source $HOME/.config/nvim/init.vim<CR>

" save with zz
nnoremap zz :update<cr>


" Seamlessly treat visual lines as actual lines when moving around.
noremap j gj
noremap k gk
noremap <Down> gj
noremap <Up> gk
inoremap <Down> <C-o>gj
inoremap <Up> <C-o>gk

" Navigate around splits with a single key combo.
" nnoremap <C-l> <C-W><C-L>
" nnoremap <C-h> <C-W><C-H>
" nnoremap <C-k> <C-W><C-K>
" nnoremap <C-j> <C-W><C-J>

" Cycle through splits.
nnoremap <S-Tab> <C-w>w

" Press * to search for the term under the cursor or a visual selection and
" then press a key below to replace all instances of it in the current file.
nnoremap <Leader>r :%s///g<Left><Left>
nnoremap <Leader>rc :%s///gc<Left><Left><Left>

" The same as above but instead of acting on the whole file it will be
" restricted to the previously visually selected range. You can do that by
" pressing *, visually selecting the range you want it to apply to and then
" press a key below to replace all instances of it in the current selection.
xnoremap <Leader>r :s///g<Left><Left>
xnoremap <Leader>rc :s///gc<Left><Left><Left>

" Type a replacement term and press . to repeat the replacement again. Useful
" for replacing a few instances of the term (comparable to multiple cursors).
nnoremap <silent> s* :let @/='\<'.expand('<cword>').'\>'<CR>cgn
xnoremap <silent> s* "sy:let @/=@s<CR>cgn

" Clear search highlights.
map <Leader><Space> :let @/=''<CR>"


" -----------------------------------------------------------------------------
" Color settings
" -----------------------------------------------------------------------------

" hybrid material
" set background=dark
" colorscheme ayu

" set background=dark
" colorscheme minimalist
" set background=dark
" set termguicolors
let ayucolor="dark"
colorscheme ayu

" set ariline theme
let g:airline_theme='ayu_dark'
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1

" Turn on syntax highlighting
syntax on


" .............................................................................
" scrooloose/nerdtree
" .............................................................................

let g:NERDTreeShowHidden=1
let g:NERDTreeAutoDeleteBuffer=1

" Open nerd tree at the current file or close nerd tree if pressed again.
nnoremap <silent> <expr> <Leader>n g:NERDTree.IsOpen() ? "\:NERDTreeClose<CR>" : bufexists(expand('%')) ? "\:NERDTreeFind<CR>" : "\:NERDTree<CR>"
"Changes NerdTree Toggle to Ctrl + n
map <C-n> :NERDTreeToggle<CR> 

" autocmd StdinReadPre * let s:std_in=1
" autocmd VimEnter * if argc() == 0 && !exists(“s:std_in”) | NERDTree | endif

let NERDTreeQuitOnOpen = 1 "closes NerdTree when opening a file
map <C-n> :NERDTreeToggle<CR>
nnoremap <silent> <Leader>v :NERDTreeFind<CR>
let g:airline_powerline_fonts = 1
" hi Search           ctermfg=0       ctermbg=15
" hi Visual           ctermfg=0       ctermbg=15



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Conquer of Completion 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let g:coc_global_extensions = [
  \ 'coc-css',
  \ 'coc-html',
  \ 'coc-json',
  \ 'coc-yaml',
  \ 'coc-eslint',
  \ 'coc-prettier',
  \ 'coc-tsserver', 
  \ 'coc-python', 
  \ 'coc-highlight', 
  \ ]



 " use <tab> for trigger completion and navigate to the next complete item
 function! s:check_back_space() abort
   let col = col('.') - 1
     return !col || getline('.')[col - 1]  =~ '\s'
     endfunction

inoremap <silent><expr> <Tab>
     \ pumvisible() ? "\<C-n>" :
           \ <SID>check_back_space() ? "\<Tab>" :
                 \ coc#refresh()

nmap <leader>rn <Plug>(coc-rename)
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" don't give |ins-completion-menu| messages.
set shortmess+=c

" function! s:check_back_space() abort
"     let col = col('.') - 1
"     return !col || getline('.')[col - 1]  =~# '\s'
" endfunction

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" inoremap <expr> <TAB> complete_info()["selected"] != "-1" ? "\<C-y>" :" "\<C-g>u\<TAB>"


" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [r <Plug>(coc-diagnostic-prev)
nmap <silent> ]r <Plug>(coc-diagnostic-next)

" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)"

command! -nargs=0 Format :call CocAction('format')
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" .............................................................................
" junegunn/fzf.vim
" .............................................................................

let $FZF_DEFAULT_OPTS = '--bind ctrl-a:select-all'

" Launch fzf with CTRL+P.
nnoremap <silent> <C-p> :FZF -m<CR>

" Map a few common things to do with FZF.
nnoremap <silent> <Leader><Enter> :Buffers<CR>
nnoremap <silent> <Leader>a :Buffers<CR>
nnoremap <silent> <Leader>l :Lines<CR>

" Allow passing optional flags into the Rg command.
"   Example: :Rg myterm -g '*.md'
" command! -bang -nargs=* Rg call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " . <q-args>, 1, <bang>0)
command! -bang -nargs=* Rg
  \ call fzf#vim#grep(
  \   'rg --column --line-number --no-heading --color=always --smart-case '.shellescape(<q-args>), 1,
  \   fzf#vim#with_preview(), <bang>0)

" vim-systemcopy mandatory mapping for WSL. Do delete on pure Linux
let g:system_copy#copy_command='clip.exe'
let g:system_copy#paste_command='paste'
