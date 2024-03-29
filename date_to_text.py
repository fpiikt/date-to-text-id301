"""
  �����: ��������� �������, ������ � S3355


  ���������� ��������� � ������� dateToStr(st)

"""
import time
import re

def dateToStr(st):
    """
    �������� �������

    �������� ������� �� ���������� ����������, ������������� � �������������� � ��� ������� - checkFormat � toStr,
    ����������� ������� �������� �� ��������������
    :param st: ������, ���������� ���� � ������� DD.MM.YYYY HH:MM:SS ��������� ���������� ��������:
    DD - {1 .. 31}
    MM - {1 .. 12}
    YYYY - {0001 .. 9999}
    HH - {0 .. 23}
    MM - {0 .. 60}
    SS - {0 .. 60}
    :return: ���������� ���������� ���� � ���� ������ �� ��������� �������� �� ������� �����, ���� ��������� �� ������,
    ���� ������ ����� ������������ ������ ��� ��������� �� ��������� ���������� ��������
    """


    dateVal = ("",
               "������",
               "������",
               "������",
               "���������",
               "�����",
               "������",
               "�������",
               "�������",
               "�������",
               "�������",
               "������������",
               "�����������",
               "�����������",
               "�������������",
               "�����������",
               "������������",
               "�����������",
               "�������������",
               "�������������",
               "���������",
               "�������� ������",
               "�������� ������",
               "�������� ������",
               "�������� ���������",
               "�������� �����",
               "�������� ������",
               "�������� �������",
               "�������� �������",
               "�������� �������",
               "���������",
               "�������� ������")

    monthVal = ("",
                "������",
                "�������",
                "�����",
                "������",
                "���",
                "����",
                "����",
                "�������",
                "��������",
                "�������",
                "������",
                "�������")

    yearThous = ("",
                 "���� ",
                 "��� ",
                 "��� ",
                 "������ ",
                 "���� ",
                 "����� ",
                 "���� ",
                 "������ ",
                 "������ ")

    yearThousOrd = ("",
                 "����",
                 "����",
                 "����",
                 "�������",
                 "����",
                 "�����",
                 "����",
                 "������",
                 "������")

    yearHundr = ("",
                 "��� ",
                 "������ ",
                 "������ ",
                 "��������� ",
                 "������� ",
                 "�������� ",
                 "������� ",
                 "��������� ",
                 "��������� ")

    yearHundrOrd = ("",
                 "",
                 "����",
                 "����",
                 "�������",
                 "����",
                 "�����",
                 "����",
                 "������",
                 "������")

    yearLessHundr = ("",
                     "�������",
                     "�������",
                     "��������",
                     "����������",
                     "������",
                     "�������",
                     "��������",
                     "��������",
                     "��������",
                     "��������",
                     "�������������",
                     "������������",
                     "������������",
                     "��������������",
                     "������������",
                     "�������������",
                     "������������",
                     "��������������",
                     "��������������",
                     "����������",
                     "�������� �������",
                     "�������� �������",
                     "�������� ��������",
                     "�������� ����������",
                     "�������� ������",
                     "�������� �������",
                     "�������� ��������",
                     "�������� ��������",
                     "�������� ��������",
                     "����������",
                     "�������� �������",
                     "�������� �������",
                     "�������� ��������",
                     "�������� ����������",
                     "�������� ������",
                     "�������� �������",
                     "�������� ��������",
                     "�������� ��������",
                     "�������� ��������",
                     "����������",
                     "����� �������",
                     "����� �������",
                     "����� ��������",
                     "����� ����������",
                     "����� ������",
                     "����� �������",
                     "����� ��������",
                     "����� ��������",
                     "����� ��������",
                     "������������",
                     "��������� �������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ����������",
                     "��������� ������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ��������",
                     "��������� ��������",
                     "�������������",
                     "���������� �������",
                     "���������� �������",
                     "���������� ��������",
                     "���������� ����������",
                     "���������� ������",
                     "���������� �������",
                     "���������� ��������",
                     "���������� ��������",
                     "���������� ��������",
                     "������������",
                     "��������� �������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ����������",
                     "��������� ������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ��������",
                     "��������� ��������",
                     "��������������",
                     "����������� �������",
                     "����������� �������",
                     "����������� ��������",
                     "����������� ����������",
                     "����������� ������",
                     "����������� �������",
                     "����������� ��������",
                     "����������� ��������",
                     "����������� ��������",
                     "�����������",
                     "��������� �������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ����������",
                     "��������� ������",
                     "��������� �������",
                     "��������� ��������",
                     "��������� ��������",
                     "��������� ��������")

    hourVal = ("����",
               "����",
               "���",
               "���",
               "������",
               "����",
               "�����",
               "����",
               "������",
               "������",
               "������",
               "�����������",
               "����������",
               "����������",
               "������������",
               "����������",
               "�����������",
               "����������",
               "������������",
               "������������",
               "��������",
               "�������� ����",
               "�������� ���",
               "�������� ���")

    smVal = ("",
            "����",
            "���",
            "���",
            "������",
            "����",
            "�����",
            "����",
            "������",
            "������",
            "������",
            "�����������",
            "����������",
            "����������",
            "������������",
            "����������",
            "�����������",
            "����������",
            "������������",
            "������������",
            "��������",
            "�������� ����",
            "�������� ���",
            "�������� ���",
            "�������� ������",
            "�������� ����",
            "�������� �����",
            "�������� ����",
            "�������� ������",
            "�������� ������",
            "��������",
            "�������� ����",
            "�������� ���",
            "�������� ���",
            "�������� ������",
            "�������� ����",
            "�������� �����",
            "�������� ����",
            "�������� ������",
            "�������� ������",
            "�����",
            "����� ����",
            "����� ���",
            "����� ���",
            "����� ������",
            "����� ����",
            "����� �����",
            "����� ����",
            "����� ������",
            "����� ������",
            "���������",
            "��������� ����",
            "��������� ���",
            "��������� ���",
            "��������� ������",
            "��������� ����",
            "��������� �����",
            "��������� ����",
            "��������� ������",
            "��������� ������",
            "����������")



    def checkFormat(st):
        """
        ������� ��� �������� ������������ ������� �������� ��������.


        ��� �������� ������ ����������������� � ������ ������ struct_time. � ���������� ���� ������ ������������ � ��������
        �������������� ��� ��������� ��������� ������ ����. ���� ������/�������� ������ �����������, ������������� ����������
        ValueError � �������������� � dateToStr

        :param st: ������, ���������� ���� � ������� DD.MM.YYYY HH:MM:SS
        :return: ������ ������ struct_time
        """

        try:
            fTime = time.strptime(st, "%d.%m.%Y %H:%M:%S")
        except ValueError:
            raise
        return fTime


    def toStr(fTime):
        """
        ������� ��� �������������� ������� ������ struct_time � ��������� �����.

        ����� ��������������� � ������ ����������� ������������ ����, ������� ����� ����� ������������ �����.
        ������� ����������� ��� - �� ���� ����������� ����� ��������, ����� �������� � �������� ������ �����. ����� �����
        ���������� �������� ���� �� ������, ����� ��� �������� ������ 1000 ��� 100 - ��� ���������� ���������� ���� ����
        "������", "���".
        ����� ���������� �������� "�������" ����� ���� � ����� ����������� ���������� ���� ���� "���", "������", "�������".
        :param fTime: ������ ������ struct_time
        :return: ���������� ���������� ���� � ���� ������ �� ��������� �������� �� ������� �����.
        """
        thousandN = 0
        hundredN = 0
        st = str(fTime.tm_year)
        if int(st) >= 1000:
            thousandN = int(st[0])
            hundredN = int(st[1])
            yearlessN = int(st[2] + st[3])
        elif int(st) >= 100:
            hundredN = int(st[0])
            yearlessN = int(st[1] + st[2])
        elif int(st) >= 10:
            yearlessN = int(st[0] + st[1])
        else:
            yearlessN = int(st[0])

        thousandW = " ����� "
        hundredW = " "
        yearThousUse = yearThous
        yearHundrUse = yearHundr

        if fTime.tm_year < 1000:
            thousandW = " "
        elif thousandN == 1: 
            thousandW = " ������ "
        elif thousandN in [2, 3, 4]: 
            thousandW = " ������ "

        if fTime.tm_year % 1000 == 0:
            thousandW = "��������� "
            yearThousUse = yearThousOrd
        elif fTime.tm_year % 100 == 0:
            hundredW = "������ "
            yearHundrUse = yearHundrOrd


        hourW = " ����� "
        if fTime.tm_hour in [1, 21]:
            hourW = " ��� "
        if fTime.tm_hour in [2, 3, 4, 22, 23]:
            hourW = " ���� "
        minuteW = " ����� "
        if fTime.tm_min in [1, 21, 31, 41, 51]:
            minuteW = " ������ "
        elif fTime.tm_min in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]:
            minuteW = " ������ "
        elif fTime.tm_min == 0:
            minuteW = " "
        secondW = " ������"
        if fTime.tm_sec in [1, 21, 31, 41, 51]:
            secondW = " �������"
        elif fTime.tm_sec in [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54]:
            secondW = " �������"
        elif fTime.tm_sec == 0:
            secondW = " "

        fStr = dateVal[fTime.tm_mday] + " " + monthVal[fTime.tm_mon] + " " + yearThousUse[thousandN] + thousandW + \
               yearHundrUse[hundredN] + hundredW + yearLessHundr[yearlessN] + " ���� " + hourVal[fTime.tm_hour] +\
               hourW + smVal[fTime.tm_min] + minuteW + smVal[fTime.tm_sec] + secondW
        fStr = re.sub(r'\s+', ' ', fStr)
        fStr = fStr.rstrip()
        return fStr

    #���� ����������
    try:
        fTime = checkFormat(st)
    except ValueError:
        return "������������ ������ ����"
    return toStr(fTime)
    #����� �����

if __name__ == "__main__":
    assert dateToStr("30.09.2019 15:32:45") == "��������� �������� ��� ������ �������������� ���� ���������� ����� �������� ��� ������ ����� ���� ������", "������ � �������� 1" # Ok
    assert dateToStr("2.3.1991 03:26:23") == "������ ����� ���� ������ ��������� ��������� ������� ���� ��� ���� �������� ����� ����� �������� ��� �������", "������ � �������� 2" # Ok
    assert dateToStr("30.02.1765 12:03:01") == "��������� ������� ���� ������ ������� ���������� ������ ���� ���������� ����� ��� ������ ���� �������", "������ � �������� 3" # ���������� ����������� ����� ��� ������
    assert dateToStr("13.06.0745 01:01:00") == "����������� ���� ������� ����� ������ ���� ���� ��� ���� ������" ,"������ � �������� 4" # Ok
    assert dateToStr("05.04.2000 00:59:02") == "����� ������ ������������� ���� ���� ����� ��������� ������ ����� ��� �������", "������ � �������� 5" # Ok
    assert dateToStr("25.09.185 18:45:34") == "�������� ����� �������� ��� ����������� ������ ���� ������������ ����� ����� ���� ����� �������� ������ �������", "������ � �������� 6" # ������������ ������ ����
    assert dateToStr("18.11.1565 20:00:34") == "������������� ������ ���� ������ ������� ���������� ������ ���� �������� ����� �������� ������ �������", "������ � �������� 7" # Ok
    assert dateToStr("23.09.3198 00:00:00") == "�������� ������ �������� ��� ������ ��� ��������� �������� ���� ���� �����", "������ � �������� 8" # Ok
    assert dateToStr("09.05.2001 01:67:23") == "������� ��� ��� ������ ������� ���� ���� ��� ���������� ���� ����� �������� ��� �������", "������ � �������� 9"  # ���������� ����������� �������� � �������
    assert dateToStr("11.12.1800 17:45:15") == "������������ ������� ���� ������ ������������ ���� ���������� ����� ����� ���� ����� ���������� ������", "������ � �������� 10"  # Ok

