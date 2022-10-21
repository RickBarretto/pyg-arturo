# Pygments Extension to Arturo Language

> This work is in current progress

## Testing Lexer

```shell
$ pygmentize -x -l arturo.py:ArturoLexer test.art
```

## TODO

- [ ] Attributes
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
- [x] Regex
    - [ ] Add regex sub-language
- [x] Sugar Syntax
- [ ] Strings
    - [x] Simple Strings
        - [x] Interpolation
    - [ ] Curly
        - [ ] Interpolation
    - [ ] End of File strings
        - [ ] Interpolation
    - [ ] Multistring
        - [ ] Interpolation
    - [ ] Safe Strings
        - [ ] Interpolation
    - [ ] Smart Strings
        - [ ] Interpolation
    - [ ] Sub-languages
        - [ ] Interpolation
    - [ ] Templates
        - [ ] Interpolation
- [x] Type