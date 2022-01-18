## Working with this repo
1. Use your machine's terminal to navigate to the parent directory where you want to place the folder containing this repository
2. On the repo's main page, click the green `Code` dropdown, then copy the link under the `HTTPS` option
3. On your terminal, type `git clone <URL_COPIED_FROM_GITHUB>`, where the entirety of `<URL_COPIED_FROM_GITHUB>` is replaced by the link from step 2
4. **Change directory (`cd`) into the newly copied folder**
6. *Pull* the latest updates from Github: `git pull origin`. **DO THIS WHENEVER YOU START WORKING!** *Note: this may erase local changes if you haven't previously saved them to the repo!*
7. When you are done making changes, use `git status` to see what files have changed (file types listed in `.gitignore` will never be committed)
8. Typically, use `git add .` to add all files in the folder to the staging area
9. Type `git commit -m "YOUR_COMMIT_MSG"`, where `"YOUR_COMMIT_MSG"` is a short description of your changes
10. Type `git push` to upload your changes to GitHub
11. Return to Step 5 next time you work on the repo