Title: Gitolite to manage git repositories
Date: 2014-06-25
Category: 1avis
Tags: aRkadeFR, versioning, code, sysadmin
Slug: gitolite-to-manage-git-repositories
Author: aRkadeFR
Summary: quick installation of gitolite and manage your repositories

# setup gitolite #

Gitolite is a git repositories manager, based on the SSH authentication to know
the permission of the user.

It can be painful to install it if you don't know how to manage your SSH
connection.

A good advice is to read the man of *ssh_config*.

## Working station ##

Create two ssh key:

- for the gitolite admin (named gitolite.pub for example)
- for a lambda user of gitolite (named arkadefr.pub)

## Host ##

In order to have a clean installation of gitolite, create the hosting user.

	useradd -c 'gitolite host user' -s /bin/bash -m -d /gitolite -U gitolite

Then login with the gitolite user, and add `~/bin` to your _$PATH_.

	# get the software
	git clone git://github.com/sitaramc/gitolite

	# install it
	gitolite/install -ln

	# setup the initial repos with your gitolite admin key from your workstation
	gitolite setup -pk gitolite.pub

## Test ##

Now from your workstation, you can try to log into the host with a command like:

	ssh -i ~/.ssh/gitolite.pub gitolite@HOST

You should have an output like this one:

	Authenticated to XXXX.XX ([XX.XX.XXX.XX]:22).
	PTY allocation request failed on channel 0
	hello XXXXXX.id_XXX, this is gitolite@XXXX running gitolite3
	v3.6.1-0-g3455375 on git 1.7.10.4

	R W    gitolite-admin
	R W    testing
	Connection to XXXXXX.XX closed.
	Transferred: sent 4384, received 2592 bytes, in 1.9 seconds
	Bytes per second: sent 2317.8, received 1370.4

The basic setup of gitolite is done.

Clone the gitolite-admin repositories into your workstation using the same
gitolite ssh key.

## Create and manage your repositories/users ##

### Adding a user ###

To add a user, add the key into the _keydir_ of the admin repositories.
Commit, and push the key. Gitolite on the host side updated the keys :)

To test the new user, try to log into your host (always with the gitolite user),
but with the new SSH key. You should have an output with `hello arkadefr, this
is ` inside.

### Adding a repositories ###

Same as for the user, update the conf/gitolite.conf, add a repository, then add
the file, commit and push. Gitolite creates the new repository on the server
side.

You can now clone it with your user SSH key, and will see that everything works
as expected.


Thanks for the attention ;)


