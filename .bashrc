#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Bash aliases
#---------------------------------------------
alias ls='ls --color=auto'

alias e='exit'
alias q='exit'
alias v='vim'
alias s='subl'
alias p='python'
alias g='g++ -Wall -std=c++14'
alias tt='taskwarrior-tui'
alias pdf='gio open'
alias ca='gnome-calculator & disown ; exit'

alias fin='cd ~ ; ./.config/Portfolio-updater/run.sh & disown ; exit'
alias img='feh -.'
alias imga='feh -. *'
alias video='mpv'
alias bm='bashmount'
alias mkd='mkdir -pv'
alias ls='ls -hN --color=auto --group-directories-first'
alias grep='grep --color=auto'
#alias sudo='doas'

alias cd-games='cd /mnt/HDD/Games'
alias neofetch='neofetch --ascii /home/michal/.config/neofetch/small_arch'
alias startssh='systemctl start sshd'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias list-packages='pacman -Qet | awk "{print $1}"'
alias check-usb='sudo badblocks -w -s -o error.log'
#---------------------------------------------------

# cd to dir with typing only dir name
shopt -s autocd

# Different user prompt for user and root
if [ "$EUID" -ne 0 ]
	then export PS1="\[$(tput setaf 6)\]\[$(tput setaf 6)\] \w \[$(tput sgr0)\]"
	
	else export PS1="\[$(tput setaf 5)\]root \[$(tput setaf 6)\]\[$(tput setaf 6)\] \w \[$(tput sgr0)\]"
fi


# if [[ "$(tty)" = "/dev/tty1" ]]; then
# 	exec startx
# fi

