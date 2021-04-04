import pytest
import OPi.GPIO as GPIO


def test_pwm_wrong_chip_pin():

    # Test for a chip-pin combo that does not exist
    PWM_chip = 99
    PWM_pin = 99
    frequency_Hz = 500
    Duty_Cycle_Percent = 50

    with pytest.raises(Exception) as ex:

        GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
        if ex.errno == 2:
            assert str(ex.value) == "FileNotFoundError: [Errno 2] No such file or directory: '/sys/class/pwm/pwmchip{0}/export'".format(PWM_chip)
        elif ex.errno == 19:
            assert str(ex.value) == "OSError: [Errno 19] No such device"


def test_invalid_duty_cycle():

    PWM_chip = 0
    PWM_pin = 0
    frequency_Hz = 500
    Duty_Cycle_Percent_high = 150
    Duty_Cycle_Percent_low = -50

    with pytest.raises(Exception) as ex:
        p = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent_high)
        p.duty_cycle(150)
        assert str(ex.value) == "Duty cycle must br between 0 and 100. Current value: {0} is out of bounds".format(Duty_Cycle_Percent_high)
        p.pwm_close()

    with pytest.raises(Exception) as ex:
        p = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent_low)
        p.duty_cycle(-50)
        assert str(ex.value) == "Duty cycle must br between 0 and 100. Current value: {0} is out of bounds".format(Duty_Cycle_Percent_low)
        p.pwm_close()
