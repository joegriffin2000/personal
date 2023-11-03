import java.util.Random;
import java.util.Scanner;

/* 
 * Abstract class definition of a game
 * Defines a two dimensional board, the current player, the size of the board, attributes for player records, and a move tracker
 * a number of abstract methods for playing the game are provided
*/
abstract class Game
{
	protected int num_moves = 0;
	protected String[][] board;
	protected String current_player = "  X  ";
	protected int size;
	protected int[] X_score = {0,0,0};
	protected int[] O_score = {0,0,0};

	public abstract boolean legal_move(int x, int y);
	public abstract void make_move(int x, int y);
	public abstract String game_over();
	public abstract void play_game();
	protected abstract void reset_game();	
	public abstract String toString();
	
}


/* 
 * TicTacToe game
 * In addition to the inheritance from above, defines two variables for gathering user input and random move generation
*/
class TicTacToe extends Game
{
	protected Scanner user_IO = new Scanner(System.in);
	protected Random rand = new Random();
	
	/* 
	 * Constructor for TicTacToe
	 * Allows for a board of size 3-9 to be constructed
	 * If the board is outside of those bounds, it is set to three
	 * Every board space is initially filled with (i,j), to allow the players easy access to where they can move
	*/
	public TicTacToe(int size)
	{
		if (size < 3 || size > 9)
		{
			System.out.println("Illegal size entered, setting size to 3");
			size = 3;
		}
		
		this.size = size;
		board = new String[this.size][this.size];

		for (int i = 0; i < this.size; i++)
		{
			for(int j = 0; j < this.size; j++)
			{
				board[i][j] = String.format("(%d,%d)", i, j);
			}
		}
	}
	
	/* 
	 * Public method to reset the game board. 
	 * Returns all spaces to (i,j), resets the move counter
	 * NOTE: We do not reset player (to allow for player O to sometimes start the game)
	*/
	public void reset_game()
	{
		board = new String[this.size][this.size];

		for (int i = 0; i < this.size; i++)
		{
			for(int j = 0; j < this.size; j++)
			{
				board[i][j] = String.format("(%d,%d)", i, j);
			}
		}
		
		num_moves = 0;
	}
	
	/* 
	 * Boolean method to determine if the input coordinates are a legal move
	 * First checks to ensure x and y are within the bounds of the matrix
	 * Then checks if board[x][y] is open
	*/
	public boolean legal_move(int x, int y)
	{
		if (x >= this.size || x < 0)
		{
			return false;
		}
		if (y >= this.size || y < 0)
		{
			return false;
		}
		if (board[x][y] == "  X  " || board[x][y] == "  O  ")
		{
			return false;
		}
		return true;
	}
	
	/* 
	 * Method to make a move
	 * Changes the value at board[x][y] to X or O
	 * NOTE: Does not do any error checking to ensure the square is open
	 * Must only be called after legal move is confirmed
	*/
	public void make_move(int x, int y)
	{
		board[x][y] = current_player;
		num_moves++;
		if (current_player == "  X  ")
		{
			current_player = "  O  ";
		}
		else
		{
			current_player = "  X  ";
		}
	}
	
	/* 
	 * Method for manual play
	 * Prints the board to the screen, and prompts the user for the coordinates they wish to move in
	 * We first validate that the input is integer, then that the move is legal
	 * If either of the above is false, we recall play game with an appropriate reminder for the user
	 * If the move is legal, it is executed and the win conditions are checked.
	 * If the game is over (either via a win or tie), the recursive loop exits
	 * Otherwise we continue play
	*/
	public void play_game()
	{
		System.out.println("*******************************\n\n");
		System.out.println(this.toString());
		int row_val = -1;
		int col_val = -1;
		// a try block is necessary due to casting user input
		try
		{
			System.out.println("Please enter the row you wish to move in");
			String row_input = user_IO.next();
			System.out.println("Please enter the column you wish to move in");
			String col_input = user_IO.next();
			row_val = Integer.parseInt(row_input);
			col_val = Integer.parseInt(col_input);
		}
		catch (NumberFormatException e)
		{
			System.out.println("One of the values you entered was not an integer. Please try again");
			play_game();
		}
		if (!(legal_move(row_val, col_val))) // If the coorindates entered are invalid targets
		{
			System.out.println(row_val);
			System.out.println("You have entered an invalid row or column value");
			System.out.println("Please enter a value between 0 and " + (size - 1));
			play_game();
		}
		else // Needs to be in an else clause to prevent recursive badness!
		{
			make_move(row_val, col_val);
			String result = game_over();
			if (result == "  X  ")
			{
				System.out.println("X has won the game!");
				X_score[0]++;
				O_score[1]++;
			}
			else if (result == "  O  ")
			{
				System.out.println("O has won the game!");
				X_score[1]++;
				O_score[0]++;
			}
			else if (num_moves == (size * size)) // If our number of moves is equal to size^2 and no one has won, the game is a tie
			{
				System.out.println("The game has ended in a tie!");
				X_score[2]++;
				O_score[2]++;
			}
			else
			{
				play_game();
			}
		}
	}
	
	/* 
	 * A method to randomly play the game
	 * The user provides a target number of games to play
	 * If the num_games is less than 10 it is set to 10
	 * If the num_games is greater than 1000 it is set to 1000
	 * We continuously generate random integers within the range [0-(size-1)] and try to make moves with them
	 * Otherwise the logic is identical to the loop above
	*/
	public void random_play_game(int num_games)
	{
		if (num_games < 10)
		{
			num_games = 10;
		}
		else if (num_games > 1000)
		{
			num_games = 1000;
		}
		System.out.println("Simulating " + num_games + " number of random Tic-Tac-Toe games!");
		int curr_games = 0;
		boolean game_won = false;
		int rand_x;
		int rand_y;
		String result;
		while (curr_games < num_games)
		{
			this.reset_game();
			game_won = false;
			result = "No winner";
			while (!game_won)
			{
				rand_x = rand.nextInt(size);
				rand_y = rand.nextInt(size);
				if (legal_move(rand_x, rand_y))
				{
					make_move(rand_x, rand_y);
				}
				result = game_over();
				if (result == "  X  ")
				{
					System.out.println("X has won the game!");
					X_score[0]++;
					O_score[1]++;
					game_won = true;
				}
				else if (result == "  O  ")
				{
					System.out.println("O has won the game!");
					X_score[1]++;
					O_score[0]++;
					game_won = true;
				}
				else if (num_moves == (size * size))
				{
					System.out.println("The game has ended in a tie!");
					X_score[2]++;
					O_score[2]++;
					game_won = true;
				}
			}
			curr_games++;
		}
		System.out.println("**************************\nTHE GAMES ARE OVER!\n\n");
		System.out.println("After " + num_games + " we have the following records");
		result = "Player\tWins\tLosses\tTies\n";
		result += String.format("X\t%d\t%d\t%d\n", X_score[0], X_score[1], X_score[2]);
		result += String.format("O\t%d\t%d\t%d\n", O_score[0], O_score[1], O_score[2]);
		System.out.println(result);
	}
	
	/* 
	 * A string method to return if the game is over
	 * This method is a String method so we can identify the winner explicitly
	*/
	public String game_over()
	{
		int i;
		int j;
		boolean all_same;
		
		// Horizontal check
		for (i = 0; i < size; i++)
		{
			all_same = true;
			for (j = 0; j < size-1; j++)
			{
				if (board[i][j] != board[i][j+1])
				{
					all_same = false;
					break;
				}
			}
			if (all_same)
			{
				return board[i][0];
			}
		}
		
		// Vertical check
		for (j = 0; j < size; j++)
		{
			all_same = true;
			for (i = 0; i < size-1; i++)
			{
				if (board[i][j] != board[i+1][j])
				{
					all_same = false;
					break;
				}
			}
			if (all_same)
			{
				return board[0][j];
			}
		}

		// DIagonal check
		all_same = true;
		for(i = 0; i < size - 1; i++)
		{
			if (board[i][i] != board[i+1][i+1])
			{
				all_same = false;
				break;
			}
		}
		if (all_same)
		{
			return board[0][0];
		}
		
		// Antidiagonal check
		all_same = true;
		for(i = 0; i < size - 1; i++)
		{
			if(board[i][size-i-1] != board[i+1][size-i-2])
			{
				all_same = false;
				break;
			}
		}
		
		if (all_same)
		{
			return board[0][size-1];
		}
		return "No winner!";
	}
	
	/* 
	 * A toString method to allow for easy printing
	*/
	public String toString()
	{
		String result = "Current Game Stats\n";
		result += "Player\tWins\tLosses\tTies\n";
		result += String.format("X\t%d\t%d\t%d\n", X_score[0], X_score[1], X_score[2]);
		result += String.format("O\t%d\t%d\t%d\n", O_score[0], O_score[1], O_score[2]);
		result += String.format("It is Player %s's turn\n", current_player);
		result += "CURRENT BOARD\n";
		for (int i = 0; i < size; i++)
		{
			for (int j = 0; j < size; j++)
			{
				result += board[i][j] + "\t";
			}
			result += "\n";
		}
		return result;
	}
	
}

/* 
 * TicTacToeTwo
 * A child class of TicTacToe
 * The only change is how victory is achieved
 * In this class we can achieve victory with a user defined run 
*/
class TicTacToeTwo extends TicTacToe
{
	// Instance variable for how many items in a row are needed
	private int num_consecutive;
	
	/* 
	 * Constructor
	 * Uses TicTacToe constructor for all inherited data points
	 * Defines num_consecutive as 3 if the entered value is < 3 or > size
	 * Otherwise it is the input value (meaning we could only need 5 consecutive on a 7x7 board)
	*/
	public TicTacToeTwo(int size, int num_consecutive)
	{
		super(size);
		if (num_consecutive < 3 || num_consecutive > this.size)
		{
			num_consecutive = 3;
		}
		this.num_consecutive = num_consecutive;
	}
	
	/* 
	 * The victory condition checker changes
	 * We must now count the consecutive occurrences
	 * Could be improved with faster cutoffs?
	 * Only checks matrix diagonal antidiagonal
	 * BONUS: Implement a check for all diagonal/antidiagonal runs
	*/
	public String game_over()
	{
		int i;
		int j;
		int counter;
		
		for (i = 0; i < size; i++)
		{
			counter = 1;
			for (j = 0; j < size-1; j++)
			{
				if (board[i][j] != board[i][j+1])
				{
					counter = 1;
				}
				else
				{
					counter++;
				}
				if (counter == num_consecutive)
				{
					return board[i][j];
				}
			}
		}
		
		for (j = 0; j < size; j++)
		{
			counter = 1;
			for (i = 0; i < size-1; i++)
			{
				if (board[i][j] != board[i+1][j])
				{
					counter = 1;
				}
				else
				{
					counter++;
				}
				if (counter == num_consecutive)
				{
					return board[i][j];
				}
			}
		}
		counter = 1;
		for(i = 0; i < size - 1; i++)
		{
			if (board[i][i] != board[i+1][i+1])
			{
				counter = 1;
			}
			else
			{
				counter++;
			}
			if (counter == num_consecutive)
			{
				return board[i][i];
			}
		}
		
		counter = 1;
		for(i = 0; i < size - 1; i++)
		{
			if(board[i][size-i-1] != board[i+1][size-i-2])
			{
				counter = 1;
			}
			else
			{
				counter++;
			}
			if (counter == num_consecutive)
			{
				return board[i][size-i-1];
			}
		}
		return "No winner!";
	}
}


/* 
 * Class to run main
*/
class Test_Games 
{
  public static void main(String[] args) 
  {
	System.out.println("Welcome to Tic Tac Toe!");
	System.out.println("We will be demoing two games, regular Tic Tac Toe, and a condensed version!");
	System.out.println("The condensed version will allow you to win in runs of 2-n, where n is the size of the board!");
	
	TicTacToe game_one = new TicTacToe(4);
	
	System.out.println("First we will validate the make move method and toString. Then we will call the play game and random play methods");
	System.out.println(game_one);
	game_one.make_move(0,0);
	game_one.make_move(1,2);
	game_one.make_move(3,3);
	System.out.println(game_one);
	
	System.out.println("We will now reset the board and play the game once via user input");
	game_one.reset_game();
	//game_one.play_game();
	//System.out.println("***************************\n********************\n");
	//System.out.println(game_one);
	
	System.out.println("Now to play random games!");
	game_one.random_play_game(200);
	
	
	TicTacToeTwo game_two = new TicTacToeTwo(4,3);
	
	//game_two.play_game();
	game_two.random_play_game(200);
	System.out.println(game_one);
	System.out.println(game_two);
	
  }
}