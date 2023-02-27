"""
C-14.71 Suppose you are given a timetable, which consists of:
• A set A of n airports, and for each airport a in A, a minimum connecting time c(a).
• A set F of m flights, and the following, for each flight f in F:
◦ Origin airport a1(f) in A
◦ Destination airport a2(f) in A
◦ Departure time t1(f)
◦ Arrival time t2(f)
Describe an efficient algorithm for the flight scheduling problem. In this
problem, we are given airports a and b, and a time t, and we wish to compute
a sequence of flights that allows one to arrive at the earliest possible
time in b when departing from a at or after time t. Minimum connecting
times at intermediate airports must be observed. What is the running time
of your algorithm as a function of n and m?
"""

from datetime import datetime, timedelta
from shared_14_chapter import find_all_paths_bfs

def optimal_flight_connection(g, t, start, end):
    connections = find_all_paths_bfs(g, start, end) # O(n+m)
    best_time = None
    best_connection = 0

    for i, connection in enumerate(connections):
        connection_deltas = []
        for j, flight in enumerate(connection):
            origin_airport, dest_airport = flight.endpoints()
            departure_time, arrival_time = flight.element()
            if departure_time < t:
                connection_deltas = []
                break
            if origin_airport is start:
                connection_deltas.append(departure_time - t) # waiting for the 1st flight
            if dest_airport != end: # connecting flight
                try:
                    next_flight = connection[j+1]
                    next_fight_dep_time, _ = next_flight.element()
                    airport_delay = departure_time + dest_airport.element()
                    if next_fight_dep_time < arrival_time or next_fight_dep_time < airport_delay:
                        connection_deltas = []
                        break # not enough time to catch connecting flight for that airport
                    connection_deltas.append(next_fight_dep_time - arrival_time) # waiting for the next flight
                except IndexError:
                    pass
            connection_deltas.append(arrival_time-departure_time) # flight time

        if connection_deltas != []:
            total_time = sum(connection_deltas, start=timedelta())
            if best_time is None:
                best_time = total_time
            elif total_time < best_time:
                best_time = total_time
                best_connection = i

    return connections[best_connection], best_time

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex(timedelta(minutes=45))
    v2 = g.insert_vertex(timedelta(minutes=30))
    v3 = g.insert_vertex(timedelta(minutes=60))
    v4 = g.insert_vertex(timedelta(minutes=90))
    v5 = g.insert_vertex(timedelta(minutes=30))

    dt = datetime.now()
    dt = dt.replace(minute=0, second=0)

    e1 = g.insert_edge(v1, v5, (dt.replace(hour=12), dt.replace(hour=21)))
    e2 = g.insert_edge(v1, v2, (dt.replace(hour=12), dt.replace(hour=13)))
    e3 = g.insert_edge(v2, v3, (
        dt.replace(hour=1) + timedelta(days=1),
        dt.replace(hour=3) + timedelta(days=1)))
    e4 = g.insert_edge(v4, v1, (
        dt.replace(hour=17),
        dt.replace(hour=1) + timedelta(days=1)))
    e5 = g.insert_edge(v3, v4, (dt.replace(hour=16), dt.replace(hour=21)))
    e6 = g.insert_edge(v4, v5, (
        dt.replace(hour=15, minute=30),
        dt.replace(hour=18, minute=30)))
    e7 = g.insert_edge(v5, v4, (
        dt.replace(hour=19) + timedelta(days=1),
        dt.replace(hour=21, minute=30) + timedelta(days=1)))

    t = dt.replace(hour=11, minute=0)
    best_connection, total_time = optimal_flight_connection(g, t, v1, v4)
    total_h = total_time.seconds / 3600 + total_time.days * 24
    assert best_connection == [e1, e7]
    assert total_h == 34.5


    t = dt.replace(hour=16, minute=0)
    best_connection, total_time = optimal_flight_connection(g, t, v4, v1)
    total_h = total_time.seconds / 3600 + total_time.days * 24
    assert best_connection == [e4]
    assert total_h == 9
