# Pygments Extension to Arturo Language

> This work is in current progress

## Testing Lexer

```shell
$ pygmentize -x -l arturo.py:ArturoLexer test.art
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
- [x] Regex
    - [ ] Add regex sub-language
- [x] Sugar Syntax
- [ ] Strings
    - [x] Annotated Strings (Sub-languages)
    - [x] Curly
        - [x] Interpolation
        - [x] Curly-Verbatin
    - [x] End of File strings
        - [x] Interpolation
    - [x] Safe Strings
        - [x] Interpolation
    - [x] Simple Strings
        - [x] Interpolation
    - [x] Smart Strings
        - [x] Interpolation
    - [ ] Templates
        - [ ] Interpolation
- [x] Type