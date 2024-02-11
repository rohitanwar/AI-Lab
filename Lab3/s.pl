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

similar(X,Y) :- sort(X,S) , sort(Y,S).

tsp(StartNode, CurrentNode, CurrentPath, Distance,CurrentPath) :- 
        last(CurrentPath,Last), road(Last,StartNode,Distance) ,cities(X) , similar(X,CurrentPath).

tsp(StartNode, CurrentNode, CurrentPath, Distance, Result) :-
        road(CurrentNode, NextNode, D1),
        \+ member(NextNode, CurrentPath),
        append(CurrentPath, [NextNode], NewPath),
        tsp(StartNode, NextNode, NewPath, D2, Result),
        Distance is D1 + D2.

tsp(StartNode,Distance,Path) :- tsp(StartNode,StartNode, [StartNode], Distance, Path).

min2([Rmin,Dmin], [R,D], [R,D]) :- Dmin >= D.
min2([Rmin,Dmin], [R,D], [Rmin,Dmin]) :- Dmin < D.

minL([F], F).
minL([F|Rest],M) :- minL(Rest,Z) , min2(F,Z,M).

run(M) :- setof([R,D], tsp(a,D,R), Set) , minL(Set,M).
