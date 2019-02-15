for filename in `ls *`; 
do 
	mv "$filename" "prefix_$filename" 
done;
