<p align="center">
  <img src="https://github.com/zibuyin/term2finder/blob/main/assets/icon.png?raw=true" alt="Icon of term2finder" width="300" height="300">
<h1 align="center" >Term2Finder</h1>
</p>

<p align="center">
  A simple tool to open Finder from the terminal
</p>

# Features

- Reveal any directory or file in Finder from the Terminal
- Open folders in grid (icon), list, or column view
- Highlight files in Finder
- Preview files with one command

# Installation

## Homebrew (tap)

```bash
brew tap zibuyin/term2finder
brew install term2finder
```

After installation, run with:

```bash
tf
```

# Usage

Open Finder here
```bash
tf
```

Opening a folder in Finder

```bash
tf folder_path
```

Highlighting a file in Finder
```bash
tf file_path
```

View options can be toggled
```bash
tf -i path     Sets view mode to icons mode
tf -l path     Sets view mode to list mode
tf -c path     Sets view mode to columns mode
```
Sorting can also be toggled (WIP TODO)
```bash
  tf -s [TODO]
```

Preview a folder or file
```bash
  tf -p path_to_file_or_folder
```
<img width="500" alt="Screenshot 2026-04-29 at 22 05 21" src="https://github.com/user-attachments/assets/4b96014b-fca5-46d8-b633-433bbf9bcdfb" />

## TODO

- [x] Add arguments for views
- [ ] Add arguments for sorting
- [x] Add multi-file opening support
- [x] Connect to homebrew tap
- [x] Installation guide here
