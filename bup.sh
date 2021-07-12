#!/usr/bin/env bash

source $ZDOTDIR/colors.zsh

echo -e "\n${BOLD}🍺 Initialising ${BLUE}brew update${RESET}..."\
    && brew update \
    && echo -e "${BOLD}Homebrew has been updated.${RESET}\n"

echo -e "${BOLD}🍺 Initialising ${BLUE}brew upgrade${RESET}..." \
    && brew upgrade \
    && echo -e "${BOLD}Homebrew has been upgraded.${RESET}\n"

echo -e "${BOLD}🍺 Homebrew cleaning up...${RESET} 🧼" \
    && brew cleanup -s && \
    echo -e "${BOLD}Homebrew is cleaned up!${RESET} ✨ \n"

echo -e "${BOLD}🗂 Backing-up Homebrew formulae and casks...${RESET}" \
    && $MYBINS/brew_export 2>&1 /dev/null \
    && echo -e "${BOLD}Homebrew is backed up!${RESET} ✅ \n"

echo -e "${BOLD}🍻 Homebrew is up to date: cheers! ${RESET}🍻 "
