sumto(1,1).
sumto(N,M) :- 1,N1 is N-1, sumto(N1,M1), M is M1+N.