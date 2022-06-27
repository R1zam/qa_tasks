class Car:
    def __init__(self, make, model, year, trim, engine, transmission):
        self.make = make
        self.model = model
        self.year = year
        self.trim = trim
        self.engine = engine
        self.transmission = transmission

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_trim(self):
        return self.trim

    def get_engine(self):
        left_bracket = self.engine.rfind("(")
        wrong_space = self.engine[:left_bracket + 1].rfind(" ")
        self.engine_true = self.engine[:wrong_space] + self.engine[wrong_space + 1:]
        return self.engine_true

    def get_transmission(self):
        return self.transmission
