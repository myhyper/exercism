dic = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}
class Allergies:

    def __init__(self, score):
        self.score = score
        self.arr = []

    def allergic_to(self, item):
        return (self.score & dic[item]) is dic[item]

    @property
    def lst(self):
        rtv = []
        for key in dic:
            if (self.score & dic[key]) is dic[key]:
                rtv.append(key)
        return rtv
