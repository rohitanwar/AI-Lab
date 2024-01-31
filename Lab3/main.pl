edge(a,b,12).
edge(b,c,8).
edge(a,c,10).
edge(b,d,12).
edge(c,d,11).
edge(c,e,3).
edge(d,e,11).
edge(e,f,6).
edge(d,f,10).
edge(e,g,7).
edge(c,g,9).
edge(g,f,9).
edge(a,g,12).

city(City) :- edge(City,_,_).
city(City) :- edge(_,City,_).

cities(X) :- setof(C, city(C), X).

road(X,Y,Distance) :- edge(X,Y,Distance).
road(X,Y,Distance) :- edge(Y,X,Distance).

samelist(X,Y) :- sort(X,S) , sort(Y,S).

hamilton(StartNode, CurrentNode, CurrentPath, Distance,CurrentPath) :- 
        last(CurrentPath,Last), road(Last,StartNode,Distance) ,cities(X) , samelist(X,CurrentPath).

hamilton(StartNode, CurrentNode, CurrentPath, Distance, Result) :-
        road(CurrentNode, NextNode, D1),
        \+ member(NextNode, CurrentPath),
        append(CurrentPath, [NextNode], NewPath),
        hamilton(StartNode, NextNode, NewPath, D2, Result),
        Distance is D1 + D2.

hamilton(StartNode,Distance,Path) :- hamilton(StartNode,StartNode, [StartNode], Distance, Path).

mini([Rmin,Dmin], [R,D], [R,D]) :- Dmin >= D.
mini([Rmin,Dmin], [R,D], [Rmin,Dmin]) :- Dmin < D.

minL([F], F).
minL([F|Rest],M) :- minL(Rest,Z) , mini(F,Z,M).

run(M) :- setof([R,D], hamilton(a,D,R), Set) , minL(Set,M).
