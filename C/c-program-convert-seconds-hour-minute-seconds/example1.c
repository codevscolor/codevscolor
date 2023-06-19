// https://codevscolor.com/c-program-convert-seconds-hour-minute-seconds

#include <stdio.h>

int main()
{
    int inputSecond;

    int hours, minutes, seconds;
    int remainingSeconds;

    int secondsInHour = 60 * 60;
    int secondsInMinute = 60;

    printf("Enter the seconds value: ");
    scanf("%d", &inputSecond);

    hours = (inputSecond / secondsInHour);

    remainingSeconds = inputSecond - (hours * secondsInHour);
    minutes = remainingSeconds / secondsInMinute;

    remainingSeconds = remainingSeconds - (minutes * secondsInMinute);
    seconds = remainingSeconds;

    printf("%d hour, %d minutes and %d seconds", hours, minutes, seconds);
}