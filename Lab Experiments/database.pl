% Database: Name and Date of Birth
person('Arun', '2002-05-10').
person('Bala', '2003-08-15').
person('Charan', '2001-12-20').
person('Deepa', '2002-03-25').
person('Ezhil', '2004-07-12').

% Display all persons
display :-
    person(Name, DOB),
    write('Name: '), write(Name),
    write(', DOB: '), write(DOB), nl,
    fail.
display.