class NationalPark:
    
    all = []

    def __init__(self, name):
        self._name = None
        self.name = name
        NationalPark.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, '_name_set'):
            if isinstance(value, str) and len(value) >= 3:
                self._name = value
                self._name_set = True
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        visitors = []
        for trip in self.trips():
            if trip.visitor not in visitors:
                visitors.append(trip.visitor)
        return visitors
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        if not self.visitors():
            return None
        
        visitor_counts = {}
        for trip in self.trips():
            visitor = trip.visitor
            visitor_counts[visitor] = visitor_counts.get(visitor, 0) + 1
        
        return max(visitor_counts, key=visitor_counts.get)
    
    @classmethod
    def most_visited(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda park: park.total_visits()) if any(park.total_visits() > 0 for park in cls.all) else None


class Trip:
    
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = None
        self._national_park = None
        self._start_date = None
        self._end_date = None
        
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        Trip.all.append(self)
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        if isinstance(value, NationalPark):
            self._national_park = value
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value


class Visitor:

    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        parks = []
        for trip in self.trips():
            if trip.national_park not in parks:
                parks.append(trip.national_park)
        return parks
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])