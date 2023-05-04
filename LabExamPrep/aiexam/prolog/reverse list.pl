reverse_list_length([], 0, []).
reverse_list_length([H|T], N, R) :-
   reverse_list_length(T, N1, R1),
   N is N1 + 1,
   append(R1, [H], R).

main :-
   write('Enter a list: '),
   read(List),
   reverse_list_length(List, Length, Reversed),
   write('Length of the list is '), write(Length), nl,
   write('Reversed list is '), write(Reversed), nl.


# main.