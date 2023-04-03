# Je n'ai jamais ecrit de code en Perl, mais je ne le ferais plus jamais.

$input = <STDIN>;

# Chomp retire la fin de ligne
chomp($input);

if ($input eq reverse $input) {
    print("The string is a palindrome!\n");
} else {
    print("The string is not a palindrome.\n");
}
