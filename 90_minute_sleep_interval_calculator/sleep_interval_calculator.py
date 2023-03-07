#incomplete

def SleepIntervalCalculator():
    hr_1 = 0
    min_1 = 0
    hr_2 = 0
    min_2 = 0

    def calculate_sleep_time_hr(time):
        if time > 0:
            if time // 60 == 0:
                return (time // 60) + 12
            else:
                return (time // 60)

        else:
            if time // 60 == 0:
                return ((720 + time) // 60) + 12
            else:
                return (720 + time) // 60

    def calculate_sleep_time_min(time, caller):
        if time > 30:
            if isinstance(time / 60, int):
                return time / 60
            elif isinstance(time / 60, float):
                if caller == "1":
                    hr_1 += time / 60
                else:
                    hr_2 += time / 60

                return time % 60 * 60

    sleep_duration = int(input("When do you want to wake up? (example input: 8 AM)\nInput here: ")) * 60

    hr_1 += calculate_sleep_time_hr(sleep_duration - 90 * 6)
    min_1 += calculate_sleep_time_min(abs(sleep_duration - 90 * 6), "1")
    hr_2 += calculate_sleep_time_hr(sleep_duration - 90 * 5)
    min_2 += calculate_sleep_time_min(abs(sleep_duration - 90 * 5), "2")


    print(f'{hr_1}:{min_1} or {hr_2}:{min_2}')




def main():
    sic = SleepIntervalCalculator()


if __name__ == '__main__':
    main()