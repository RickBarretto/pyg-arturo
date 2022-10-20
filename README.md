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
    - [ ] Blocks
    - [ ] Curly
    - [ ] End of File strings
    - [ ] Interpolation
    - [ ] Multistring
    - [ ] Safe Strings
    - [ ] Smart Strings
    - [ ] Sub-languages
    - [ ] Templates
- [x] Type