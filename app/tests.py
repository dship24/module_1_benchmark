from django.test import SimpleTestCase
from django.http import response

class TestSumDouble(SimpleTestCase):
    def test_5_10(self):
        response = self.client.get('/warmup-1/sum_double/5/10/')
        self.assertContains(response, "15")

    def test_2_2(self):
        response = self.client.get('/warmup-1/sum_double/2/2/')
        self.assertContains(response, "8")

    def test_20_1(self):
        response = self.client.get('/warmup-1/sum_double/20/1/')
        self.assertContains(response, "21")

class TestAlarmClock(SimpleTestCase):
    def test_false_2(self):
        response = self.client.get('/logic-1/alarm_clock/False/2/')
        self.assertContains(response, "7:00")

    def test_false_6(self):
        response = self.client.get('/logic-1/alarm_clock/False/6/')
        self.assertContains(response, "10:00")

    def test_true_1(self):
        response = self.client.get('/logic-1/alarm_clock/True/1/')
        self.assertContains(response, "10:00")
    
    def test_true_6(self):
        response = self.client.get('/logic-1/alarm_clock/True/6/')
        self.assertContains(response, "off")

class TestLuckySum(SimpleTestCase):
    def test_5_13_2(self):
        response = self.client.get('/logic-2/lucky_sum/5/13/2/')
        self.assertContains(response, "5")

    def test_2_4_13(self):
        response = self.client.get('/logic-2/lucky_sum/2/4/13/')
        self.assertContains(response, "6")

    def test_13_6_3(self):
        response = self.client.get('/logic-2/lucky_sum/13/6/3/')
        self.assertContains(response, "0")

    def test_5_7_3(self):
        response = self.client.get('/logic-2/lucky_sum/5/7/3/')
        self.assertContains(response, "15")
