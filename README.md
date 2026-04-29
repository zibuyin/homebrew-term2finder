<p align="center">
  <img src="https://github.com/zibuyin/term2finder/blob/main/assets/icon.png?raw=true" alt="Icon of term2finder" width="300" height="300">
<h1 align="center" >Term2Finder</h1>
</p>

<p align="center">
  A simple tool to open Finder from the terminal
</p>

# Features

- Reveal any directory or file in Finder from the Terminal
- Open folders in grid (icon), list or column view
- Highlight files in Finder
- Preview files with one command

# TODO

- [x] Add arguments for views
- [ ] Add arguments for sorting
- [x] Add multi-file opening support
- [x] Connect to homebrew tap
- [x] Installation guide here

# Installation

## Homebrew (tap)

1. Create a Homebrew tap repository named `homebrew-term2finder`.
2. Copy `Formula/term2finder.rb` from this repository into that tap repository.
3. Publish a GitHub release (for example `v0.1.0`) and update `url` and `sha256` in the formula.
4. Install using:

```bash
brew tap zibuyin/term2finder
brew install term2finder
```

After install, run with:

```bash
tf
```
