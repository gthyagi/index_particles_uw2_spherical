clc;
clear;

%Loading surface datasets
delimiterIn = ',';
sum_layer_org = importdata('./sum_layer_org_sxyz.txt');
sum_5up_layer_5 = importdata('./sum_5up_layer_5_sxyz.txt', delimiterIn);
sum_5up_layer_10 = importdata('./sum_5up_layer_10_sxyz.txt', delimiterIn);
sum_5up_layer_15 = importdata('./sum_5up_layer_15_sxyz.txt', delimiterIn);
sum_5up_layer_20 = importdata('./sum_5up_layer_20_sxyz.txt', delimiterIn);
sum_cont_plate = importdata('/Users/tgol0003/uw_thyagi/uw_codes/construct_shape/matlab_input/sum_cont_plate.txt');

sum_5up_layer_var = importdata('./sum_5up_layer_var_sxyz.txt');
sum_layer_var = importdata('./sum_layer_var_sxyz.txt');

% Creating color bar in km
color_value_slo = (1.0 - sqrt(sum_layer_org(:,3).^2 + sum_layer_org(:,2).^2 + sum_layer_org(:,1).^2))*6371.0;
color_value_slv = (1.0 - sqrt(sum_layer_var(:,3).^2 + sum_layer_var(:,2).^2 + sum_layer_var(:,1).^2))*6371.0;
color_value_sum_up = (1.0 - sqrt(sum_cont_plate(:,3).^2 + sum_cont_plate(:,2).^2 + sum_cont_plate(:,1).^2))*6371.0;
color_value_sum_up(color_value_sum_up <= 0.1) = 0.1;

%Visualizing data sets
visualize_points = true;
if visualize_points
%     scatter3(sum_layer_org(:,1),sum_layer_org(:,2),sum_layer_org(:,3),2,color_value_slo,'.'); %2 is the size of point
%     scatter3(sum_5up_layer_5(:,1),sum_5up_layer_5(:,2),sum_5up_layer_5(:,3),'.');
    scatter3(sum_5up_layer_10(:,1),sum_5up_layer_10(:,2),sum_5up_layer_10(:,3),'.');
    hold on;
%     scatter3(sum_5up_layer_15(:,1),sum_5up_layer_15(:,2),sum_5up_layer_15(:,3),'.');
%     scatter3(sum_5up_layer_20(:,1),sum_5up_layer_20(:,2),sum_5up_layer_20(:,3),'.');
    
%     scatter3(sum_cont_plate(:,1),sum_cont_plate(:,2),sum_cont_plate(:,3), color_value_sum_up, '.');
%     scatter3(sum_5up_layer_15(:,1),sum_5up_layer_15(:,2),sum_5up_layer_15(:,3),'.');
%     scatter3(sum_5up_layer_20(:,1),sum_5up_layer_20(:,2),sum_5up_layer_20(:,3),'.');
%     scatter3(sum_layer_var(:,1),sum_layer_var(:,2),sum_layer_var(:,3),2,color_value_slv,'.');
%     scatter3(sum_5up_layer_var(:,1),sum_5up_layer_var(:,2),sum_5up_layer_var(:,3),2,'.');
end

grid on;
hold on;
colormap(parula(14)); % or other colormap
colorbar; % color bar
caxis([0 700])


% % Creating oceanic and slab lithosphere bottom surface
% % oc_slab_litho_bot = importdata(string(mesh_data_path)+'oc_slab_litho_bot.txt');
% % x = oc_slab_litho_bot(:,1);
% % y = oc_slab_litho_bot(:,2);
% % z = oc_slab_litho_bot(:,3);
% % tri = delaunay(x,y);
% % trisurf(tri,x,y,z)

 
% % Creating alpha shapes 
% % oc_slab_litho_shp = alphaShape(oc_slab_litho(:,1), oc_slab_litho(:,2), oc_slab_litho(:,3));
% % oc_slab_crust_shp = alphaShape(oc_slab_crust(:,1), oc_slab_crust(:,2), oc_slab_crust(:,3));
% % sum_cont_shp = alphaShape(sum_cont(:,1),sum_cont(:,2),sum_cont(:,3));
% % him_cont_shp = alphaShape(him_cont(:,1),him_cont(:,2),him_cont(:,3));
% him_sum_box_shp = alphaShape(him_sum_box(:,1),him_sum_box(:,2),him_sum_box(:,3));
% % sum_slab_crust_shp = alphaShape(sum_slab_crust(:,1), sum_slab_crust(:,2), sum_slab_crust(:,3));
% % him_slab_crust_shp = alphaShape(him_slab_crust(:,1), him_slab_crust(:,2), him_slab_crust(:,3));
% % him_slab_litho_shp = alphaShape(him_slab_litho(:,1), him_slab_litho(:,2), him_slab_litho(:,3));
% 
% 
% %visualizing alpha shapes
% visualize_alpha_shape = true;
% if visualize_alpha_shape
% %     plot(oc_slab_litho_shp)
% %     plot(oc_slab_crust_shp)
% %     plot(sum_cont_shp)
% %     plot(him_cont_shp)
%     plot(him_sum_box_shp)
% %     plot(sum_slab_crust_shp)
% %     plot(him_slab_crust_shp)
% %     plot(him_slab_litho_shp)
% end