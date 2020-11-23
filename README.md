# GitHub-Automated-File-Uploader
A hands-free automated script that uploads files to your GitHub repository. The files don't have to be in a git directory, they can be anywhere.

Just type `upload` in Terminal, hit enter, and watch it go!

- [Setup](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#setup)   *(Less than a minute)*
- [Features](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#features)
- [Usage](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#usage)
- [Contact Me/Questions](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#contact-me--questions)

-----

## Setup
1. Copy paste the [bash function](https://github.com/ishaanjav/GitHub-Automated-File-Uploader/blob/main/bash_script.sh) into `bash_profile` or `bashrc`. On line 5 of the bash function, enter the path to the folder where the `upload.py` script is.
  - *To do this type `open ~/.bash_profile` or `nano ~/.bash_profile` and paste the code in (all inside Terminal)*
2. Install the Selenium Webdriver by typing this in Terminal: `pip install selenium`
3. In [`upload.py`](https://github.com/ishaanjav/GitHub-Automated-File-Uploader/blob/main/upload.py), enter in the link for the repository you want to upload to on line 14, and your GitHub login on lines 16 and 17.

**That's it! To run the automated tool just type `upload` in Terminal and hit enter!** For more commands check out the [Usage Section](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#usage).

-----

## Features
- Upload all files in a directory
- Upload specific files in a directory

### In this Repo:
- **Python script** 
  - for automated uploading of files to GitHub: just run `python upload.py` followed by the information in the [Usage Section](https://github.com/ishaanjav/GitHub-Automated-File-Uploader#usage)
- **Bash script** 
  - shorter command to run the automation tool: just type `upload` in terminal and hit enter!
  - uploads files even if the Python script is not in the same directory

## Usage
**Open Terminal and type:**
```
upload
```
**and that's it!**
If you want to upload specific files, type:
```
upload file1.txt file2.java file3.whatever file4.......
```

*Make sure to follow the instructions in the [Setup Section](https://github.com/ishaanjav/GitHub-Automated-File-Uploader/blob/main/README.md#setup). It takes less than a minute. 
Alternatively, you can run `python upload.py <DIRECTORY_TO_UPLOAD_FROM>` if you did not use the BASH script in this repo*

------

## Contact Me / Questions
Have any questions? Contact me at **ijapps101@gmail.com**

Give this a star if you found it useful and check out my [YouTube Channel](https://www.youtube.com/IJApps) for similar content.
