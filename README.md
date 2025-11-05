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
