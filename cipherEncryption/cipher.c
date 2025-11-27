//Basic of cryptography-Cipher Text
#include<stdio.h>
#include<cs50.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>


int main(int argc,char *argv[] )
{
    if (argc != 2)
     {
        printf("Usage: ./cipher key\n");
        return 1;
     }


    {

        for(int j=0;j<strlen(argv[1]);j++)
        {
                  if(!isdigit(argv[1][j]))
                 {
                    printf("Key must be numeric!\n");
                    return 1;
                 }
        }


            int key = atoi(argv[1]);
            string text = get_string("plaintext: ");

            for(int i=0;i<strlen(text);i++)
            {

                if(isalpha(text[i]))
                {
                        if(islower(text[i]))
                        {
                            text[i] = ((text[i] - 'a' + key) % 26) + 'a';
                        }

                        else if(isupper(text[i]))
                        {
                            text[i] = ((text[i] - 'A' + key) % 26) + 'A';
                        }

                }

            }

            printf("ciphertext:%s\n",text);
            return 0;
    }


}
