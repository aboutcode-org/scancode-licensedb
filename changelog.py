import os
from git import Repo

def generate_license_changelog():
    # Setup paths
    repo_path = '..'
    output_path = 'docs/changelog.md'
    # We look in etc because that is where the license files live
    search_path = 'etc'

    # Open the repository
    print("Opening repository...")
    repo = Repo(repo_path)
    
    # Get the last 50 changes
    print("Fetching recent commits...")
    commits = list(repo.iter_commits(paths=search_path, max_count=50))
    
    # Start building the Markdown table
    # We use a list called 'lines' to hold each row of our table
    lines = [
        "# License Changelog",
        "",
        "| Date | Action | License | Commit |",
        "| :--- | :--- | :--- | :--- |"
    ]

    # Loop through each commit to find what changed
    for commit in commits:
        # Get a readable date
        date_str = commit.authored_datetime.strftime("%Y-%m-%d")
        commit_hash = commit.hexsha[:7]

        # Comparing this commit with the one before it
        if commit.parents:
            diffs = commit.diff(commit.parents[0])
        else:
            # This is the very first commit in the repo
            diffs = commit.diff(None)

        for diff in diffs:
            # Look for the file name
            file_path = diff.b_path or diff.a_path
            
            # Check if it is a license YAML file
            if file_path.endswith('.yml') and 'licenses' in file_path:
                # Get just the name (like 'mit') instead of 'etc/licenses/mit.yml'
                license_name = os.path.basename(file_path).replace('.yml', '')
                
                # Decide if it was Added or Refined
                if diff.change_type == 'A':
                    action = "Added"
                else:
                    action = "Refined"
                
                # Add the row to our list
                new_row = f"| {date_str} | {action} | {license_name} | `{commit_hash}` |"
                lines.append(new_row)

    # Save the list to a file
    print(f"Saving changelog to {output_path}...")
    with open(output_path, 'w') as f:
        # Join all lines with a newline character
        f.write('\n'.join(lines))
    
    print("Done!")

if __name__ == "__main__":
    generate_license_changelog() 
