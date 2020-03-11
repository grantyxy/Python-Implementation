from datetime import datetime


class people:
    current_year = datetime.now().year

    def __init__(self, name, year, major):
        self._name = name
        self._year = year
        self._major = major

    def __str__(self):
        return f"""Name:  {self._name}
Year:  {self._year}
Major: {self._major}""" if self.check_valid_year() else "无效数据"

    def get_name(self):
        return self._name

    def get_year(self):
        return self._year

    def get_major(self):
        return self._major

    def set_name(self, name):
        self._name = name

    def set_year(self, year):
        self._year = year

    def set_major(self, major):
        self._major = major
    
    def check_valid_year(self):
        return self._year <= people.current_year


if __name__ == "__main__":
    a = people("Sun Xiaochuan", 2008, "Computer Science")
    print(a)

"""
Name:  Sun Xiaochuan
Year:  2008
Major: Computer Science
"""
