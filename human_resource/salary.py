class Salary:
    """Simple Salary Information"""

    def __init__(self,  hourly_rate):
        self.hourly_rate = hourly_rate

    def salary_from_hours(self, hours):
        return hours * self.hourly_rate

    def salary_from_days(self, days):
        return (days * 8) * self.hourly_rate
