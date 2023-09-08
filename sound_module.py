class Instrument:
    def __init__(self, name, pitch_range):
        self.name = name
        self._pitch_range = None  # Use a private attribute with a different name

    @property
    def pitch_range(self):
        return self._pitch_range
    
    @pitch_range.setter
    def pitch_range(self, pitch_range):
        if isinstance(pitch_range, list):
            self._pitch_range = pitch_range  # Use the private attribute

    def __repr__(self):
        return f"The range of the {self.name} goes from {self._pitch_range[0]} to {self._pitch_range[1]}"


class Woodwind(Instrument):
    def __init__(self, name, pitch_range):
        super().__init__(name, pitch_range)
    
    def frullato(self, notes):
        pass

class Stringed(Instrument):
    def __init__(self, name, pitch_range):
        super().__init__(name, pitch_range)
    
    def _double_stops(self, notes):
        pass

flute = Woodwind("flute", ['C4', 'G6'])  # Create an Instrument instance
flute.pitch_range = ['C4', 'G6']  # Set the pitch range using the setter
print(flute)


        
