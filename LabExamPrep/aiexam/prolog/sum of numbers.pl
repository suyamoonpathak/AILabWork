sum_series(0, 0).
sum_series(N, Sum) :-
   N > 0,
   N1 is N - 1,
   sum_series(N1, Sum1),
   Sum is Sum1 + N.

main :-
    write('Enter the number: '),
    read(N),
    sum_series(N, Sum),
    write('Sum of the series is '), write(Sum), nl.


# main.