{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your algorithm guesses the integer,on average, in 5 attempts\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np # Package import to create an array.\n",
    "\n",
    "\n",
    "def game_core_v3(number):\n",
    "    '''Game function to guess an integer in the range from 1 to 100.'''\n",
    "    count = 0 # Attempt Counter.\n",
    "    predict = np.random.randint(1,101) # Guessable integer.\n",
    "    min_unit=1 # Smallest random array integer.\n",
    "    max_unit=101 # largest random array integer.\n",
    "    while number!=predict:\n",
    "        count+=1\n",
    "        middle = (min_unit+max_unit)//2\n",
    "        if middle > number:\n",
    "            max_unit = middle \n",
    "        elif middle < number:\n",
    "            min_unit = middle  \n",
    "        else:\n",
    "            # Exiting the cycle if guessed right.\n",
    "            break \n",
    "    \n",
    "    return(count)\n",
    "\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Function to determine the speed of guessing for 1000 game's starts.'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # Fix RANDOM SEED to reproduce experiment.\n",
    "    random_array = np.random.randint(1,101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Your algorithm guesses the integer,on average, in {score} attempts\")\n",
    "    \n",
    "    return(score)\n",
    "\n",
    "\n",
    "score_game(game_core_v3) # Run check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
