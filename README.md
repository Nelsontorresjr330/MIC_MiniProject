# MyMiniProject
## Installation and Deployment
First, install the MyMiniProject following:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)

Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`. On Intel Mac the proper directory should be `/usr/local/var/mongodb` and on Apple Silicon Mac it is `/opt/homebrew/var/mongodb` ).

You may need to run `npm install` or `npm upgrade` to make sure everything is up to date. Next up, you will need to have [webgme-cli](https://github.com/webgme/webgme-cli) installed as well so run `npm install -g webgme-cli`.

Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using MyMiniProject!

# PlugIns
All the PlugIns are accessable via the OneViz visualizer toolbar
 * Undo Button : Deletes the most recent operation
 * SetValues Button : Updates the values on the nodes to display their calculated values
 * CheckSolution Button : Checks to see if the target has been reached (Currently displays result in logger)
 * ValidPuzzle Button : Checks to make sure there are no more than 5 operations, exactly 6 nodes and all values are not -1 each (Currently displays result in logger)
 * GeneratePuzzles Button :  MUST BE USED IN DIGITS META CONTEXT, NOT PUZZLE CONTEXT! Generates 6 puzzles with random values and targets each, does not necessarily have a solvable solution.
