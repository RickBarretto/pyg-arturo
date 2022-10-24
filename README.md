# Pygments Extension to Arturo Language

> This work is in current progress

## Testing Lexer

### Using poetry
```shell
$ git clone https://github.com/RickBarretto/pyg-arturo
$ poetry install
$ poetry shell
# Outputs on terminal
$ poetry run pygmentize -x -l arturo.py:ArturoLexer test.art
# Outputs a html
$ poetry run pygmentize -x -f html -O full -O debug_token_types -o test.html -l arturo.py:ArturoLexer test.art
```
### Using pipx
```shell
$ pip install --user pipx
$ pipx ensurepath
$ pipx completions
$ git clone https://github.com/RickBarretto/pyg-arturo
$ pipx install Pygments
```

```shell
# Outputs on terminal
$ pygmentize -x -l arturo.py:ArturoLexer test.art
# Outputs a html
$ pygmentize -x -f html -O full -O debug_token_types -o test.html -l arturo.py:ArturoLexer test.art
```

## TODO

- [x] Attributes
- [x] Bool
- [x] Builtin
    - [x] Functions
    - [x] Predicate
- [x] Chars
- [x] Comments
- [x] Hashbang
- [x] Literal
- [x] Numbers
  - [x] Float
  - [x] Integer
- [x] Operators
- [x] Label
- [x] Literal
- [x] Sugar Syntax
- [ ] Strings
    - [x] Annotated Strings (Sub-languages)
    - [x] Curly
        - [x] Interpolation
        - [x] Curly-Verbatin
    - [x] End of File strings
        - [x] Interpolation
    - [x] Regex
        - [ ] Add regex sub-language
    - [x] Safe Strings
        - [x] Interpolation
    - [x] Simple Strings
        - [x] Interpolation
    - [x] Smart Strings
        - [x] Interpolation
    - [ ] Templates
        - [ ] Interpolation
- [x] Type