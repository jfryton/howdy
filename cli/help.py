# Prints a simple help page for the CLI

print("""
Usage:
  howdy <user> <command> [argument]

Commands:
  help          Show this help page
  list          List all saved face models for the current user
  add           Add a new face model for the current user
  remove [id]   Remove a specific model
  clear         Remove all face models for the current user
  test          Test the camera and recognition methods

For support please visit
https://github.com/Boltgolt/howdy\
""")
