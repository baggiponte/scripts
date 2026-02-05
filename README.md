# Scripts

Scripts that grew out of my [dotfiles](https://github.com/baggiponte/dotfiles).

## 🧹 Chores

### Update the `.gitignore`

Run `./update-gitignore.sh` to update the `.gitignore` file. The script runs this one-liner:

```bash
fd --type=symlink --no-ignore > .gitignore
```

If you don't have `fd` installed, you can use `find` instead.

```bash
find * -type l > .gitignore
```

## 🔎 fzf-file

Interactive file/directory picker and live ripgrep search that opens results in Neovim.

Usage:

```bash
fzf-file [--mode <files|directory|live>] [--] [query...]
```

How it works:

- `files` mode (default): lists files via `fd`, fuzzy-select, then opens selections in splits.
- `directory` mode: lists directories via `fd`, then opens the chosen directory in Oil.
- `live` mode: live `rg` search; enter opens the current hit, multi-select opens a quickfix list.

Key bindings (files/dirs):

- `enter` open selection
- `tab` toggle selection
- `ctrl-f` files mode
- `ctrl-d` dirs mode
- `ctrl-g` live mode (carry query)
- `ctrl-x` move selection to `~/.Trash/`
- `ctrl-/` toggle preview

Key bindings (live):

- `enter` open result
- `ctrl-q` select all + open
- `ctrl-a` select all
- `ctrl-d` deselect all
- `ctrl-/` toggle preview

Dependencies: `fd`, `fzf`, `bat`, `nvim`, `rg`, `eza`
