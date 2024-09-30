class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participant_count += 1  # Increment the participant count

    def get_participant_count(self):
        return self.participant_count  # Return the current participant count

# Example usage:
event = Event("Python Workshop", "2024-10-15")
print(f"Initial participant count: {event.get_participant_count()}")  # Output: 0

event.add_participant()
event.add_participant()
print(f"Participant count after adding participants: {event.get_participant_count()}")  # Output: 2