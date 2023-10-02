import sys


def command_args():
    # Get total number of arguments
    total_args = len(sys.argv)

    if(total_args == 1):
        print("No command-line arguments provided.")
    else:
        print(f"Total command line arguments: {total_args - 1}")
        print("Arguments:")
        for i in range(1, total_args):
            print(f"{i}. {sys.argv[i]}")


if __name__ == "__main__":
    command_args()