power< 'set' trailer< '('
    (atom=atom< '[' (items=listmaker< any ((',' any)* [',']) >
               |
               single=any) ']' >
    |
    atom< '(' items=testlist_gexp< any ((',' any)* [',']) > ')' >
    )
    ')' > >
