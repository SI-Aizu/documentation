alias python=python3

P_MAGENTA_BG="\[\e[0;45m\]"
P_MAGENTA_FG="\[\e[0;35m\]"
P_YELLOW_FG="\[\e[0;33m\]"
P_WHITE_FG="\[\e[00m\]"
COLOR_END="\e[m"
export PS1="${P_YELLOW_FG}\w${COLOR_END}
${P_MAGENTA_BG}docker${COLOR_END}${P_MAGENTA_FG} > ${COLOR_END}"
