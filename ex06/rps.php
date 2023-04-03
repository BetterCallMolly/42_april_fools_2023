<?php
    // Read from STDIN (https://www.php.net/manual/en/features.commandline.io-streams.php)
    $stdin = fopen('php://stdin', 'r');

    echo "Choose rock, paper, or scissors: ";
    // Trims remove whitespace and newlines from input (https://stackoverflow.com/questions/3727839/does-php-trim-remove-line-breaks)
    $choice = strtolower(trim(fgets($stdin)));

    $choices = ["rock", "paper", "scissors"];
    $computer_choice = $choices[rand(0, 2)];

    // Check if the user's choice is valid
    if (!in_array($choice, $choices)) {
        echo "We're playing 'rock, paper, scissors'. Not 'rock, paper, $choice'.\n";
        exit;
    }

    // Decide who won using if/else statements (dirty way for my mind)
    $win_msg = "Congratulations! You won! The computer chose $computer_choice.\n";

    if ($choice == $computer_choice) {
        echo "It's a tie! You both chose $choice.\n";
    } else if ($choice == "rock" && $computer_choice == "scissors") {
        echo $win_msg;
    } else if ($choice == "paper" && $computer_choice == "rock") {
        echo $win_msg;
    } else if ($choice == "scissors" && $computer_choice == "paper") {
        echo $win_msg;
    } else {
        echo "Sorry, you lost. The computer chose $computer_choice.\n";
    }
?>
