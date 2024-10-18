class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turn_on: bool = False

    # giving our Microwave class a turn on method
    def turned_on(self) -> None:
        if self.turn_on:
            print(f'Microwave {self.brand} is already turned on.')
        else:
            self.turn_on = True
            print(f'Microwave {self.brand} is now turned on.')

    # giving our Microwave class a method that will run the microwave for a certain number of seconds
    def run(self, seconds: int) -> None:
        if self.turn_on:
            print(f'Running Microwave {self.brand} for {seconds} seconds.')
        else:
            print(f'Turn on the Microwave first!')

    # giving our Microwave class method that will be called when the microwave is done running
    def run_finished(self) -> None:
        print(f'Microwave {self.brand} has finished running.')

    # giving our Microwave class a turn off method
    def turned_off(self) -> None:
        if self.turn_on:
            self.turn_on = False
            print(f'Microwave {self.brand} is now turned off.')
        else:
            print(f'Microwave {self.brand} is already turned off.')

Bosch: Microwave = Microwave('Bosch', '1000W')
print(Bosch.brand, Bosch.power_rating)
Bosch.run(30)
Bosch.turned_on()
Bosch.run(30)
Bosch.run_finished()
Bosch.turned_off()
