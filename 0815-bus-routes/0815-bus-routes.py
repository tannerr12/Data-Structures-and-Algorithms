class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Map each stop to the buses that go through it
        stop_to_buses = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus)
        
       # Set of visited stops and buses
        visited_stops = set([source])
        visited_buses = set()
        
        # Queue for BFS: each element is (stop, buses)
        # Initialize with source, 0 buses used
        queue = deque([(source, 0)])
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            if current_stop == target:
                return buses_taken

            for bus in stop_to_buses[current_stop]:
                # Skip if this bus has been used before
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                # Add all stops of this bus to the queue
                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        queue.append((next_stop, buses_taken + 1))
                        visited_stops.add(next_stop)

        # If no route found, return -1
        return -1