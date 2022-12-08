
# Justine Arzola 1804667 homework 4
def get_age():  # def statement to get age
    inputforage = int(input())
    if 18 <= inputforage <= 75:  # setting the range for the age group to test
        return inputforage
    raise ValueError("Invalid age.")  # raising error


def fat_burning_heart_rate(inputforage):  # def statement to calculate fat burn heart rate
    return (220 - inputforage) * 0.7


if __name__ == "__main__":
    try:
        inputforage = get_age()
        print("Fat burning heart rate for a", inputforage, "year-old:", fat_burning_heart_rate(inputforage), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")
