import subprocess

def git_pull():
    # Change directory to the specified path
    git_path = r"C:\Users\Admin\Documents\Get"
    try:
        # Execute the Git pull command
        subprocess.check_output(['git', 'pull'], cwd=git_path)
        print("Git pull completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Git pull failed with error:", e.output)

if __name__ == "__main__":
    git_pull()
