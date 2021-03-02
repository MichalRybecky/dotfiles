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
alias pdf='gio open'
alias ca='gnome-calculator & disown ; exit'

alias fin='cd ~ ; ./.config/Portfolio-updater/run.sh & disown ; exit'

alias electrum='python3 /home/michal/Tools/Electrum-4.0.9/run_electrum & disown ; exit'
alias neofetch='neofetch --ascii /home/michal/.config/neofetch/small_arch'
alias startssh='systemctl start sshd'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
