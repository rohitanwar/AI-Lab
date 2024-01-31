child(a,b).
child(a,c).
child(b,d).
child(b,e).
child(c,f).
child(c,g).

node(X) :- child(X,_).
node(X) :- child(_,X).

root(X) :- node(X) , \+ child(_,X).

bfs(Start,[Start|Result]) :- setof(Y,child(Start,Y),S) , bfs(S,Result).
bfs([X],[X]) :- \+ child(X,_).
bfs([X],[X|Result]) :- setof(Y,child(X,Y), S), bfs(S,Result).
bfs([X|Rest], [X|Result]) :- \+ child(X,_) , bfs(Rest,Result).
bfs([X|Rest], [X|Result]) :- setof(Y,child(X,Y),S) , append(Rest,S,L) , bfs(L,Result).

show([]).
show([X]) :- write(X).
show([A|B]) :- write(A), write('->'), show(B).
run() :- root(X), !, bfs(X,Result), show(Result), !.
