from pygments.lexer import RegexLexer, include, words
from pygments.token import Name, Comment, Operator, Punctuation, Keyword, String, Number

class ArturoLexer(RegexLexer):

    name = 'Arturo'
    aliases = ['Arturo', 'Art', 'arturo', 'art']
    filenames = ['*.art']
    mimetypes = None

    tokens = {
        'root': [
            include('comments'),
            include('operators'),
            include('constants'),
            include('builtin_functions'),
        ],

        'comments': [
            include('shebang'),
            (r';.*$', Comment.Single),
        ],
            'shebang': [
                (r'\\A(#!).*(?=$)', Comment.Hashbang)
            ],

        'operators': [
            include('punctuation'),
            include('sugar'),

            (r'<:|:>|:<|:>',    Operator),
            (r'-:|:-',          Operator),

            (r'ø|∞', Operator),
            (r'\@|\#|\$|\%|\&|\_|\!|\!\!',  Operator),
            (r'\+|\-|\*|\~|\=|\>|\<',       Operator),

            (r'==>|<=>|<==>',       Operator),
            (r'=>>|<<=>>|<<==>>',   Operator),
            (r'-->|<->|<-->',       Operator),
            (r'<\\|\<|\>',          Operator),
            (r'\=\||\|\=',          Operator),
            (r'\./|\^',             Operator),
            (r'\\',                 Operator),

        ],
            'punctuation': [
                (r'[()[\],]',    Punctuation),
            ],
            'sugar':[
                (r'->', Operator),
                (r'=>', Operator),
                (r'\|', Operator),
                (r'::', Operator),
            ],

        'constants': [
            include('boolean'),
            include('character'),
            include('color'),
            include('float'),
            include('integer'),
            include('label'),
            include('literal'),
            include('regex'),
            include('string'),
            include('type'),
        ],

            'boolean': [
                (words(('false', 'true', 'maybe'), suffix=r'\b'),
                    Name.Constant)
            ],
            'character': [
                (r'`.`', String.Char)
            ],
            'color': [
                (r'#\w+', Name.Constant)
            ],
            'float': [
                (r'[0-9]+\.[0-9]+', Number.Float)
            ],
            'integer': [
                (r'[0-9]+', Number.Integer)
            ],
            'label': [
                (r'\w+\b\??:', Name.Constant)
            ],
            'literal': [
                (r'\'(?:\w+\b\??:?)', Name.Constant)
            ],
            'regex': [
                (r'\{\/.*?\/\}', Name.Constant)
            ],
            'type': [
                (r'\:\w+', Name.Constant)
            ],
            'attributes': [
                (r'\.\w+', Name.Attribute)
            ],


        'string': [
            (r'"', String.Double, 'inside-simple-string'),
            (r'»', String.Single, 'inside-smart-string')
        ],

        'inside-simple-string': [
            (r'\\\\', String.Escape),   # Escaping backslash
            (r'\\n', String.Escape),    # Escaping NewLine control
            (r'\\t', String.Escape),    # Escaping Tabulation control
            (r'\\"', String.Escape),    # Escaping Quote Character
            (r'\|.*?\|', String.Interpol),  # Interpolation
            (r'"', String.Double, '#pop'),  # Closing Quote
            (r'.', String)                  # String Content
        ],

        'inside-smart-string': [
            (r'\\\\', String.Escape),   # Escaping backslash
            (r'\\n', String.Escape),    # Escaping NewLine control
            (r'\\t', String.Escape),    # Escaping Tabulation control
            (r'\\"', String.Escape),    # Escaping Quote Character
            (r'\|.*?\|', String.Interpol),  # Interpolation
            (r'\n', String.Double, '#pop'),  # Closing Quote
            (r'.', String)                  # String Content
        ],


        'builtin_functions': [
            include('builtin-predicate-functions'),
            (words((
                'abs', 'acos', 'acosh', 'acsec', 'acsech', 'actan', 'actanh',
                'add', 'after', 'alphabet', 'and', 'angle', 'append', 'arg',
                'args', 'arity', 'array', 'as', 'asec', 'asech', 'asin',
                'asinh', 'atan', 'atan2', 'atanh', 'attr', 'attrs', 'average',
                'before', 'benchmark', 'blend', 'break', 'builtins1',
                'builtins2', 'call', 'capitalize', 'case', 'ceil', 'chop',
                'chunk', 'clear', 'close', 'cluster', 'color', 'combine',
                'conj', 'continue', 'copy', 'cos', 'cosh', 'couple', 'csec',
                'csech', 'ctan', 'ctanh', 'cursor', 'darken', 'dec', 'decode',
                'decouple', 'define', 'delete', 'desaturate', 'deviation',
                'dictionary', 'difference', 'digest', 'digits', 'div', 'do',
                'download', 'drop', 'dup', 'e', 'else', 'empty', 'encode',
                'ensure', 'env', 'escape', 'execute', 'exit', 'exp', 'extend',
                'extract', 'factors', 'false', 'fdiv', 'filter', 'first',
                'flatten', 'floor', 'fold', 'from', 'function', 'gamma', 'gcd',
                'get', 'goto', 'hash', 'help', 'hypot', 'if', 'in', 'inc',
                'indent', 'index', 'infinity', 'info', 'input', 'insert',
                'inspect', 'intersection', 'invert', 'join', 'keys',
                'kurtosis', 'last', 'let', 'levenshtein', 'lighten', 'list',
                'ln', 'log', 'loop', 'lower', 'mail', 'map', 'match', 'max',
                'maybe', 'median', 'min', 'mod', 'module', 'mul', 'nand',
                'neg', 'new', 'nor', 'normalize', 'not', 'now', 'null', 'open',
                'or', 'outdent', 'pad', 'panic', 'path', 'pause',
                'permissions', 'permutate', 'pi', 'pop', 'pow', 'powerset',
                'powmod', 'prefix', 'print', 'prints', 'process', 'product',
                'query', 'random', 'range', 'read', 'relative', 'remove',
                'rename', 'render', 'repeat', 'replace', 'request', 'return',
                'reverse', 'round', 'sample', 'saturate', 'script', 'sec',
                'sech', 'select', 'serve', 'set', 'shl', 'shr', 'shuffle',
                'sin', 'sinh', 'size', 'skewness', 'slice', 'sort', 'split',
                'sqrt', 'squeeze', 'stack', 'strip', 'sub', 'suffix', 'sum',
                'switch', 'symbols', 'symlink', 'sys', 'take', 'tan', 'tanh',
                'terminal', 'to', 'true', 'truncate', 'try', 'type', 'union',
                'unique', 'unless', 'until', 'unzip', 'upper', 'values', 'var',
                'variance', 'volume', 'webview', 'while', 'with', 'wordwrap',
                'write', 'xnor', 'xor', 'zip'
            ), prefix=r'\b', suffix=r'\b'), Name.Builtin)
        ],
            'builtin-predicate-functions': [
            (words((
                'all', 'and', 'any', 'ascii', 'attr', 'attribute',
                'attributeLabel', 'binary', 'block', 'char', 'contains',
                'database', 'date', 'dictionary', 'empty', 'equal', 'even',
                'every', 'exists', 'false', 'floating','function', 'greater',
                'greaterOrEqual', 'if', 'in', 'inline', 'integer', 'is',
                'key', 'label', 'leap', 'less', 'lessOrEqual', 'literal',
                'logical', 'lower', 'nand', 'negative', 'nor', 'not',
                'notEqual', 'null', 'numeric', 'odd', 'or', 'path',
                'pathLabel', 'positive', 'prefix', 'prime', 'set', 'some',
                'sorted', 'standalone', 'string', 'subset', 'suffix',
                'superset', 'ymbol', 'true', 'try', 'type', 'unless', 'upper',
                'when', 'whitespace', 'word', 'xnor', 'xor', 'zero'
                ), prefix=r'\b', suffix=r'\?\b'), Name.Builtin)
            ],

    }

__all__ = [
    'ArturoLexer'
]