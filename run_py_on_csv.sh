
#get arg1 and arg2
if [ $# -ne 1 ]
then
    echo "Usage: $0 arg1"
    exit 1
fi
arg1=$1

# loop through all files in the directory and subdirectories and finf .csv files
for file in $(find . -name "*.csv")
do
    # run python script on each file
    python3 $arg1 $file
done
