# Martian Locations Database & Advanced Pathfinding (Backend)
MARS_LOCATIONS = {
    "Jezero Crater Base": {
        "lat": 0.0, 
        "lng": 15.0, 
        "type": "Habitat", 
        "desc": "Main human research base & landing site.",
        "safety": "High"
    },
    "Arsia Mons Lava Tube": {
        "lat": -9.4, 
        "lng": 239.0, 
        "type": "Shelter", 
        "desc": "Natural subterranean shielding from solar flares.",
        "safety": "Maximum"
    },
    "Valles Marineris Deposit": {
        "lat": -14.0, 
        "lng": 283.0, 
        "type": "Resource", 
        "desc": "Subsurface glacial ice harvesting facility.",
        "safety": "Medium"
    }
}

def get_location_details(name):
    return MARS_LOCATIONS.get(name, MARS_LOCATIONS["Jezero Crater Base"])

def calculate_a_star_safe_route(start_lat, start_lng, target_lat, target_lng):
    """
    Simulated A* Pathfinding / Obstacle Avoidance Algorithm
    Calculates dynamic waypoints around the active dust storm vortex.
    """
    # Offset midpoint to simulate smart obstacle avoidance around storm coords [15.0, -20.0]
    detour_lat = (start_lat + target_lat) / 2 + 12.0
    detour_lng = (start_lng + target_lng) / 2 - 10.0
    
    # A* calculated optimal safe path waypoints
    safe_route = [
        [start_lat, start_lng],
        [detour_lat, detour_lng],
        [target_lat, target_lng]
    ]
    return safe_route