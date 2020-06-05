export fileid=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT
export filename=yolov4.weights

wget --quiet --save-cookies cookies.txt 'https://docs.google.com/uc?export=download&id='$fileid -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1/p' > confirm.txt
wget --quiet --load-cookies cookies.txt -O $filename 'https://docs.google.com/uc?export=download&id='$fileid'&confirm='$(<confirm.txt)
rm -f confirm.txt cookies.txt
