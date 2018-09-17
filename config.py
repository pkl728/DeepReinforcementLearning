#### SELF PLAY
EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 30000
TURNS_UNTIL_TAU0 = 10 # turn on which it starts playing deterministically
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

HIDDEN_CNN_LAYERS = [
	{'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 20
SCORING_THRESHOLD = 1.3

#### Gmail Settings
GMAIL_ACCOUNT = "your_email@gmail.com"
GMAIL_PASSWORD = "your_password"

#### CoreML Setting
CREATOR_NAME = "Patrick Lind"
CREATOR_LICENSE = "GNU General Public License v3.0"
MODEL_DESCRIPTION = "Model trained to play Connect4"
MODEL_INPUT_DESCRIPTION = "Input is a multi-array consisting of current player\'s positions and available positions."
MODEL_OUTPUT_DESCRIPTION = "Probabilities of success for moves to choose from"
