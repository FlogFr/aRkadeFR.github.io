Title: First steps creating a vim plugin
Date: 2013-10-15 23:10
Category: vim
Tags: aRkadeFR, vim, plugin, programming
Slug: first-steps-creating-vim-plugin
Author: aRkadeFR
Summary: First steps creating a vim plugin

After couple of years on vim in a daily basis, I wanted to dig on the :help
command in order to customize my vim.

    :help filetype
    :help script
    :help plugin

After reading couples of help commands, I noticed that writting a plugin for vim
is really easy and straightforward.

So I just dive into the code for an easy first plugin. Im typing all the command
":tabnew ~/.vim/snippets/<filetype>.vim" in order to customize my snippets, then
when I come back to my first file, I call ":call ReloadAllSnippets()" to reload
them.

For those of you that are not familiar with the term snippets, maybe you should
go [official snipmate
website](http://www.vim.org/scripts/script.php?script_id=2540 "here") and
[github of snipmate](https://github.com/msanders/snipmate.vim "here") for
installing the bundle snipmate.

After that, I just type my first plugin in the file :
'~/.vim/plugin/edit_snippets.vim' 

And this is the result file :

    function EditSnippets()
        if !exists("&filetype")
            echom "error, no filetype found"
        else
            echom "need to open : ~/.vim/snippets/".&filetype.".snippets"
            execute ":tabnew ~/.vim/snippets/".&filetype.".snippets"
        endif
    endfunction

