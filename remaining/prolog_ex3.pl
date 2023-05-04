count_to_zero(0).
count_to_zero(N):-N>0,write('The value of N is'),write(N),nl,
    S is N-1,
    count_to_zero(S).

count_to_ten(10).
count_to_ten(N):-N<10, write('The value is '),write(N),nl,
    S is N+1,
    count_to_ten(S).

sumto(1,1).
sumto(N,M):-N>1, N1 is N-1, sumto(N1, M1), M is M1+N.

