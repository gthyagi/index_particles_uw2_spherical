# creates grid using xyz 
# then converts the grid to xyz
lon_min=$1
lon_max=$2
lat_min=$3
lat_max=$4
input_file=$5
output_file=$6

gmt xyz2grd $input_file -Gsum_5up_layer_5.nc -R$lon_min/$lon_max/$lat_min/$lat_max -I0.05
gmt grd2xyz sum_5up_layer_5.nc | awk '{print $1","$2","$3}' > $output_file
