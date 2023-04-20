// https://codevscolor.com/c-program-read-file-contents-character

#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *input;
	FILE *output;
	char ch;

	input = fopen("example.txt", "r");
	output = fopen("output.txt", "w");

	if (input == NULL)
	{
		printf("File is not available \n");
		return 0;
	}
	else
	{
		while ((ch = fgetc(input)) != EOF)
		{
			fputc(ch, output);
		}
	}

	fclose(input);
	fclose(output);

	return 0;
}