class Tester:
    results = {}

    def __init__(self, participants):
        self.participants = participants

    def test_implementations(self):
        for participant in self.participants:
            try:
                participant_result = participant.start()
            except Exception as e:
                print("Participant '{}' failed due to {}".format(participant.get_name(), e))
                participant_result = ("FAILED", 0, None)
            self.results[participant.get_name()] = participant_result
        return self.results
