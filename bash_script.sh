# Copy paste the below function into your bash_profile or bashrc file

upload(){
    loc=$PWD
    eval cd "<PATH TO FOLDER WHERE THE upload.py PYTHON SCRIPT IS>"
    # Change it to python3 based on your version of python
    python "upload.py" "$loc" "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "${10}" "${11}"
}
