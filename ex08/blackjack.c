#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define INVALID_DECK 1
#define NO_DECK 2
#define INVALID_CARD 3
#define CHEATING 4

void print_error(int errno) {
    switch (errno)
    {
        case INVALID_DECK:
            puts("ERROR: Invalid deck, only 23456789TJDKA are allowed");
            exit(errno);
        case NO_DECK:
            puts("ERROR: No deck provided, ./blackjack <deck> (23456789TJDKA)");    
            exit(errno);
        case INVALID_CARD:
            puts("ERROR: An invalid card was found in the deck.");
            exit(errno);
        case CHEATING:
            puts("ERROR: Cheating detected, more than 4 cards of the same value.");
            exit(errno);
        default:
            printf("ERROR: Unknown error %d\n", errno);
            break;
    }
}

int card_value(char card, int *sum) {
    if (card >= '2' && card <= '9')
        return card - '0';
    switch (card)
    {
        case 'J': // Jack
        case 'Q': // Queen
        case 'K': // King
        case 'T': // Ten
        case 'D': // Diamond
            return 10;
        case 'A':
            if (*sum + 11 > 21)
                return 1;
            else
                return 11;
        default:
            break;
    }
}

// Check for a maximum of 4 cards of the same value
int cheating(char *deck) {
    int cardsCounter[13] = {0};
    for (int i = 0; i < strlen(deck); i++) {
        switch (deck[i])
        {
            case '2':
                cardsCounter[0]++;
                break;
            case '3':
                cardsCounter[1]++;
                break;
            case '4':
                cardsCounter[2]++;
                break;
            case '5':
                cardsCounter[3]++;
                break;
            case '6':
                cardsCounter[4]++;
                break;
            case '7':
                cardsCounter[5]++;
                break;
            case '8':
                cardsCounter[6]++;
                break;
            case '9':
                cardsCounter[7]++;
                break;
            case 'T':
                cardsCounter[8]++;
                break;
            case 'J':
                cardsCounter[9]++;
                break;
            case 'Q':
                cardsCounter[10]++;
                break;
            case 'K':
                cardsCounter[11]++;
                break;
            case 'A':
                cardsCounter[12]++;
                break;
            default:
                break;
        }
    }
    // If there is a card with more than 4 cards, return true
    for (int i = 0; i < 13; i++) {
        if (cardsCounter[i] > 4)
            return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 2) print_error(NO_DECK);
    char possibleValues[14] = "23456789TJDKA\0";
    char *deck = argv[1];
    int length = strlen(deck);
    if (length == 0) print_error(NO_DECK);
    if (cheating(deck)) print_error(CHEATING);
    for (int i = 0; i < strlen(deck); i++) {
        if (strchr(possibleValues, deck[i]) == NULL)
            print_error(INVALID_DECK);
    }

    int score = 0;
    for (int i = 0; i < strlen(deck); i++) {
        score += card_value(deck[i], &score);
    }
    if (score != 21)
        printf("%d\n", score);
    else
        puts("Blackjack!");
}