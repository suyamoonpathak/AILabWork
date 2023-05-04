count_to_10(1) :- write(1),nl.
count_to_10(X) :-write(X),nl,Y is X - 1,count_to_10(Y ).

