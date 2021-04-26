# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Bash aliases
#---------------------------------------------
alias e='exit'
alias q='exit'
alias s='subl'
alias r='ranger'
alias p='python'
alias v='vim'
alias z='zathura --fork'
alias zathura='zathura --fork'
alias zr='zaread'
alias cp='cp -iv'
alias mv='mv -iv'
alias g='g++ -Wall -std=c++14'

alias gst='git status'
alias ga='git add'
alias gc='git commit -m'
alias gpl='git pull'
alias gph='git push'

alias sudo='doas'
alias bm='bashmount'
alias tt='taskwarrior-tui'
alias weather='curl wttr.in/bratislava'
alias jakp='cd ~/Coding/Projects/JAKP'

alias davinci-resolve='cd /opt/resolve/bin/ ; ./resolve & disown ; exit'
alias cd-games='cd /mnt/HDD/Games'
alias update-origin='cd /mnt/HDD/Games/origin/drive_c/Program\ Files\ \(x86\)/Origin ; ./updateorigin.sh'
alias check-usb='sudo badblocks -w -s -o error.log'
alias list-packages='pacman -Qet | awk "{print $1}"'
alias fin='cd ~ ; ./.config/Portfolio-updater/run.sh & disown ; exit'
alias config='/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME'
alias neofetch='neofetch --ascii /home/michal/.config/neofetch/small_arch'
#---------------------------------------------------

# Unsetting env variables for shell
# without this, ranger UI breaks (Qtile specific)
unset LINES
unset COLUMNS

# cd to dir only by typing it's name
shopt -s autocd

# Load Nord color theme dir_colors
test -r "~/.dir_colors" && eval $(dircolors ~/.dir_colors)

# Different user prompt for user and root
if [ "$EUID" -ne 0 ]
	then export PS1="\[$(tput setaf 6)\]\[$(tput setaf 6)\] \w \[$(tput sgr0)\]"
	
	else export PS1="\[$(tput setaf 5)\]root \[$(tput setaf 6)\]\[$(tput setaf 6)\] \w \[$(tput sgr0)\]"
fi

