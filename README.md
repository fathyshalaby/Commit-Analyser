🔍 **CommitAnalyzer**: Perfecting Your Code's Paper Trail! 🔍

In the intricate dance of software development, commit messages are the footprints left behind. Enter **CommitAnalyzer** – ensuring every step is precise and informative! 💻📜

With a simple integration into your version control system, **CommitAnalyzer** scrutinizes every commit message, ensuring they align with your team's specified format or standard. Whether you're enforcing a particular verb tense, ticket number inclusion, or a specific structure, this tool ensures that every message is clear, consistent, and meaningful. 🛠️🔧

Benefits:
- **Consistency**: Maintain a uniform commit log, making it easier for team members to understand the project's history.
- **Automation**: Reduce manual reviews of commit messages, saving time and preventing oversights.
- **Integration**: Seamlessly integrates with popular version control systems like Git.
- **Customization**: Tailor the tool's rules to fit your team's unique requirements and standards.
- **Feedback Loop**: Provides real-time feedback to developers, suggesting improvements or corrections to their commit messages.

In the realm of code, where clarity is king, **CommitAnalyzer** ensures that your project's narrative is as polished as the code itself. Commit with confidence, knowing that your messages are in line with your team's best practices! 🔍📖


## Instructions:
Place the above Python code in the pre-commit file within the .git/hooks directory of your repository.
Make the pre-commit file executable:

chmod +x pre-commit

In the root of your repository, create a file named .commitformat.

Now, when a user tries to commit, the script will check the commit message against the regex pattern specified in .commitformat. If the commit message doesn't match, the commit will be halted, and an error message will be displayed.

This approach provides flexibility, as users can easily modify the .commitformat file to change the commit message requirements as needed.
