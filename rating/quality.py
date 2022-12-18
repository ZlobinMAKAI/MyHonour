from dataBases.getValue import getTest_mark, getActivity, getTg_id

def rank_counter(tg_iD):
    active_k = 1  # коэффициент увеличения активности
    test_k = 1  # коэффициент увеличения тестов

    test_points = int(getTest_mark(tg_iD)[0:2])  # балл студента за последний тест

    max_test = int(getTest_mark(tg_iD)[2:4])

    print("Enter active points of student:")
    active_points = int(input())  # сумма баллов за посещение мероприятий. 1 посещение = 10 баллов

    print("Enter max active points among student:")
    max_active = int(input())  # максимальный балл за активность среди всех студентов

    rank_points = 0  # рейтинговый балл, полученный по формуле

    if (0 <= active_points / max_active < 0.3):
        test_k = 1
    if (0.3 <= active_points / max_active < 0.6):
        test_k = 1.3
    if (0.6 <= active_points / max_active < 0.8):
        test_k = 1.6
    if (0.8 <= active_points / max_active <= 1):
        test_k = 2

    if (0 <= test_points / max_test < 0.3):
        active_k = 1
    if (0.3 <= test_points / max_test < 0.6):
        active_k = 1.5
    if (0.6 <= test_points / max_test < 0.8):
        active_k = 2
    if (0.8 <= test_points / max_test <= 1):
        active_k = 3

    rank_points = test_k * test_points + active_k * active_points / 20

    return rank_points


print("Rank points is:", rank_counter())