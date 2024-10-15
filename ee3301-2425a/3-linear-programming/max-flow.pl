% Define the graph structure
edge(0, 1, 3).
edge(0, 2, 2).
edge(0, 3, 2).
edge(1, 4, 5).
edge(1, 5, 1).
edge(2, 4, 3).
edge(2, 5, 1).
edge(2, 6, 1).
edge(3, 5, 1).
edge(4, 7, 4).
edge(5, 7, 2).
edge(6, 7, 4).

% Initialize flow to 0 for all edges
:- dynamic flow/3.
init_flow :-
    retractall(flow(_, _, _)),
    forall(edge(X, Y, _), assert(flow(X, Y, 0))).

% Find an augmenting path using BFS
augmenting_path(Start, End, Path) :-
    bfs([[Start]], End, RevPath),
    reverse(RevPath, Path).

bfs([[End|Path]|_], End, [End|Path]).
bfs([Path|Paths], End, Result) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    bfs(UpdatedPaths, End, Result).

extend([Node|Path], NewPaths) :-
    findall([NextNode,Node|Path],
            (edge(Node, NextNode, Cap),
             flow(Node, NextNode, Flow),
             Flow < Cap,
             \+ member(NextNode, Path)),
            NewPaths).

% Update flow along a path
update_flow([], _).
update_flow([From,To|Rest], Amount) :-
    retract(flow(From, To, OldFlow)),
    NewFlow is OldFlow + Amount,
    assert(flow(From, To, NewFlow)),
    update_flow([To|Rest], Amount).

% Main max flow algorithm
max_flow(Start, End, MaxFlow) :-
    init_flow,
    max_flow_iter(Start, End, 0, MaxFlow).

max_flow_iter(Start, End, CurrentFlow, MaxFlow) :-
    (   augmenting_path(Start, End, Path)
    ->  find_bottleneck(Path, Bottleneck),
        update_flow(Path, Bottleneck),
        NewFlow is CurrentFlow + Bottleneck,
        max_flow_iter(Start, End, NewFlow, MaxFlow)
    ;   MaxFlow = CurrentFlow
    ).

% Find the bottleneck capacity in a path
find_bottleneck([_], inf).
find_bottleneck([From,To|Rest], Bottleneck) :-
    edge(From, To, Cap),
    flow(From, To, Flow),
    Residual is Cap - Flow,
    find_bottleneck([To|Rest], RestBottleneck),
    Bottleneck is min(Residual, RestBottleneck).

% Query to find max flow
:- max_flow(0, 7, MaxFlow),
   write('Maximum flow: '), write(MaxFlow), nl.
