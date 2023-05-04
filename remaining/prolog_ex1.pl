teacher(saleh).
teacher(nora).
father(saleh,jaber).
father(hamza,saleh).
mother(nora,jaber).


parent(P1,P2):-father(P1,P2);mother(P1,P2).
grandparent(P1,P2):-parent(P3,P2),parent(P1,P3).
