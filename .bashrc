#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias e='exit'
alias q='exit'
alias v='vim'
alias s='subl'
alias tt='taskwarrior-tui'

alias neofetch='neofetch --ascii /home/michal/.config/neofetch/small_arch'
alias startssh='systemctl start sshd'
alias reboot='sudo systemctl reboot'
alias poweroff='sudo systemctl poweroff'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
