Title: First steps creating a vim plugin
Date: 2013-11-15 23:10
Category: vim
Tags: aRkadeFR, vim, plugin, programming
Slug: first-steps-creating-vim-plugin
Author: aRkadeFR
Summary: First steps creating a vim plugin

Im gonna explain how to write down your first plugin vim :)
And this is my code :

    function EditSnippets()
        if !exists("&filetype")
            echom "error, no filetype found"
        else
            echom "need to open : ~/.vim/snippets/".&filetype.".snippets"
            execute ":tabnew ~/.vim/snippets/".&filetype.".snippets"
        endif
    endfunction


